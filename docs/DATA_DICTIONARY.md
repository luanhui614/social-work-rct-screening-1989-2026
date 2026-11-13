# Data dictionary

The main JSONL file is gzip-compressed; Python `gzip.open(path, "rt")` reads one JSON object per line. Original source IDs are unique within `corpus`. They are retained even when duplicate publication indices are excluded.

|Field|Meaning|
|---|---|
|corpus|`swrd` journal or `sswr` conference|
|record_id|Original source ID|
|year / original_year|Analysis publication year / original source year|
|source_name_or_format|Source journal or conference presentation format|
|doi|Source DOI or source identifier; a legacy non-DOI identifier must not be presented as a DOI|
|model_a_label / model_b_label|Unmodified original seven-category model calls|
|screening_group|`concordant_positive`, `discordant`, `concordant_negative`, using RCT versus non-RCT calls|
|original_is_duplicate|Original source duplicate flag|
|is_duplicate|Final duplicate-index exclusion, incorporating bibliographic checks|
|insufficient_abstract|Author-designated cleaning exclusion for inadequate abstract information|
|cleaning_exclusion_reason|Source duplicate flag, additional corroborated duplicate, insufficient abstract or null|
|analysis_record_id|Retained article/source representative; excluded source-flag duplicates or insufficient abstracts can be null|
|in_original_audit|Membership in the original 1,622-source-ID worklist|
|sample_membership|Original workbench section flags; not a new sample draw|
|final_reference_label|Latest accepted seven-category reference decision; null for unreviewed concordant negatives or excluded insufficient information|
|reference_status|Reference provenance, same-article inheritance or model-negative-not-reviewed state|
|freeze_version|Final frozen analysis version|

Duplicate-article mapping retains each source ID, retained representative, original and analysis years, final category and identity-decision IDs. A verified source record is prioritized, followed by abstract completeness, a matching registered DOI and source ID; category and model outcome are not selection criteria. Reference classifications can be inherited within a corroborated same-article group, which does not mean each index version was independently read by a human.

Linkage pairs use SAME, RELATED, DIFFERENT, INDETERMINATE or NOT_ELIGIBLE_OUTCOME. The `author_adjudicated` flag identifies explicitly recorded author pair decisions. Conference outcomes prioritize SAME, then INDETERMINATE, then RELATED_ONLY, then NOT_IDENTIFIED. Counts of assessed pairs, conference reports and different journal article IDs are separate units.
