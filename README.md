# Social work RCT screening and verification, 1989–2026

Public study code, the operational codebook, final categorical reference coding and minimized record-level results for **What Social Work Publishes**.

**Method:** dual-model intersection/consensus triage → reference verification and adjudication → cleaned report-level analysis. Final reference decisions override model calls. Targeted negative audits evaluate the audited candidates; no sampling-weighted primary total or corpus-wide sensitivity is claimed.

## Reproduce

Python 3.9 or newer; no third-party package is required for the numerical analysis.

```bash
python3 scripts/reproduce.py
python3 scripts/export_review_worklist.py
python3 scripts/verify.py
```

|Corpus|Raw screened|Analysis denominator|Identified RCT reports|Per 1,000|
|---|---:|---:|---:|---:|
|Journals, 1989–2025|65,290|64,417|388|6.0|
|SSWR abstracts, 2005–2026|23,793|23,772|559|23.5|

The unit is a **report**, not a distinct trial. The original verification workbench contains 1,622 IDs; 1,617 are classifiable unique records after cleaning. Positive-set PPV is 375/385 (97.40%) for journals and 527/531 (99.25%) for conferences. Targeted-sample NPV is 285/287 (99.30%) and 284/288 (98.61%); its scope is the sampled candidate frames.

## Source data and citation

Bibliographic data and basic variables originate in the [Social Work Meta-Data Project](https://github.com/beperron/SocialWork-MetaData), which provides SWRD and SSWR Conference Database records. The study's screening extract has a different scope from the upstream 62,602-article scientific-research core. Source abstracts and author-level records are obtained from that project, not redistributed in this repository.

Perron, B. E., Victor, B. G., & Qi, Z. (2026a). AI-assisted curation of conference scholarship: Compiling, structuring, and analyzing two decades of presentations at the Society for Social Work and Research (2005–2026). *Journal of the Society for Social Work and Research*. Advance online publication. https://doi.org/10.1086/741324

Perron, B. E., Victor, B. G., & Qi, Z. (2026b). Evolution of social work knowledge production over 35 years: An AI-enabled analysis of trends in empiricism, methodology, collaboration, citation patterns, and output. *Research on Social Work Practice, 36*(8), 1576–1590. https://doi.org/10.1177/10497315261416833

## Files

- [Final method](docs/METHODS.md), [source attribution](docs/DATA_SOURCES.md), and [data dictionary](docs/DATA_DICTIONARY.md).
- [Final reference codebook](docs/CODEBOOK_v1.3.md) and [documented model prompt](docs/MODEL_PROMPT_v2.md).
- `data/`: final minimized screening records, reference coding, additional final exclusion and recorded linkage pairs.
- `config/study.json`: actual documented configuration, with unavailable information left null.
- `scripts/`: decision reconstruction, descriptive analysis, workbench recovery and checks.
- `results/` and `tables/`: reproducible JSON and Markdown results.
- `figures/`: the corresponding PNG/PDF figures.

## Linkage status

The retained, assisted pair assessments give 83 SAME, 68 RELATED_ONLY, 29 INDETERMINATE and 379 NOT_IDENTIFIED conference-report outcomes. They are not an independent human linkage gold standard. Unresolved identities remain visible; a not-identified result does not establish non-publication. Read the method before using these figures as publication outcomes.

## Public-release scope

This repository contains the current agreed method and final analysis materials. Historical exploratory analyses, draft decisions, superseded code, correspondence, manuscript drafts, full source abstracts and the local archive are excluded, including from this repository's initial history. The original model runner and sampling generator are not claimed to have been recovered.

No study-code license is assigned in this release. Upstream data and third-party materials retain their own terms. Citation information is in [CITATION.cff](CITATION.cff). No DOI is claimed for this code release.
