# Social work RCT screening and human verification, 1989–2026

Research materials for **What Social Work Publishes**: the screening criteria, documented dual-model prompt and configuration, reference coding, screening and linkage code, and minimized record-level snapshots.

**Status — 13 November 2026:** final statistical outputs are withheld pending bibliographic deduplication and reconciliation of a small number of record-level label conflicts. The retained category labels are an auditable author-accepted snapshot, not a claim that every source ID is a unique publication. See [release status](RELEASE_STATUS.json) and the [identity quality review](docs/DATA_QUALITY_STATUS.md). Earlier releases are historical snapshots, not the final manuscript dataset.

## Study workflow

Two language models classified each title and abstract separately under the same written eligibility criteria. Records both models classified as RCTs and records classified as RCTs by only one model underwent human verification. Targeted samples of records both models classified as non-RCTs were also verified. Final human decisions determine reviewed eligibility; unreviewed records both models classified as non-RCTs remain excluded. Performance is evaluated against the final human classifications, separately by screening group. Targeted negative samples do not establish sensitivity or negative predictive value for the entire negative pool, and no sampling-weighted primary count is reported.

## Research materials

- [Methods](docs/METHODS.md) and [screening codebook](docs/CODEBOOK.md).
- [Exact documented model prompt](docs/MODEL_PROMPT_v2.md), [model configuration and run summaries](docs/MODEL_EXECUTION.md).
- [Human verification and adjudication](docs/REFERENCE_REVIEW_PROTOCOL.md), [sampling records both models classified as non-trials](docs/NEGATIVE_AUDIT.md).
- [Source databases](docs/DATA_SOURCES.md), [data dictionary](docs/DATA_DICTIONARY.md), [materials index](docs/RESEARCH_MATERIALS.md).
- [Minimized screening snapshot](data/record_level_results.jsonl), [reference coding](data/reference_coding.jsonl), [additional author decision](data/additional_reference_coding.jsonl), [current linkage pairs](data/linkage_pair_assessments.jsonl).

## Reproduce and check

Python 3.9 or newer; numerical analysis uses the standard library.

```bash
python3 scripts/verify.py --snapshot
python3 scripts/reproduce.py --allow-provisional
python3 scripts/export_review_worklist.py
python3 scripts/verify.py --generated
```

Explicitly provisional outputs are generated in `.provisional_results/`, which is excluded from version control. They can reproduce the retained snapshot but must not be cited as final manuscript results. The release check below is expected to stop until the open identity issues are resolved:

```bash
python3 scripts/check_release_status.py
```

Passing integrity or reproduction checks establishes computational consistency, not complete deduplication or independent validation of all classifications. Superseded tables, figures and the earlier enriched-reference performance comparisons have been removed from the active branch. Historical commits and tags are retained without rewriting history.

## Source data, citation and rights

Bibliographic data and basic source variables originate in the [Social Work Meta-Data Project](https://github.com/beperron/SocialWork-MetaData). Cite the study manuscript and the source database publications listed in [Data sources](docs/DATA_SOURCES.md). Do not substitute the upstream scientific-research core for this study's screening extract.

Source abstracts, full-text PDFs, unpublished manuscript files, internal correspondence, personal reviewer returns and the local archive are not distributed here. Third-party materials retain their own terms. No study-code license or repository DOI has been assigned. [CITATION.cff](CITATION.cff) identifies this methods and data-snapshot repository; a final statistical release has not been issued.
