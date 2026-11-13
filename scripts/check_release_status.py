from pathlib import Path
import json
P=Path(__file__).resolve().parents[1]
def blockers():
 s=json.loads((P/'RELEASE_STATUS.json').read_text())
 return [] if s['analysis_status']=='frozen' and s['final_results_available'] else ['Analysis is not frozen']
if __name__=='__main__':
 errors=blockers()
 if errors:raise SystemExit('; '.join(errors))
 print('Frozen statistical release status verified.')
