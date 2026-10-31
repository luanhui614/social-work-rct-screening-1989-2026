#!/usr/bin/env python3
"""Recover the actual original workbench memberships, without new sampling."""
import json
from pathlib import Path
from study import read_jsonl
ROOT=Path(__file__).resolve().parents[1]
def main():
    rows=read_jsonl(ROOT/'data/record_level_results.jsonl')
    work=[dict(corpus=r['corpus'],record_id=r['record_id'],screening_group=r['screening_group'],sample_membership=r['sample_membership'],final_reference_label=r['final_reference_label']) for r in rows if r['in_original_audit']]
    assert len(work)==1622
    path=ROOT/'results/original_review_worklist.json'
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(work,ensure_ascii=False,indent=2)+'\n')
    print('Recovered 1,622 original audit IDs; no random sample regenerated.')
if __name__=='__main__':main()
