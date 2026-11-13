#!/usr/bin/env python3
"""Reproduce a retained snapshot without certifying publication identity."""
import argparse
import json
from pathlib import Path
from study import analyze,aggregate_links,decision,markdown,read_jsonl
from check_release_status import blockers
ROOT=Path(__file__).resolve().parents[1]

def save(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--allow-provisional',action='store_true',help='Explicitly reproduce the retained snapshot despite open identity issues.')
    args=p.parse_args();reasons=blockers()
    if reasons and not args.allow_provisional:
        print('Final results are unavailable. Use --allow-provisional only to inspect the retained snapshot.')
        return 2
    rows=read_jsonl(ROOT/'data/record_level_results.jsonl');out=ROOT/'.provisional_results';out.mkdir(exist_ok=True)
    a=analyze(rows)
    for name,obj in a.items():save(out/(name+'.json'),obj)
    conferences=[r for r in rows if r['corpus']=='sswr' and not r['is_duplicate'] and decision(r)[1]]
    links=aggregate_links(conferences,read_jsonl(ROOT/'data/linkage_pair_assessments.jsonl'))
    save(out/'linkage_record_outcomes.json',links)
    save(out/'analysis_status.json',dict(analysis_status='provisional_snapshot_not_final',open_release_blockers=reasons))
    totals=a['summary']['totals'];banner='PROVISIONAL SNAPSHOT — publication-identity reconciliation is incomplete; do not cite as final manuscript results.'
    text='# Provisional descriptive snapshot\n\n'+banner+'\n\n'+markdown(['Corpus','Raw screened','Retained source records','RCT-labeled records','Per 1,000','Wilson 95% interval'],[[c.upper(),totals[c]['raw_screened'],totals[c]['n'],totals[c]['rct'],f"{totals[c]['rate_per_1000']:.1f}",f"[{totals[c]['ci95'][0]:.1f}, {totals[c]['ci95'][1]:.1f}]"] for c in ['swrd','sswr']])
    text+='\n\nSource-ID uniqueness is not publication-entity uniqueness. These counts reproduce retained labels and existing exclusions only. No weighted correction or whole-negative-pool sensitivity is estimated.\n\n'
    text+=markdown(['Corpus','Group','Original reviewed IDs','Retained source records','RCT','Non-RCT'],[[r[k] for k in ['corpus','stratum','review_ids','classifiable_deduplicated','rct','non_rct']] for r in a['human_audit']])+'\n'
    (out/'SUMMARY.md').write_text(text)
    counts={k:sum(r['outcome']==k for r in links) for k in ['SAME','RELATED_ONLY','INDETERMINATE','NOT_IDENTIFIED']}
    (out/'linkage.md').write_text('# Provisional linkage snapshot\n\n'+banner+'\n\n'+markdown(['Outcome','Conference source reports'],list(counts.items()))+'\n\nThe search is limited to social work journals; a missing match does not establish non-publication.\n')
    print('Reproduced the retained PROVISIONAL snapshot in .provisional_results/. Final-release status remains blocked.' if reasons else 'Snapshot regenerated.')
    return 0
if __name__=='__main__':raise SystemExit(main())
