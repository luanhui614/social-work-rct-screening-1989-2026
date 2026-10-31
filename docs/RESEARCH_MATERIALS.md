# Research materials accompanying the manuscript

This index connects the manuscript to its documented screening materials, final reference protocol and reproducible results. All links below are relative to this version of the repository.

|Material|File|Function|
|---|---|---|
|Initial screening prompt|[Prompt v2](MODEL_PROMPT_v2.md); [machine-readable system and user messages](../materials/initial_screening_prompt_v2.json)|Exact prompt documented in Brian's classification report; applied to the two initial screeners|
|Model settings and run summary|[Execution information](MODEL_EXECUTION.md); [configuration](../config/study.json); [source-reported timings](../materials/documented_model_run_summary.json)|Documented settings, output format, score interpretation and unavailable execution details|
|Final eligibility definitions|[Frozen codebook v1.3](CODEBOOK_v1.3.md)|Author-approved operational definitions used for final reference coding; seven substantive categories|
|Reference review and final adjudication|[Review protocol](REFERENCE_REVIEW_PROTOCOL.md); [blank review form](REVIEW_FORM.md)|Review procedure, roles and evidence fields; the blank form is provided for reuse, not as a claim that every historical field was completed|
|Targeted negative audit|[Audit design](NEGATIVE_AUDIT.md); [original design metadata](../materials/original_review_design.json)|Actual frame definitions, regex, reported seed, overlap and recovered sample membership|
|Original operational benchmark|[Benchmark explanation](REFERENCE_REVIEW_PROTOCOL.md#original-operational-benchmark); [source benchmark metadata](../materials/original_reference_benchmark.json); [Table S1](../tables/Table_S1_original_reference.md)|Auxiliary original model validation; separate from completed verification and final counts|
|Source databases and basic variables|[Source attribution](DATA_SOURCES.md); [data dictionary](DATA_DICTIONARY.md); [source registry](../data/source_registry.json)|Upstream database citations, scope, IDs and variable meanings|
|Final reference coding|[Workbench coding](../data/reference_coding.jsonl); [additional decision](../data/additional_reference_coding.jsonl)|Final categorical decisions; no superseded personal coding files|
|Record-level screening and analysis|[Record-level results](../data/record_level_results.jsonl); [decision rules](../scripts/study.py); [analysis](../scripts/reproduce.py)|Reconstruct final report eligibility and all numerical summaries|
|Conference–journal linkage|[Recorded pair assessments](../data/linkage_pair_assessments.jsonl); [method](METHODS.md#analysis-and-linkage); [outcomes](../results/linkage.md)|Recorded assisted assessments and report-level aggregation; unresolved identities remain explicit|
|Tables, figures and numerical results|[Summary](../results/SUMMARY.md); [tables](../tables); [figures](../figures)|Publication results and source-level summaries|
|Source-document provenance|[Source filenames and fingerprints](../materials/source_document_provenance.json)|Identifies the supplied source documents from which method details were extracted|

## Reading the versions correctly

Prompt v2 documents what the initial models actually received. Codebook v1.3 supplies the clarified final manual eligibility definitions. The models were not rerun under v1.3; final reference decisions override model suggestions for reviewed records. Neither the old prompt's broad follow-up wording nor an earlier pilot configuration replaces the frozen final definitions.

The source classification report identifies locally hosted Ollama models. An earlier pilot codebook describes a different vLLM setup; that preliminary configuration is not presented as the final full-corpus run. Source-report model identifiers are retained verbatim without inferring a model revision or weight digest.

The public package contains current analysis materials and necessary historical method inputs such as the actual initial prompt. Superseded results and draft interpretations remain in the local archive. Full unpublished manuscript files, correspondence, raw reviewer returns and source abstracts are not redistributed. No new license or repository DOI has been assigned.
