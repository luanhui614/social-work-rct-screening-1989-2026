# Research materials index

|Material|File|Purpose|
|---|---|---|
|Current publication status|[Release status](../RELEASE_STATUS.json); [quality review](DATA_QUALITY_STATUS.md)|Separates reproducibility of a retained snapshot from readiness of final statistical results|
|Eligibility criteria and categories|[Codebook](CODEBOOK.md)|The manuscript's five conditions and seven substantive labels, grounded in the supplied original criteria|
|Actual documented prompt|[Prompt v2](MODEL_PROMPT_v2.md); [JSON](../materials/initial_screening_prompt_v2.json)|Verbatim system prompt and user template|
|Model setup|[Execution](MODEL_EXECUTION.md); [configuration](../config/study.json); [timing summaries](../materials/documented_model_run_summary.json)|Documented settings and explicit unknowns; no invented runner or release identifier|
|Human review|[Protocol](REFERENCE_REVIEW_PROTOCOL.md); [blank form](REVIEW_FORM.md)|Review roles, final author decisions and reusable fields|
|Sampling|[Both-model-negative samples](NEGATIVE_AUDIT.md); [design metadata](../materials/original_review_design.json)|Source candidate pools, documented expression, overlaps and seed; not an assertion that the original generator was recovered|
|Source data|[Attribution](DATA_SOURCES.md); [registry](../data/source_registry.json); [dictionary](DATA_DICTIONARY.md)|Upstream database citations, extract identities and variable definitions|
|Coding snapshots|[Screening](../data/record_level_results.jsonl); [reference coding](../data/reference_coding.jsonl); [additional decision](../data/additional_reference_coding.jsonl)|Retained model calls and latest accepted human categories; no silent relabeling|
|Known identity issues|[QC cases](../data/identity_qc_cases.json)|Traceable duplicates, potential duplicates and label conflicts|
|Linkage snapshot|[Pairs](../data/linkage_pair_assessments.jsonl); [report outcomes](../data/linkage_record_outcomes.jsonl)|Current relationships and aggregation, with indeterminate identities retained|
|Analysis|[Decision/statistics code](../scripts/study.py); [reproduction](../scripts/reproduce.py); [verification](../scripts/verify.py); [release gate](../scripts/check_release_status.py)|Provisional numerical reproduction with a separate final-release check|
|Provenance|[Document fingerprints](../materials/source_document_provenance.json)|Identifies supplied sources without distributing manuscript drafts|

The active branch omits earlier enriched-reference performance comparisons, superseded result tables/figures, manuscript drafts, full abstracts/PDFs, private correspondence and personal reviewer return files. Necessary original method inputs, including the verbatim prompt and sampling metadata, remain because they document what was actually done. No license or DOI has been added.
