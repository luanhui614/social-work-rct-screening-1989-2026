"""Verify frozen counts, recorded decisions, cleaning and reproducibility."""
import argparse,json,hashlib,re,math
from pathlib import Path
from collections import Counter
from study import read_jsonl,analyze,aggregate_links,decision,consensus
from cleaning import reconstruct
P=Path(__file__).resolve().parents[1]
def load(p):return json.loads(p.read_text())
def same(a,b):
    if isinstance(a,float) and isinstance(b,(int,float)):return math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-12)
    if isinstance(a,dict):return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    return a==b
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--snapshot',action='store_true');parser.add_argument('--generated',action='store_true');args=parser.parse_args()
    status=load(P/'RELEASE_STATUS.json');assert status['analysis_status']=='frozen' and status['final_results_available']
    rows=read_jsonl(P/'data/record_level_results.jsonl.gz');assert len(rows)==89083
    assert len({(r['corpus'],r['record_id']) for r in rows})==len(rows)
    mapping=load(P/'data/duplicate_article_mapping.json');rebuilt=reconstruct(rows,mapping)
    for a,b in zip(rows,rebuilt):
        for k in ['is_duplicate','year','analysis_record_id','cleaning_exclusion_reason']:assert a[k]==b[k],(a['record_id'],k)
    clean=[r for r in rows if not r['is_duplicate'] and not r['insufficient_abstract']]
    assert len(clean)==87575
    assert sum(r['original_is_duplicate'] for r in rows if r['corpus']=='swrd')==872
    assert sum(r['cleaning_exclusion_reason']=='additional_bibliographic_duplicate' for r in rows)==614
    assert sum(r['is_duplicate'] for r in rows if r['corpus']=='swrd')==1486
    assert sum(r['is_duplicate'] for r in rows if r['corpus']=='sswr')==21
    assert sum(r['insufficient_abstract'] and not r['is_duplicate'] for r in rows)==1
    a=analyze(rows);t=a['summary']['totals']
    assert (t['swrd']['n'],t['swrd']['rct'],t['swrd']['individual'],t['swrd']['cluster'])==(63803,384,351,33)
    assert (t['sswr']['n'],t['sswr']['rct'],t['sswr']['individual'],t['sswr']['cluster'])==(23772,559,474,85)
    for cp in ['swrd','sswr']:
        for n in ['annual','period']:
            q=[x for x in a[n] if x['corpus']==cp]
            assert sum(x['n'] for x in q)==t[cp]['n'] and sum(x['rct'] for x in q)==t[cp]['rct']
        q=a['journals'] if cp=='swrd' else a['conference_formats']
        assert sum(x['n'] for x in q)==t[cp]['n'] and sum(x['rct'] for x in q)==t[cp]['rct']
    assert sum(r['in_original_audit'] for r in rows)==1622
    assert sum(r['in_original_audit'] for r in clean)==1612
    assert sum(r['final_reference_label'] is not None for r in clean)==1613
    by={(r['corpus'],r['record_id']):r for r in rows}
    for ids,label in [(['33736','82759'],'INDIVIDUAL'),(['34120','82763'],'OTHER'),(['82865','122194'],'INDIVIDUAL')]:
        assert {by['swrd',i]['final_reference_label'] for i in ids}=={label}
        assert len({by['swrd',i]['analysis_record_id'] for i in ids})==1
    assert by['swrd','37634']['final_reference_label']=='SECONDARY' and not by['swrd','37634']['in_original_audit']
    refs=read_jsonl(P/'data/reference_coding.jsonl');assert len(refs)==1622
    for r in refs:assert r['final_reference_label']==by[r['corpus'],r['record_id']]['final_reference_label']
    for r in clean:
        if r['screening_group']!='concordant_negative':assert r['final_reference_label'] is not None
    assert consensus('INDIVIDUAL','CLUSTER')=='concordant_positive'
    assert consensus('INDIVIDUAL','OTHER')=='discordant'
    assert consensus('SECONDARY','QUASI')=='concordant_negative'
    pairs=read_jsonl(P/'data/linkage_pair_assessments.jsonl');assert len(pairs)==327
    assert len({(r['conference_record_id'],r['journal_record_id']) for r in pairs})==327
    author={('2006-U-0255','19969'):'SAME',('2017-U-0064','70280'):'SAME',('2019-U-0627','69175'):'RELATED',('2022-O-0031','61715'):'SAME'}
    for key,value in author.items():assert next(r for r in pairs if (r['conference_record_id'],r['journal_record_id'])==key)['relation']==value
    cs=[r for r in clean if r['corpus']=='sswr' and decision(r)[1]];links=aggregate_links(cs,pairs)
    assert links==read_jsonl(P/'data/linkage_record_outcomes.jsonl')
    assert Counter(r['outcome'] for r in links)==Counter(SAME=90,RELATED_ONLY=99,INDETERMINATE=9,NOT_IDENTIFIED=361)
    assert len({r['journal_record_id'] for r in pairs if r['relation']=='SAME'})==73
    assert sum(r['relation']=='SAME' for r in pairs)==115
    for r in rows:assert 'abstract' not in r and 'reviewer' not in r
    if args.generated:
        for n,x in a.items():assert same(x,load(P/'results'/(n+'.json'))),n
        assert load(P/'results/linkage_record_outcomes.json')==links
        assert load(P/'figures/source_data/Figure_1.json')==a['annual']
        assert load(P/'figures/source_data/Figure_2.json')==a['journals']
    if args.snapshot:
        lines=(P/'MANIFEST.sha256').read_text().splitlines();expected={}
        for line in lines:
            digest,name=line.split('  ',1);expected[name]=digest
            assert hashlib.sha256((P/name).read_bytes()).hexdigest()==digest,name
        actual={str(p.relative_to(P)) for p in P.rglob('*') if p.is_file() and not any(x in p.parts for x in ['.git','__pycache__','.provisional_results']) and p.name!='MANIFEST.sha256'}
        assert actual==set(expected),(actual-set(expected),set(expected)-actual)
    print('PASS: frozen source-to-analysis chain, author decisions, subgroup sums, current linkage and reproduction checks.')
if __name__=='__main__':main()
