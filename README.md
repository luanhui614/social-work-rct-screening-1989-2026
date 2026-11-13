# Social work RCT screening and human verification, 1989–2026

Frozen research materials for **What Social Work Publishes**, version **2.0.0**, 13 November 2026. The repository provides the screening codebook, documented model prompt and settings, screening and linkage analysis code, final reference classifications, bibliographic cleaning decisions and minimized record-level results. Source abstracts and full-text PDFs are not redistributed.

## Final count chain

|Stage|Journal records|Conference abstracts|
|---|---:|---:|
|Original screened source records|65,290|23,793|
|Source-designated duplicate indices removed|872|21|
|Additional corroborated duplicate indices removed|614|0|
|Insufficient abstract excluded|1|0|
|Clean analysis denominator|63,803|23,772|
|Final identified RCT reports|384|559|

Journal RCTs comprise 351 INDIVIDUAL and 33 CLUSTER reports; conference RCTs comprise 474 and 85. These are report counts. The complete [count chain](docs/COUNT_FLOW.md) distinguishes source-ID workload, cleaned verification denominators and final eligibility. [Freeze status](data/freeze_status.json) and [cleaning decisions](docs/DATA_QUALITY_STATUS.md) document the final analysis version. Earlier tagged releases are superseded historical snapshots.

## Screening and verification

Two language models separately classified titles and abstracts under the same eligibility criteria. Records both models classified as RCTs and those classified as RCTs by only one model underwent verification. Targeted samples of records both models classified as non-RCTs were also reviewed. Final human decisions govern reviewed eligibility. Unreviewed concordant-negative records remain excluded.

The original verification worklist contained 1,622 source IDs. Removing nine duplicate journal indices and one insufficient abstract left 1,612 classifiable records: 738 journal records and 874 conference abstracts. One additional author-adjudicated journal article outside this worklist is SECONDARY; it does not enter designed-sample performance denominators. Targeted negative samples do not establish whole-pool sensitivity or NPV. No sampling-weighted primary total is inferred.

## Materials

- [Codebook](docs/CODEBOOK.md), [methods](docs/METHODS.md), [reference decisions](docs/REFERENCE_REVIEW_PROTOCOL.md).
- [Verbatim v2 prompt](docs/MODEL_PROMPT_v2.md), [documented execution](docs/MODEL_EXECUTION.md), [negative sampling](docs/NEGATIVE_AUDIT.md).
- [Data dictionary](docs/DATA_DICTIONARY.md), [data sources](docs/DATA_SOURCES.md), [materials index](docs/RESEARCH_MATERIALS.md).
- [Record-level data](data/README.md), [statistical results](results/SUMMARY.md), [tables](tables/README.md), [figures](figures/README.md).

## Reproduce

Python 3.9 or newer; the numerical analysis uses the standard library.

```bash
python3 scripts/verify.py --snapshot
python3 scripts/reproduce.py
python3 scripts/export_review_worklist.py
python3 scripts/verify.py --generated
```

Compressed JSONL files are read directly by the scripts. Integrity checks compare source counts, cleaning flags, source-to-analysis mappings, author decisions, screening-group totals, human verification denominators, yearly and journal distributions, linkage aggregation and file hashes. Reproduction uses retained model classifications; the original inference runner and sampling generator were not recovered. Recorded settings are not substituted for missing execution logs.

## Attribution and rights

Bibliographic source data and basic variables originate in the [Social Work Meta-Data Project](https://github.com/beperron/SocialWork-MetaData). Cite the study manuscript and source database publications listed in [Data sources](docs/DATA_SOURCES.md). Do not substitute the upstream scientific-research core for this study's screening extract.

Third-party materials retain their own terms. No study-code license or repository DOI has been assigned. Unpublished manuscript files, full abstracts, PDFs, personal reviewer returns and internal correspondence are not included.
