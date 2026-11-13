"""Recover original selected source IDs; do not redraw either sample."""
import json
from pathlib import Path
from study import read_jsonl
P=Path(__file__).resolve().parents[1]
def main():
    rs=read_jsonl(P/'data/record_level_results.jsonl.gz')
    selected=[dict(corpus=r['corpus'],record_id=r['record_id'],screening_group=r['screening_group'],sample_membership=r['sample_membership'],is_duplicate=r['is_duplicate'],insufficient_abstract=r['insufficient_abstract']) for r in rs if r['in_original_audit']]
    assert len(selected)==1622
    p=P/'results/original_review_worklist.json';p.write_text(json.dumps(selected,ensure_ascii=False,indent=2)+'\n')
    print('Recovered the original 1,622 source IDs; no sample redrawn.')
if __name__=='__main__':main()
