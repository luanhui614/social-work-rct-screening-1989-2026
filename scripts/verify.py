#!/usr/bin/env python3
"""Check reproducibility, provenance and the statistical-release hold separately."""
import argparse
import hashlib
import json
import math
import re
from collections import Counter
from pathlib import Path
from study import aggregate_links,analyze,consensus,decision,read_jsonl
from check_release_status import blockers
ROOT=Path(__file__).resolve().parents[1]

def equivalent(a,b):
    if isinstance(a,float) or isinstance(b,float):return isinstance(a,(int,float)) and isinstance(b,(int,float)) and math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-12)
    if isinstance(a,dict):return isinstance(b,dict) and a.keys()==b.keys() and all(equivalent(a[k],b[k]) for k in a)
    if isinstance(a,list):return isinstance(b,list) and len(a)==len(b) and all(equivalent(x,y) for x,y in zip(a,b))
    return a==b

def check(condition,message):
    if not condition:raise ValueError(message)

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--snapshot',action='store_true');parser.add_argument('--generated',action='store_true');args=parser.parse_args()
    status=json.loads((ROOT/'RELEASE_STATUS.json').read_text());cfg=json.loads((ROOT/'config/study.json').read_text());expected=cfg['snapshot_expected']
    check(status['final_results_available'] is False and cfg['final_results_available'] is False,'This development snapshot must not advertise final statistical results.')
    check(bool(blockers()),'Open identity issues must keep final release blocked.')
    rows=read_jsonl(ROOT/'data/record_level_results.jsonl');a=analyze(rows);summary=a['summary']
    check(len(rows)==expected['raw_journal_n']+expected['raw_conference_n'],'Unexpected raw screening count.')
    for c,prefix in [('swrd','journal'),('sswr','conference')]:
        t=summary['totals'][c]
        check(t['n']==expected['analysis_'+prefix+'_n'],'Retained snapshot denominator differs from configuration.')
        check(t['rct']==expected[prefix+'_rct_reports'],'Retained category snapshot changed without documentation.')
        for name in ['annual','period','journals' if c=='swrd' else 'conference_formats']:
            group=[r for r in a[name] if r['corpus']==c]
            check(sum(r['n'] for r in group)==t['n'] and sum(r['rct'] for r in group)==t['rct'],'Group totals fail reconciliation.')
    check(sum(r['review_ids'] for r in a['human_audit'])==expected['original_audit_ids'],'Historical workbench membership changed.')
    # Current categories are preserved; identity problems are not silently recoded.
    by={(r['corpus'],r['record_id']):r for r in rows}
    cases=json.loads((ROOT/'data/identity_qc_cases.json').read_text())['cases']
    check(len(cases)==4,'Expected the documented open identity cases.')
    for c in cases:
        check(all((c['corpus'],rid) in by for rid in c['record_ids']),'QC case cannot be traced to its source IDs.')
        check(all(not by[c['corpus'],rid]['is_duplicate'] for rid in c['record_ids']),'Known merges must not be silently applied to a preserved snapshot.')
    check(by['swrd','33736']['final_reference_label']=='INDIVIDUAL' and by['swrd','82759']['final_reference_label']=='CLUSTER','Retained randomization-level conflict was overwritten.')
    check(by['swrd','37634']['final_reference_label']=='SECONDARY' and not decision(by['swrd','37634'])[1] and not by['swrd','37634']['in_original_audit'],'Additional author decision incorrectly changes original audit membership.')
    refs=read_jsonl(ROOT/'data/reference_coding.jsonl')
    check(len(refs)==expected['original_audit_ids'],'Reference source-record count differs.')
    for r in refs:check(r['final_reference_label']==by[r['corpus'],r['record_id']]['final_reference_label'],'Reference snapshot does not join to screening snapshot.')
    check(consensus('INDIVIDUAL','CLUSTER')=='concordant_positive','Allocation-level disagreement incorrectly changes binary triage.')
    check(consensus('QUASI','INDIVIDUAL')=='discordant' and consensus('OTHER','SECONDARY')=='concordant_negative','Binary triage error.')
    pairs=read_jsonl(ROOT/'data/linkage_pair_assessments.jsonl');check(len(pairs)==expected['linkage_pair_n'],'Pair snapshot count differs.')
    check(len({(p['conference_record_id'],p['journal_record_id']) for p in pairs})==len(pairs),'Duplicate pair keys.')
    author_pairs={(p['conference_record_id'],p['journal_record_id']):p['relation'] for p in pairs if p['author_adjudicated']}
    check(author_pairs=={('2006-U-0255','19969'):'SAME',('2017-U-0064','70280'):'SAME',('2019-U-0627','69175'):'RELATED',('2022-O-0031','61715'):'SAME'},'Explicit retained author linkage decisions changed.')
    links=aggregate_links([r for r in rows if r['corpus']=='sswr' and decision(r)[1]],pairs)
    check(Counter(r['outcome'] for r in links)==expected['linkage_counts'],'Current linkage snapshot aggregation differs.')
    stored=read_jsonl(ROOT/'data/linkage_record_outcomes.jsonl')
    check(equivalent(links,[{k:r[k] for k in links[0]} for r in stored]),'Pair and report-level linkage snapshots disagree.')
    same=[p for p in pairs if p['relation']=='SAME'];check(len(same)==115 and len({p['journal_record_id'] for p in same})==73,'Pair versus article unit reconciliation failed.')
    check(sum(r['conference_year']<=2021 for r in links)==423,'Mature-cohort snapshot differs.')
    forbidden={'abstract','title','authors','reviewer_name','original_merged_label','latest_human_label','original_criteria','freeze_version'}
    check(all(not forbidden.intersection(r) for r in rows),'A private/source-content field entered minimized screening data.')
    prompt=json.loads((ROOT/'materials/initial_screening_prompt_v2.json').read_text())
    blocks=re.findall(r'```text\n(.*?)\n```',(ROOT/'docs/MODEL_PROMPT_v2.md').read_text(),re.S)
    check(blocks==[prompt['system'],prompt['user_template']],'Documented prompt text was altered.')
    files=[p for p in ROOT.rglob('*') if p.is_file() and not set(p.relative_to(ROOT).parts).intersection({'.git','__pycache__','.provisional_results'})]
    for p in files:
        rel=p.relative_to(ROOT);check('archive' not in [x.casefold() for x in rel.parts],'Local archive entered public tree.')
        check(p.suffix not in {'.docx','.xlsx','.zip','.bundle','.log'},'A private or unsupported artifact entered public tree.')
        if p.suffix=='.md':
            text=re.sub(r'```.*?```','',p.read_text(),flags=re.S)
            for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text):
                if target.startswith(('http:','https:','#')):continue
                check((p.parent/target.split('#')[0]).exists(),'Broken local documentation link in '+str(rel)+': '+target)
    check(not (ROOT/'materials/original_reference_benchmark.json').exists(),'Superseded benchmark re-entered active analysis.')
    for folder in ['figures','tables','results']:check([p.name for p in (ROOT/folder).iterdir() if p.is_file()]==['README.md'],'Uncleared generated output entered active tree.')
    if args.generated:
        out=ROOT/'.provisional_results';check((out/'analysis_status.json').exists(),'No provisional output status.')
        check(json.loads((out/'analysis_status.json').read_text())['analysis_status']=='provisional_snapshot_not_final','Generated output missing provisional qualification.')
        for name,obj in a.items():check(equivalent(obj,json.loads((out/(name+'.json')).read_text())),'Generated output differs: '+name)
        check(equivalent(links,json.loads((out/'linkage_record_outcomes.json').read_text())),'Generated linkage differs.')
    manifest=ROOT/'MANIFEST.sha256'
    if args.snapshot:
        names=[]
        for line in manifest.read_text().splitlines():
            digest,name=line.split('  ',1);names.append(name);check(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,'Hash mismatch: '+name)
        check(set(names)=={str(p.relative_to(ROOT)) for p in files if p.name!='MANIFEST.sha256'},'Manifest and public file inventory differ.')
    print('PASS: preserved snapshot arithmetic, current linkage, prompt fidelity, publication file scope and final-release hold. This is not certification of completed identity QC.')
if __name__=='__main__':main()
