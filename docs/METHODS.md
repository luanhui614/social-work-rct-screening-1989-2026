# Study methods

## Collections and screening

The screening extracts contain 65,290 journal records from 88 social work journals (1989–2025) and 23,793 SSWR conference abstracts (2005–2026). These are raw screened counts, not final cleaned denominators. The collections are analyzed separately. Journal indexing for 2024–2025 is incomplete.

Two locally hosted language models each classified every title and abstract into one of seven categories using the written eligibility criteria. INDIVIDUAL and CLUSTER are RCT calls. The intersection rule identifies records for which both models make an RCT call, even if they differ on individual versus cluster randomization. Separate model classifications are not assumed to have statistically independent errors. Exact documented prompt text and settings are linked in [Model execution](MODEL_EXECUTION.md).

## Human verification and final reference decisions

Records both models classified as RCTs underwent human verification. Records classified as RCTs by only one model also underwent review. Within records both models classified as non-RCTs, samples were selected from two overlapping candidate pools defined by trial-label scores and allocation-related keywords. Selected records appearing through both pools were reviewed once. Coding used the same substantive eligibility criteria and category labels; disputed cases were resolved by author adjudication.

Coding was organized by collection, with replacement coverage for unfinished work. Multiple coder files provide provenance; they do not establish independent double-human coding of every record. The current evaluation uses final accepted human classifications, rather than the earlier enriched reference-set performance estimates. Reviewed eligible records are included and reviewed false positives excluded. Unreviewed records both models classified as non-RCTs remain excluded.

The historical verification workbench contains 1,622 source IDs. Counts of unique, classifiable publications require completed identity reconciliation; see [quality status](DATA_QUALITY_STATUS.md). Latest author-accepted categories are preserved rather than silently replaced when an identity or classification conflict is discovered.

## Screening performance

For records both models classified as RCTs, PPV is the proportion confirmed as RCTs by human verification. For model disagreements, report the number and proportion confirmed as RCTs. For sampled records both models classified as non-RCTs, sample NPV is the proportion confirmed as non-RCTs within the analyzed sample. These targeted samples do not estimate sensitivity or NPV for the entire negative pool. No sampling-weighted primary RCT total is inferred. Agreement between the two models is evaluated separately from agreement with final reference coding.

## Record linkage

Conference reports classified as eligible in the retained snapshot are compared with the full journal collection, irrespective of journal model classifications. Title and abstract terms and author names identify and assess candidate pairs. Selected full texts and project materials were consulted for unresolved identity checks. This concerns trial identity in linkage, not a change from abstract-based screening eligibility to full-text screening.

Pairs distinguish same-trial outcome articles, related papers, different studies and indeterminate identity. The released assessment file also retains NOT_ELIGIBLE_OUTCOME when an article is not an eligible outcome report. A conference report is summarized as SAME if any pair is SAME; otherwise INDETERMINATE if identity remains unresolved; otherwise RELATED_ONLY if a related paper is identified; otherwise NOT_IDENTIFIED. SAME and RELATED_ONLY remain separate outcomes. A not-identified match does not establish non-publication, because the search covers social work journals only.

One conference report may link to several articles, and the same trial may have multiple conference reports. The time interval is article year minus conference year, using the earliest identified same-trial article. Negative values indicate an article preceding the conference. Neither record IDs nor multiple presentations are silently treated as distinct trials. Current pair decisions incorporate recorded author adjudications but are not represented as an independently double-human-coded linkage gold standard.

## Analysis and release status

Descriptive results use RCT reports per 1,000 eligible records, with 95% Wilson score intervals, annual and period summaries, journal distributions and conference formats. Source IDs are preserved for provenance. The current raw duplicate-index flags are insufficient to establish unique publications; further bibliographic identity checks are open. The code can reproduce the preserved snapshot only with an explicit provisional flag, and final statistical release is blocked until those checks and any required author decisions are complete.
