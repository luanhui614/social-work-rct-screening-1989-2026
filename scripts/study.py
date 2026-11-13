"""Retained category decisions and descriptive snapshot statistics; identity QC is external."""
import gzip
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

LABELS={'INDIVIDUAL','CLUSTER','QUASI','SECONDARY','PROTOCOL','REVIEW','OTHER'}
RCT={'INDIVIDUAL','CLUSTER'}
PERIODS={'swrd':[(1989,1999),(2000,2009),(2010,2019),(2020,2025)],
         'sswr':[(2005,2009),(2010,2014),(2015,2019),(2020,2026)]}

def read_jsonl(path):
    with (gzip.open(path, 'rt', encoding='utf-8') if str(path).endswith('.gz') else Path(path).open(encoding='utf-8')) as f:
        return [json.loads(line) for line in f if line.strip()]

def consensus(a,b):
    """Binary RCT agreement: allocation-level disagreement stays positive."""
    if a not in LABELS or b not in LABELS:raise ValueError('Unknown model label')
    return 'concordant_positive' if a in RCT and b in RCT else 'concordant_negative' if a not in RCT and b not in RCT else 'discordant'

def decision(row):
    """Apply final reference decisions; never relabel unreviewed negatives human."""
    if row['is_duplicate']:return 'excluded_duplicate',False
    if row['insufficient_abstract']:return 'excluded_insufficient_abstract',False
    label=row['final_reference_label']
    if label is not None:
        if label not in LABELS:raise ValueError('Unresolved/invalid final reference label')
        return ('reference_included',True) if label in RCT else ('reference_excluded',False)
    state=consensus(row['model_a_label'],row['model_b_label'])
    if state=='concordant_negative':return 'model_negative_not_reviewed',False
    # Positive consensus is first-pass triage, not permission to override review.
    raise ValueError('A positive or discordant record lacks final reference coding')

def wilson(k,n,scale=1000):
    if not n:return [None,None]
    z=1.959963984540054;p=k/n;d=1+z*z/n;c=(p+z*z/(2*n))/d
    h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return [(c-h)*scale,(c+h)*scale]

def describe(rows):
    n=len(rows);k=sum(decision(r)[1] for r in rows)
    return dict(n=n,rct=k,rate_per_1000=1000*k/n if n else None,ci95=wilson(k,n),
       individual=sum(r['final_reference_label']=='INDIVIDUAL' for r in rows),
       cluster=sum(r['final_reference_label']=='CLUSTER' for r in rows))

def analyze(rows):
    keys=[(r['corpus'],r['record_id']) for r in rows]
    if len(set(keys))!=len(keys):raise ValueError('Duplicate source IDs')
    clean=[r for r in rows if not r['is_duplicate'] and not r['insufficient_abstract']]
    totals={};annual=[];period=[];sources=[];audit=[];model_a=[]
    for c in ['swrd','sswr']:
        raw=[r for r in rows if r['corpus']==c];rs=[r for r in clean if r['corpus']==c]
        totals[c]=describe(rs);totals[c]['raw_screened']=len(raw)
        disagreements=sum(consensus(r['model_a_label'],r['model_b_label'])=='discordant' for r in rs)
        pa=sum(r['model_a_label'] in RCT for r in rs)/len(rs);pb=sum(r['model_b_label'] in RCT for r in rs)/len(rs)
        po=1-disagreements/len(rs);pe=pa*pb+(1-pa)*(1-pb)
        totals[c].update(binary_model_agreement=po,binary_model_kappa=(po-pe)/(1-pe),agreement_denominator='retained_source_records')
        ys=sorted({r['year'] for r in rs});yearly={y:describe([r for r in rs if r['year']==y]) for y in ys}
        for y in ys:
            annual.append(dict(corpus=c,year=y,**yearly[y],indexing_incomplete=c=='swrd' and y>=2024,
              centered_three_year_mean=sum(yearly[z]['rate_per_1000'] for z in [y-1,y,y+1])/3 if all(z in yearly for z in [y-1,y,y+1]) else None))
        for lo,hi in PERIODS[c]:
            z=describe([r for r in rs if lo<=r['year']<=hi]);period.append(dict(corpus=c,start=lo,end=hi,annual_mean_rcts=z['rct']/(hi-lo+1),**z))
        groups=defaultdict(list)
        for r in rs:groups[r['source_name_or_format']].append(r)
        sources.extend(dict(corpus=c,source=name,**describe(g)) for name,g in groups.items())
        for state in ['concordant_positive','discordant','concordant_negative']:
            reviewed=[r for r in raw if r['in_original_audit'] and r['screening_group']==state]
            valid=[r for r in reviewed if not r['is_duplicate'] and not r['insufficient_abstract']]
            k=sum(decision(r)[1] for r in valid);n=len(valid)
            audit.append(dict(corpus=c,stratum=state,review_ids=len(reviewed),classifiable_deduplicated=n,rct=k,non_rct=n-k,
              ppv=k/n if state=='concordant_positive' else None,sample_npv=(n-k)/n if state=='concordant_negative' else None))
        model_a.append(dict(corpus=c,counts=dict(Counter(r['model_a_label'] for r in raw))))
    journals=sorted([r for r in sources if r['corpus']=='swrd'],key=lambda r:(-r['rct'],r['source'].casefold()))
    cumulative=0
    for i,r in enumerate(journals,1):
        cumulative+=r['rct'];r.update(rank=i,cumulative_rcts=cumulative,cumulative_percent=100*cumulative/totals['swrd']['rct'],rct_share_percent=100*r['rct']/totals['swrd']['rct'])
    summary=dict(totals=totals,journal_count=len(journals),journals_with_rct=sum(r['rct']>0 for r in journals),
       journals_without_rct=sum(r['rct']==0 for r in journals),top2_rcts=sum(r['rct'] for r in journals[:2]),top15_rcts=sum(r['rct'] for r in journals[:15]),
       conference_to_journal_rate_ratio=totals['sswr']['rate_per_1000']/totals['swrd']['rate_per_1000'])
    return dict(summary=summary,annual=annual,period=period,journals=journals,
      conference_formats=[r for r in sources if r['corpus']=='sswr'],human_audit=audit,original_model_a_categories=model_a)

def aggregate_links(conferences,pairs):
    """Aggregate recorded assessments; candidate rank alone is not a decision."""
    by=defaultdict(list)
    for r in pairs:
        if r['relation'] not in {'SAME','RELATED','DIFFERENT','INDETERMINATE','NOT_ELIGIBLE_OUTCOME'}:raise ValueError('Unknown linkage relation')
        by[r['conference_record_id']].append(r)
    out=[]
    for c in conferences:
        ps=by[c['record_id']];same=[r for r in ps if r['relation']=='SAME'];related=[r for r in ps if r['relation']=='RELATED'];pending=[r for r in ps if r['relation']=='INDETERMINATE']
        outcome='SAME' if same else 'INDETERMINATE' if pending else 'RELATED_ONLY' if related else 'NOT_IDENTIFIED'
        first=min(same,key=lambda r:(r['journal_year'],r['journal_record_id'])) if same else None
        out.append(dict(conference_record_id=c['record_id'],conference_year=c['year'],outcome=outcome,
          same_journal_ids=[r['journal_record_id'] for r in same],related_journal_ids=[r['journal_record_id'] for r in related],
          unresolved_journal_ids=[r['journal_record_id'] for r in pending],
          first_identified_same_year=first['journal_year'] if first else None,
          first_identified_same_journal_id=first['journal_record_id'] if first else None,
          signed_lag=first['journal_year']-c['year'] if first else None))
    return out

def markdown(headers,rows):
    return '\n'.join(['|'+'|'.join(headers)+'|','|'+'|'.join('---' for _ in headers)+'|']+['|'+'|'.join(str(x).replace('|',' / ') for x in r)+'|' for r in rows])
