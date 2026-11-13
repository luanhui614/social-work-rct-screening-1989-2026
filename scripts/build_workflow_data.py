"""Derive the analytical workflow figure from the unchanged frozen counts."""
from pathlib import Path
import json

P=Path(__file__).resolve().parents[1]

def main():
    flow=json.loads((P/'data/flow_counts.json').read_text())
    for c in flow.values():
        assert c['raw_records']-c['total_duplicate_records']-c['insufficient_abstract_records']==c['clean_eligible_records']
        assert sum(c['clean_model_groups'].values())==c['clean_eligible_records']
        assert sum(x['rct'] for x in c['verification_by_group'])==c['final_rct_reports']
        neg=next(x for x in c['verification_by_group'] if x['stratum']=='concordant_negative')
        assert neg['classifiable_deduplicated']+c['additional_author_coded_records_outside_original_workbench']+c['unreviewed_concordant_negatives']==c['clean_model_groups']['concordant_negative']
    out=dict(figure='S1',title='Data preparation, screening and human verification',scope='Final analytical dataset construction; retained model outputs are joined to cleaned records.',journal=flow['swrd'],conference=flow['sswr'],clean_verification_n=sum(c['unique_classifiable_verification_records'] for c in flow.values()),original_worklist_n=sum(c['original_verification_source_ids'] for c in flow.values()),additional_author_review_note='One additional journal record was classified SECONDARY outside the designed verification sample; it is excluded and does not enter sample performance denominators.')
    path=P/'figures/source_data/Figure_S1.json'
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('PASS: workflow counts derived from the frozen data, with all branches reconciled.')

if __name__=='__main__':main()
