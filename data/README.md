# Released data

|File|Contents|
|---|---|
|`record_level_results.jsonl.gz`|All 89,083 source IDs, original model classifications, final reference classifications where reviewed, selection flags and cleaning fields|
|`source_to_analysis_mapping.jsonl.gz`|Source IDs, retained analysis IDs and exclusion reasons|
|`reference_coding.jsonl`|Final classifications and cleaning fields for the 1,622 selected source IDs; 1,612 retained verification records|
|`additional_reference_coding.jsonl`|One separately recorded SECONDARY decision outside the designed verification sample|
|`duplicate_article_mapping.json`|Corroborated same-article groups and retained records|
|`bibliographic_candidate_decisions.json`|Final bibliographic identity decisions and supporting publication metadata|
|`year_corrections.json`|Source and analysis years with bibliographic basis|
|`author_adjudications.json`|Final author decisions for the listed same-article groups|
|`linkage_pair_assessments.jsonl`|Final assessments for 327 conference–journal candidate pairs|
|`linkage_record_outcomes.jsonl`|Aggregated outcomes for 559 conference RCT reports|
|`flow_counts.json`|Complete source-to-analysis count flow|
|`freeze_status.json`|Analytical freeze identifier and counts|
|`source_registry.json`|Source project identifiers and screening-extract fingerprints|

The [data dictionary](../docs/DATA_DICTIONARY.md) defines the fields. Null reference labels identify records without a final human classification; unreviewed model negatives remain distinguishable from human-confirmed non-RCTs. Detailed linkage-assessment codes support the primary confirmed-link outcome reported in the manuscript.
