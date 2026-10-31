#!/usr/bin/env python3
"""Reproduce final descriptive outputs using Python's standard library."""
import json
from pathlib import Path
from study import analyze,aggregate_links,decision,markdown,read_jsonl

ROOT=Path(__file__).resolve().parents[1]
def save(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def main():
    rows=read_jsonl(ROOT/'data/record_level_results.jsonl');out=ROOT/'results';out.mkdir(exist_ok=True)
    analyses=analyze(rows)
    for name,obj in analyses.items():save(out/(name+'.json'),obj)
    conferences=[r for r in rows if r['corpus']=='sswr' and not r['is_duplicate'] and decision(r)[1]]
    pairs=read_jsonl(ROOT/'data/linkage_pair_assessments.jsonl');links=aggregate_links(conferences,pairs)
    save(out/'linkage_record_outcomes.json',links)
    summary=analyses['summary'];totals=summary['totals']
    text='# Final descriptive results\n\n'+markdown(['Corpus','Raw screened','Eligible records','Identified RCT reports','Per 1,000','Wilson 95% interval'],[
      [c.upper(),totals[c]['raw_screened'],totals[c]['n'],totals[c]['rct'],f"{totals[c]['rate_per_1000']:.1f}",f"{totals[c]['ci95'][0]:.1f}–{totals[c]['ci95'][1]:.1f}"] for c in ['swrd','sswr']])
    text+='\n\nThe unit is a report, not a distinct trial. These are observed identified counts; targeted-negative audits do not estimate sensitivity of the entire negative pool.\n\n'
    text+='## Verification by screening stratum\n\n'+markdown(['Corpus','Stratum','Reviewed IDs','Classifiable unique records','RCT','Non-RCT'],[[r[k] for k in ['corpus','stratum','review_ids','classifiable_deduplicated','rct','non_rct']] for r in analyses['human_audit']])
    text+='\n\nThe original workbench comprises 1,622 IDs. Additional purpose-specific reference coding is stored separately and is not added to negative-sample denominators.\n'
    (out/'SUMMARY.md').write_text(text)
    for name,headers,keys in [
      ('annual',['Corpus','Year','Eligible records','RCT reports','Per 1,000'],['corpus','year','n','rct','rate_per_1000']),
      ('period',['Corpus','Start','End','Eligible records','RCT reports','Per 1,000'],['corpus','start','end','n','rct','rate_per_1000']),
      ('journals',['Rank','Journal','Eligible records','RCT reports','Per 1,000'],['rank','source','n','rct','rate_per_1000']),
      ('conference_formats',['Format','Eligible abstracts','RCT reports','Per 1,000'],['source','n','rct','rate_per_1000'])]:
        (out/(name+'.md')).write_text('# '+name.replace('_',' ').title()+'\n\n'+markdown(headers,[[f'{r[k]:.2f}' if k=='rate_per_1000' else r[k] for k in keys] for r in analyses[name]])+'\n')
    counts={k:sum(r['outcome']==k for r in links) for k in ['SAME','RELATED_ONLY','INDETERMINATE','NOT_IDENTIFIED']}
    (out/'linkage.md').write_text('# Abstract-based linkage\n\n'+markdown(['Outcome','Conference reports'],list(counts.items()))+'\n\nThese recorded, assisted assessments retain indeterminate identities and require author verification. Not identified does not mean unpublished; the search covers the 88-journal collection only.\n')
    print(f"Reproduced {totals['swrd']['rct']} journal and {totals['sswr']['rct']} conference RCT reports.")
if __name__=='__main__':main()
