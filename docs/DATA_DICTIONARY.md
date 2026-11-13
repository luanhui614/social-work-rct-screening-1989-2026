# Record-level data dictionary

The retained `data/record_level_results.jsonl` contains 89,083 source IDs. This preserves original model calls, latest accepted human categories and existing source cleaning flags. It is a source-record snapshot, not a fully deduplicated publication list. Read [release status](../RELEASE_STATUS.json) before interpreting fields with legacy names such as `final_reference_label`.

|Field|Meaning|
|---|---|
|corpus|swrd or sswr; keep corpora separate|
|record_id|Original source identifier as a string; uniqueness of this ID does not establish unique publication identity|
|year|Source publication/conference year; bibliographic year reconciliation is pending for duplicate groups|
|source_name_or_format|Source journal name or conference format|
|doi|Source identifier where supplied; some source values are non-DOI identifiers and must not be silently treated as valid DOI registrations|
|model_a_label / model_b_label|Original seven-category model outputs|
|screening_group|concordant_positive / discordant / concordant_negative, based on binary RCT calls|
|is_duplicate|Existing upstream duplicate-index flag; excludes those flagged records but is not an exhaustive identity check|
|insufficient_abstract|Author-designated insufficient abstract, excluded during cleaning rather than labeled non-RCT|
|in_original_audit|Membership in the historical 1,622-ID verification workbench|
|sample_membership|confirmed / disagree / boundary / keyword, retaining overlapping selection reasons|
|final_reference_label|Latest author-accepted substantive label retained in this snapshot; null for unreviewed negatives or the unclassifiable abstract. It is not an assurance that the source ID is a unique publication|
|reference_status|Legacy snapshot classification status. `final_reference` refers to the retained categorical decision; global publication status remains pending identity reconciliation|

`reference_coding.jsonl` retains the 1,622 workbench records. `additional_reference_coding.jsonl` retains a purpose-specific author decision outside that workbench. No human label or evidence quote has been invented to fill missing information.

`identity_qc_cases.json` records known duplicate identities, conflicting labels and pending actions. It is a review sidecar: no unresolved conflict is silently converted into a new final label or exclusion.

`linkage_pair_assessments.jsonl` contains recorded assessed pairs, not all retrieved candidates. Relations are SAME, RELATED, DIFFERENT, INDETERMINATE or NOT_ELIGIBLE_OUTCOME. `assessment_basis` documents that selected full texts and project materials supplemented identity checks. `author_adjudicated` identifies an explicit retained author decision; it does not claim universal independent double-human validation. `linkage_record_outcomes.jsonl` is the report-level aggregation of the current pair snapshot.
