# Social work RCT screening and human verification, 1989–2026

Research materials accompanying **What Social Work Publishes**. This manuscript-aligned release contains the final codebook, model prompt and settings, reference classifications, bibliographic cleaning records, analysis code, numerical results and manuscript tables and figures.

**Fixed version: [v2.1.0](https://github.com/luanhui614/social-work-rct-screening-1989-2026/releases/tag/v2.1.0), 15 November 2026.** Analytical data are frozen as `screening-human-adjudication-final-2026-11-13-v6`.

## Study workflow

Source collections → bibliographic cleaning → dual-model screening groups → human verification and adjudication → final RCT reports → descriptive and conference–journal linkage analyses.

|Stage|Journal records|Conference records|
|---|---:|---:|
|Source records|65,290|23,793|
|Duplicate indices excluded|1,486|21|
|Insufficient abstract information excluded|1|0|
|Eligible records|63,803|23,772|
|Human verification set|738|874|
|Final RCT reports|384|559|

All records both models classified as RCTs and all trial/non-trial disagreements underwent human review. Targeted samples of records both models classified as non-RCTs were also reviewed. Final human classifications determined reviewed eligibility; unreviewed concordant negatives remained excluded. [Methods](docs/METHODS.md) and the [count flow](docs/COUNT_FLOW.md) define each analysis group and denominator.

## Materials

- **Methods and criteria:** [study methods](docs/METHODS.md), [codebook](docs/CODEBOOK.md), [negative-sample selection](docs/NEGATIVE_AUDIT.md), [bibliographic cleaning](docs/DATA_QUALITY_STATUS.md).
- **Model materials:** [verbatim prompt](docs/MODEL_PROMPT_v2.md), [settings](docs/MODEL_EXECUTION.md), [machine-readable configuration](config/study.json).
- **Data:** [file inventory](data/README.md), [dictionary](docs/DATA_DICTIONARY.md), [source attribution](docs/DATA_SOURCES.md).
- **Outputs:** [summary](results/SUMMARY.md), [linkage](results/linkage.md), [manuscript tables](tables/README.md), [manuscript figures](figures/README.md).

## Reproduce the numerical results

Python 3.9 or later; numerical reproduction uses the standard library. The scripts read the retained model classifications and final reference classifications included in this release.

```bash
python3 scripts/verify.py --snapshot
python3 scripts/reproduce.py
python3 scripts/export_review_worklist.py
python3 scripts/verify.py --generated
```

Checks cover source-to-analysis mappings, cleaning exclusions, screening groups, final reference classifications, subgroup totals, linkage aggregation, figure data and file hashes. Numerical outputs are regenerated from the released records. Figure exports are supplied as PNG, PDF and editable SVG, with their numerical source data.

## Sources and citation

Bibliographic data and basic variables originate in the [Social Work Meta-Data Project](https://github.com/beperron/SocialWork-MetaData). Source publications are listed in [Data sources](docs/DATA_SOURCES.md). Cite the study manuscript and this fixed release when using these research materials; [CITATION.cff](CITATION.cff) records the version-specific URL.
