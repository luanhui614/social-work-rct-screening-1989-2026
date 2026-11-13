#!/usr/bin/env python3
"""Keep computational reproduction separate from a final statistical release."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def blockers(root=ROOT):
    status=json.loads((root/'RELEASE_STATUS.json').read_text())
    cases=json.loads((root/status['known_issues_file']).read_text())['cases']
    reasons=[]
    if not status.get('final_results_available'):reasons.append('Final statistical results have not been cleared for release.')
    if status.get('analysis_status')!='final_identity_reconciled':reasons.append('Bibliographic identity reconciliation is incomplete.')
    unresolved=[c['case_id'] for c in cases if not c['status'].startswith('resolved_')]
    if unresolved:reasons.append('Open identity/label cases: '+', '.join(unresolved))
    return reasons

def main():
    reasons=blockers()
    if reasons:
        print('FINAL STATISTICAL RELEASE BLOCKED')
        for reason in reasons:print('- '+reason)
        return 2
    print('Final statistical release status cleared.')
    return 0
if __name__=='__main__':raise SystemExit(main())
