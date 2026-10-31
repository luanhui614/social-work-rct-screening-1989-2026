# Record-level data dictionary

`data/record_level_results.jsonl` contains 89,083 source IDs, one JSON object per line. Analysis removes the flagged duplicates and insufficient abstract; it retains 88,189 records. `null` final reference labels are not human-confirmed non-RCT labels.

|Field|Meaning|
|---|---|
|corpus|swrd or sswr; keep the corpora separate|
|record_id|Source record identifier, stored as a string|
|year|Publication or conference year|
|source_name_or_format|Journal name or canonical conference presentation format|
|doi|Source DOI where available|
|model_a_label / model_b_label|Original seven-class model outputs|
|screening_group|concordant_positive / discordant / concordant_negative, based on binary RCT calls|
|is_duplicate|Duplicate-index flag; exclude from analysis|
|insufficient_abstract|Author-designated insufficient/partly missing abstract; exclude from analysis rather than label non-RCT|
|in_original_audit|Membership in the original 1,622-ID verification workbench|
|sample_membership|confirmed / disagree / boundary / keyword; multiple flags retain overlapping selection reasons|
|final_reference_label|Final accepted substantive category for reviewed records; null for unreviewed negatives and the unclassifiable abstract|
|reference_status|final_reference / model_negative_not_reviewed / unclassifiable_abstract|

`reference_coding.jsonl` contains the 1,622 workbench members with final categorical decisions and cleaning flags. Original C1–C5 answers are not presented as newly completed answers under the final codebook. `additional_reference_coding.jsonl` contains the one additional purpose-specific final exclusion and is not part of the negative audit.

`linkage_pair_assessments.jsonl` contains assessed pairs, not all retrieved candidates. `relation` is SAME / RELATED / DIFFERENT / INDETERMINATE. Journal ID, year and DOI are provided where retained. `independent_human_linkage_gold` is false: these are assisted abstract/record assessments. Pair uncertainty must not be treated as a negative RCT label.

Report-level final inclusion is computed by `scripts/study.py`: remove cleaning exclusions, apply final reference labels, and retain model-negative/unreviewed status for the rest. No missing labels are silently filled with an invented human judgement.
