"""Export fixed verification membership and final cleaning fields."""
import json
from pathlib import Path
from study import read_jsonl
P=Path(__file__).resolve().parents[1]
def main():
    rs=read_jsonl(P/'data/record_level_results.jsonl.gz')
    selected=[dict(corpus=r['corpus'],record_id=r['record_id'],screening_group=r['screening_group'],sample_membership=r['sample_membership'],is_duplicate=r['is_duplicate'],insufficient_abstract=r['insufficient_abstract']) for r in rs if r['in_original_audit']]
    assert len(selected)==1622
    p=P/'results/verification_membership.json';p.write_text(json.dumps(selected,ensure_ascii=False,indent=2)+'\n')
    print('Exported verification membership for 1,622 selected source IDs.')
if __name__=='__main__':main()
