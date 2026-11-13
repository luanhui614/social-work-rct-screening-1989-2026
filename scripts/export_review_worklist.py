#!/usr/bin/env python3
"""Recover historical source-record memberships without drawing a new sample."""
import json
from pathlib import Path
from study import read_jsonl
ROOT=Path(__file__).resolve().parents[1]

def main():
    rows=read_jsonl(ROOT/'data/record_level_results.jsonl')
    work=[{k:r[k] for k in ['corpus','record_id','screening_group','sample_membership','final_reference_label']} for r in rows if r['in_original_audit']]
    if len(work)!=1622:raise ValueError('Historical workbench membership does not match the source metadata.')
    out=ROOT/'.provisional_results';out.mkdir(exist_ok=True)
    (out/'original_review_worklist.json').write_text(json.dumps(dict(status='historical_source_record_membership_not_a_unique_publication_list',records=work),ensure_ascii=False,indent=2)+'\n')
    print('Recovered 1,622 original source IDs; no sample redrawn and no publication identity inferred.')
if __name__=='__main__':main()
