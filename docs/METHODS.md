# Study methods

The [analytical workflow](WORKFLOW.md) and [Figure S1](../figures/Figure_S1.pdf) summarize data preparation, model-result grouping, human verification, final eligibility and analysis. This describes the construction of the final analytical datasets; original model calls and source IDs remain traceable.

## 1. Design, scope and eligibility criteria

This abstract-based scientometric study analyzes the journal and conference collections separately. Model screening and human coding use the same substantive eligibility criteria and category labels. Brian's five RCT inclusion criteria and seven categories are retained in the [codebook](CODEBOOK.md). INDIVIDUAL and CLUSTER are the eligible RCT classes. The four manuscript research questions remain the basis of analysis.

## 2. Source collections

The screening extracts contain 65,290 journal records from 88 social work journals (1989–2025) and 23,793 SSWR conference abstracts (2005–2026). Source variables and extract fingerprints are documented in [Data sources](DATA_SOURCES.md). Journal indexing for 2024–2025 is incomplete.

## 3. Data cleaning and analysis denominators

Source-flag and corroborated bibliographic deduplication excludes 1,486 journal indices and 21 conference indices. Exclusion of one insufficient journal abstract leaves 63,803 eligible journal records and 23,772 conference abstracts. Distinct publication occurrences and unsupported duplicate candidates are retained. Source-to-analysis mappings, exclusion reasons and bibliographic field corrections are preserved. Non-RCT classifications remain in the all-record denominators.

## 4. Dual-model screening results and grouping

Two locally hosted language models each classified source titles and abstracts into one of seven categories using the written eligibility criteria. The classifications are retained and joined to the clean records. Both models making an RCT call defines concordant positivity, including disagreement only about individual versus cluster randomization. Exactly one RCT call defines a trial/non-trial disagreement; neither model making an RCT call defines concordant negativity. Separate classifications are not assumed to have statistically independent errors. Exact documented prompt text and settings are linked in [Model execution](MODEL_EXECUTION.md).

## 5. Human verification and final reference decisions


Records both models classified as RCTs underwent human verification. Records classified as RCTs by only one model also underwent review. Within records both models classified as non-RCTs, samples were selected from two overlapping candidate pools defined by trial-label scores and allocation-related keywords. Selected records appearing through both pools were reviewed once. Coding used the same substantive eligibility criteria and category labels; disputed cases were resolved by author adjudication.

Coding was organized by collection; disputed cases were resolved by author adjudication. Independent double-human coding of every record is not claimed. Final human classifications provide the reference for screening-performance evaluation. Reviewed eligible records are included and reviewed false positives excluded. Unreviewed records both models classified as non-RCTs remain excluded.

The original verification workbench contains 1,622 source IDs. Cleaning removes nine duplicate journal source IDs and one insufficient abstract, leaving 1,612 classifiable records (738 journal and 874 conference records). An additional author-adjudicated journal article outside the workbench is SECONDARY; it is not added to designed-sample performance denominators. Final author decisions and identity consolidation are documented in [quality status](DATA_QUALITY_STATUS.md) and the [count chain](COUNT_FLOW.md).

## 6. Screening-performance evaluation


For records both models classified as RCTs, PPV is the proportion confirmed as RCTs by human verification. For model disagreements, report the number and proportion confirmed as RCTs. For sampled records both models classified as non-RCTs, sample NPV is the proportion confirmed as non-RCTs within the analyzed sample. These targeted samples do not estimate sensitivity or NPV for the entire negative pool. No sampling-weighted primary RCT total is inferred. Agreement between the two models is evaluated separately from agreement with final reference coding.

## 7. Descriptive analysis and frozen version


Descriptive results use RCT reports per 1,000 eligible records, with 95% Wilson score intervals, annual and period summaries, journal distributions and conference formats. Source flags and corroborated bibliographic identities determine exclusions; all original IDs and model calls remain traceable. Different publication occurrences and unsupported duplicate candidates are retained under the documented cleaning rules. The frozen journal total is 384/63,803 and the conference total is 559/23,772. Wilson intervals describe identified-report proportions, not screening-error uncertainty. Numerical results are reproducible from the frozen records and reference classifications.

## 8. Conference–journal record linkage


The 559 conference reports classified as eligible in the frozen data are compared with all 63,803 eligible journal records, irrespective of journal model classifications. Title and abstract terms and author names identify and assess candidate pairs. Selected full texts and project materials were consulted for unresolved identity checks. This concerns trial identity in linkage, not a change from abstract-based screening eligibility to full-text screening.

Pairs distinguish same-trial outcome articles, related papers, different studies and indeterminate identity. The released assessment file also retains NOT_ELIGIBLE_OUTCOME when an article is not an eligible outcome report. A conference report is summarized as SAME if any pair is SAME; otherwise INDETERMINATE if identity remains unresolved; otherwise RELATED_ONLY if a related paper is identified; otherwise NOT_IDENTIFIED. SAME and RELATED_ONLY remain separate outcomes. A not-identified match does not establish non-publication, because the search covers social work journals only.

One conference report may link to several articles, and the same trial may have multiple conference reports. The time interval is article year minus conference year, using the earliest identified same-trial article. Negative values indicate an article preceding the conference. Neither record IDs nor multiple presentations are silently treated as distinct trials. Current pair decisions incorporate recorded author adjudications but are not represented as an independently double-human-coded linkage gold standard.

