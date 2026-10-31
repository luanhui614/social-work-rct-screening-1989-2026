#!/usr/bin/env python3
"""Check final counts, scope and release contents before publication."""
import json
import hashlib
import math
import re
import sys
from collections import Counter
from pathlib import Path
from study import aggregate_links,analyze,consensus,decision,read_jsonl
ROOT=Path(__file__).resolve().parents[1]
def equivalent(a,b):
    """Permit floating-point roundoff across supported Python versions only."""
    if isinstance(a,float) or isinstance(b,float):
        return isinstance(a,(int,float)) and isinstance(b,(int,float)) and math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-12)
    if isinstance(a,dict):return isinstance(b,dict) and a.keys()==b.keys() and all(equivalent(a[k],b[k]) for k in a)
    if isinstance(a,list):return isinstance(b,list) and len(a)==len(b) and all(equivalent(x,y) for x,y in zip(a,b))
    return a==b
def main():
    rows=read_jsonl(ROOT/'data/record_level_results.jsonl');a=analyze(rows);s=a['summary']
    assert len(rows)==89083
    assert (s['totals']['swrd']['n'],s['totals']['swrd']['rct'])==(64417,388)
    assert (s['totals']['sswr']['n'],s['totals']['sswr']['rct'])==(23772,559)
    assert (s['journal_count'],s['journals_with_rct'],s['top2_rcts'],s['top15_rcts'])==(88,46,188,322)
    assert sum(r['review_ids'] for r in a['human_audit'])==1622
    assert sum(r['classifiable_deduplicated'] for r in a['human_audit'])==1617
    assert consensus('INDIVIDUAL','CLUSTER')=='concordant_positive'
    assert consensus('OTHER','SECONDARY')=='concordant_negative'
    assert consensus('QUASI','INDIVIDUAL')=='discordant'
    # Final reference coding overrides model consensus in both directions.
    known=next(r for r in rows if r['corpus']=='swrd' and r['record_id']=='37634')
    assert known['final_reference_label']=='SECONDARY' and not decision(known)[1] and not known['in_original_audit']
    for c in ['swrd','sswr']:
        for name in ['annual','period','journals' if c=='swrd' else 'conference_formats']:
            z=[r for r in a[name] if r['corpus']==c]
            assert sum(r['n'] for r in z)==s['totals'][c]['n']
            assert sum(r['rct'] for r in z)==s['totals'][c]['rct']
    links=aggregate_links([r for r in rows if r['corpus']=='sswr' and decision(r)[1]],read_jsonl(ROOT/'data/linkage_pair_assessments.jsonl'))
    assert Counter(r['outcome'] for r in links)=={'SAME':83,'RELATED_ONLY':68,'INDETERMINATE':29,'NOT_IDENTIFIED':379}
    for name,expected in a.items():
        result=ROOT/'results'/(name+'.json')
        if result.exists():assert equivalent(expected,json.loads(result.read_text())),name
    result=ROOT/'results/linkage_record_outcomes.json'
    if result.exists():assert equivalent(links,json.loads(result.read_text()))
    forbidden={'abstract','title','authors','reviewer_name','original_merged_label','latest_human_label','original_criteria','freeze_version'}
    assert all(not (forbidden & set(r)) for r in rows)
    tracked_files=[p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts]
    for p in tracked_files:
        assert 'archive' not in [x.casefold() for x in p.relative_to(ROOT).parts]
        assert p.suffix not in {'.docx','.xlsx','.zip','.bundle','.log'}
        assert p.stat().st_size<100*1024*1024
    materials=json.loads((ROOT/'materials/initial_screening_prompt_v2.json').read_text())
    prompt_blocks=re.findall(r'```text\n(.*?)\n```',(ROOT/'docs/MODEL_PROMPT_v2.md').read_text(),re.S)
    assert prompt_blocks==[materials['system'],materials['user_template']]
    design=json.loads((ROOT/'materials/original_review_design.json').read_text())
    for c,total,overlap in [('swrd',748,8),('sswr',874,12)]:
        x=design[c];assert x['unique']==total and x['overlap_boundary_keyword']==overlap
        assert sum(x['samples'].values())-overlap==total
        assert x['seed']==20260905 and x['boundary_threshold']==0.02
    for p in tracked_files:
        if p.suffix!='.md':continue
        prose=re.sub(r'```.*?```','',p.read_text(),flags=re.S)
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',prose):
            if target.startswith(('http:','https:','#')):continue
            assert (p.parent/target.split('#')[0]).exists(),(p,target)
    manifest=ROOT/'MANIFEST.sha256'
    if manifest.exists():
        for line in manifest.read_text().splitlines():
            expected,name=line.split('  ',1)
            # Published bytes can be checked before regeneration. Afterwards,
            # compare derived numerical results above: Python 3.12 improved
            # float summation and can change only the last serialized digit.
            if name.startswith('results/') and '--snapshot' not in sys.argv:continue
            assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==expected,name
    print('PASS: scientific counts, classification precedence, audit units, linkage aggregation and publication file boundary.')
if __name__=='__main__':main()
