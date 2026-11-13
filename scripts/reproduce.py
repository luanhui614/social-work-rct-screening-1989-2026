"""Reproduce frozen descriptive results from retained model/reference calls."""
import json
from pathlib import Path
from collections import Counter
from study import analyze,aggregate_links,decision,markdown,read_jsonl
from check_release_status import blockers
ROOT=Path(__file__).resolve().parents[1]
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def main():
    assert not blockers()
    rows=read_jsonl(ROOT/'data/record_level_results.jsonl.gz')
    out=ROOT/'results';out.mkdir(exist_ok=True)
    a=analyze(rows)
    for n,x in a.items():save(out/(n+'.json'),x)
    conferences=[r for r in rows if r['corpus']=='sswr' and not r['is_duplicate'] and not r['insufficient_abstract'] and decision(r)[1]]
    links=aggregate_links(conferences,read_jsonl(ROOT/'data/linkage_pair_assessments.jsonl'))
    save(out/'linkage_record_outcomes.json',links)
    totals=a['summary']['totals']
    text='# Frozen descriptive results\n\nVersion 2.0.0, 13 November 2026.\n\n'+markdown(['Corpus','Raw screened','Eligible records','RCT reports','Per 1,000','Wilson 95% interval'],[[c.upper(),totals[c]['raw_screened'],totals[c]['n'],totals[c]['rct'],f"{totals[c]['rate_per_1000']:.1f}",f"[{totals[c]['ci95'][0]:.1f}, {totals[c]['ci95'][1]:.1f}]"] for c in ['swrd','sswr']])
    text+='\n\n'+markdown(['Corpus','Group','Original reviewed IDs','Classifiable deduplicated records','RCT','Non-RCT'],[[r[k] for k in ['corpus','stratum','review_ids','classifiable_deduplicated','rct','non_rct']] for r in a['human_audit']])
    text+='\n\nThe original worklist contains 1,622 source IDs; 1,612 classifiable records remain. One additional journal author decision outside this worklist is SECONDARY and is not added to designed-sample performance denominators. Negative-sample NPV is limited to the targeted analyzed sample. No sampling-weighted RCT total or whole-pool sensitivity is inferred.\n'
    (out/'SUMMARY.md').write_text(text)
    counts=Counter(r['outcome'] for r in links)
    (out/'linkage.md').write_text('# Frozen linkage results\n\n'+markdown(['Outcome','Conference reports'],[[k,counts[k]] for k in ['SAME','RELATED_ONLY','INDETERMINATE','NOT_IDENTIFIED']])+'\n\nNine indeterminate identities are retained as a linkage outcome; missing matches do not establish non-publication.\n')
    print('Reproduced frozen screening, verification and linkage results.')
if __name__=='__main__':main()
