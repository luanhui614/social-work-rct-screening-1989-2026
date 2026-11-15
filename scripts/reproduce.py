"""Reproduce manuscript statistics, tables and figure data from frozen records."""
import json
import statistics
from collections import Counter
from pathlib import Path
from study import analyze, aggregate_links, decision, markdown, read_jsonl
from check_release_status import blockers

ROOT = Path(__file__).resolve().parents[1]


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def linkage_summary(links, pairs):
    subsets = {}
    for name, records in [('all', links), ('through_2021', [r for r in links if r['conference_year'] <= 2021])]:
        same = [r for r in records if r['same_journal_ids']]
        subsets[name] = dict(n=len(records), confirmed_same_trial=len(same),
                             no_confirmed_same_trial=len(records)-len(same),
                             percent_confirmed=100*len(same)/len(records))
    lags = [r['signed_lag'] for r in links if r['same_journal_ids']]
    return dict(subsets=subsets,
                assessed_pairs=len(pairs),
                same_trial_pairs=sum(p['relation']=='SAME' for p in pairs),
                distinct_same_trial_articles=len({p['journal_record_id'] for p in pairs if p['relation']=='SAME'}),
                signed_lags={str(k):v for k,v in sorted(Counter(lags).items())},
                median_signed_lag=statistics.median(lags),
                before=sum(x<0 for x in lags), same_year=sum(x==0 for x in lags),
                after=sum(x>0 for x in lags), absolute_lag_le_2=sum(abs(x)<=2 for x in lags))


def export_tables(analysis, items):
    tables = ROOT/'tables'
    totals = analysis['summary']['totals']
    calls = {x['corpus']:x['counts'] for x in analysis['original_model_a_categories']}
    rows = []
    for label, category in zip(items['category_labels'], items['category_rows']):
        row = [category['name'], category['definition']]
        for corpus in ['swrd','sswr']:
            n=calls[corpus].get(label,0)
            row.append(f"{n:,} ({100*n/totals[corpus]['raw_screened']:.1f})")
        rows.append(row)
    rows.append(['Total screened','', '65,290 (100)', '23,793 (100)'])
    table_rows = {'1':rows}
    rows=[]
    group_names = ['Both models classified as trial', 'One model classified as trial',
                   'Both models classified as non-trial (sample)']
    for corpus, title in [('swrd','Social work journals'),('sswr','SSWR conference')]:
        audits=[a for a in analysis['human_audit'] if a['corpus']==corpus]
        rows.append([f"{title} (n = {sum(a['classifiable_deduplicated'] for a in audits)})",'','','',''])
        for title, a in zip(group_names,audits):
            n=a['classifiable_deduplicated'];k=a['rct']
            if a['stratum']=='concordant_positive': metric=f'PPV: {100*k/n:.1f}%'
            elif a['stratum']=='discordant': metric=f'RCT yield: {100*k/n:.1f}%'
            else: metric=f'Sample NPV: {100*(n-k)/n:.1f}%'
            rows.append([title,n,k,n-k,metric])
    table_rows['2']=rows
    rows=[]
    for corpus,title in [('swrd','Social work journals'),('sswr','SSWR conference')]:
        rows.append([title,'','','',''])
        records=[(f"{p['start']}–{p['end']}",p) for p in analysis['period'] if p['corpus']==corpus]
        records.append(('All years', totals[corpus]))
        for name,p in records:
            rows.append([name,f"{p['n']:,}",f"{p['rct']:,}",f"{p['rate_per_1000']:.1f}",
                         f"[{p['ci95'][0]:.1f}, {p['ci95'][1]:.1f}]"])
    table_rows['3']=rows
    for number, rows in table_rows.items():
        key='Table '+number
        (tables/f'Table_{number}.md').write_text(
            f"# {key}\n\n{items[key]['title']}\n\n"+
            markdown(items['table_headers'][number],rows)+'\n\n'+items[key]['note']+'\n')


def main():
    assert not blockers()
    config=json.loads((ROOT/'config/study.json').read_text())
    items=json.loads((ROOT/'config/manuscript_items.json').read_text())
    records=read_jsonl(ROOT/'data/record_level_results.jsonl.gz')
    analysis=analyze(records)
    out=ROOT/'results'
    for name,value in analysis.items():save(out/(name+'.json'),value)
    conferences=[r for r in records if r['corpus']=='sswr' and decision(r)[1]]
    pairs=read_jsonl(ROOT/'data/linkage_pair_assessments.jsonl')
    links=aggregate_links(conferences,pairs)
    save(out/'linkage_record_outcomes.json',links)
    primary=[dict(conference_record_id=r['conference_record_id'],conference_year=r['conference_year'],
                  confirmed_same_trial=bool(r['same_journal_ids']),
                  same_journal_ids=r['same_journal_ids'],signed_lag=r['signed_lag']) for r in links]
    save(out/'linkage_primary_outcomes.json',primary)
    linkage=linkage_summary(links,pairs)
    save(out/'linkage_summary.json',linkage)
    figure=ROOT/'figures/source_data'
    save(figure/'Figure_1.json',json.loads((ROOT/'data/flow_counts.json').read_text()))
    save(figure/'Figure_2.json',analysis['journals'])
    save(figure/'Figure_3.json',analysis['annual'])
    save(figure/'Figure_4.json',linkage)
    export_tables(analysis,items)
    totals=analysis['summary']['totals']
    text=f"# Descriptive results\n\nRelease {config['study_version']}, {config['release_date']}.\n\n"
    text+=markdown(['Corpus','Source records','Eligible records','RCT reports','Per 1,000','Wilson 95% interval'],
        [[c.upper(),f"{totals[c]['raw_screened']:,}",f"{totals[c]['n']:,}",totals[c]['rct'],
          f"{totals[c]['rate_per_1000']:.1f}",f"[{totals[c]['ci95'][0]:.1f}, {totals[c]['ci95'][1]:.1f}]"] for c in ['swrd','sswr']])
    text+='\n\n'+markdown(['Corpus','Screening group','Reviewed','RCT','Non-RCT'],
        [[a[k] for k in ['corpus','stratum','classifiable_deduplicated','rct','non_rct']] for a in analysis['human_audit']])
    text+='\n\nThe verification analysis includes 738 journal records and 874 conference records. Sample NPV refers to the targeted concordant-negative samples.\n'
    (out/'SUMMARY.md').write_text(text)
    (out/'linkage.md').write_text('# Conference–journal linkage\n\n'+markdown(
        ['Conference subset','Reports','Confirmed same-trial outcome article','Without a confirmed same-trial outcome article'],
        [[label,d['n'],d['confirmed_same_trial'],d['no_confirmed_same_trial']] for label,d in
         [('2005–2026',linkage['subsets']['all']),('2005–2021',linkage['subsets']['through_2021'])]])+
        '\n\nThe 115 SAME pairs involve 90 conference reports and 73 distinct journal articles. For linked reports, median article year minus conference year is 0; 24 articles precede the conference report, 28 are in the same year and 38 follow it.\n')
    print('Reproduced final statistics, three manuscript tables and four figure datasets.')


if __name__=='__main__':
    main()
