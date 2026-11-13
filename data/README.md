# Frozen minimized data

- `record_level_results.jsonl.gz`: all 89,083 original source IDs, original model labels, source duplicate flags, final cleaning flags, source years, final years and final reference labels where available.
- `source_to_analysis_mapping.jsonl.gz`: every original source ID mapped to its retained analysis record or documented exclusion.
- `reference_coding.jsonl`: the original 1,622-source-ID verification worklist with final classifications and cleaning flags; 1,612 classifiable records remain after cleaning.
- `additional_reference_coding.jsonl`: one author decision outside that worklist (journal 37634, SECONDARY).
- `duplicate_article_mapping.json`, `bibliographic_candidate_decisions.json`, `year_corrections.json`: cleaning provenance.
- `linkage_pair_assessments.jsonl`, `linkage_record_outcomes.jsonl`: 327 candidate-pair decisions and 559 conference report outcomes.
- `freeze_status.json`, `flow_counts.json`: version and complete count chain.

No abstract or PDF content is included. Category labels are human reference decisions only where a reference decision exists. Null labels for unreviewed model negatives must not be interpreted as missing model classifications or human-confirmed exclusions.
