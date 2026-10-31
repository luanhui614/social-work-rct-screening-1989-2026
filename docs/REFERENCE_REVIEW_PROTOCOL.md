# Reference review and final adjudication

This document describes the completed study workflow. It synthesizes the original review instructions and the author-approved final protocol; it is not a verbatim copy of the original instructions. The [frozen codebook](CODEBOOK_v1.3.md) controls final eligibility.

## Purpose and routing

Both models classified every record. INDIVIDUAL and CLUSTER are positive RCT calls. Agreement about RCT status includes disagreement about allocation level. Concordant positives were verified for false positives; every binary disagreement received a final reference decision; targeted concordant-negative samples were checked for missed eligible reports.

The original workbench contained 748 journal and 874 conference IDs (1,622 in total). A record present in both audit frames was reviewed once and retained both membership flags. After removing four duplicate journal indices and one insufficient abstract, 1,617 workbench records were classifiable unique records.

Coding was allocated by corpus. A replacement coder completed unfinished work, and disputed cases received final author adjudication. Different coder files support traceability; they do not establish that all records were independently rated by two humans. Final accepted author/reference decisions determine reviewed classifications. No universal human–human kappa is inferred from these files.

## Review procedure

1. Read the complete original English title and abstract. Chinese guidance translations, where available, assist reading; the English source controls interpretation.
2. Identify the sentences establishing or contradicting intervention assignment, allocation, comparison arms, participants and outcomes. The original interface allowed evidence marking, notes and discussion flags.
3. Apply the five conditions and the report-purpose definitions in the frozen codebook. Select one substantive label. Do not determine eligibility from a model's confidence, the word “follow-up”, the data type or a named parent trial alone.
4. Refer genuinely unresolved evidence or conflicting report relationships for final adjudication. Obtain additional source information where necessary and document the decision.
5. Retain the final categorical decision and join it to the record ID and corpus. Final decisions override model calls. Exclude duplicates and abstracts insufficient for classification during cleaning.

The original workbench displayed model panels and optional prior-verdict panels. Its instructions recommended deciding from the abstract first, before inspecting those panels. This completed review is not described as universally blinded. The source instructions allowed UNCERTAIN as a pending status; the final classifiable analysis set has no unresolved eligibility labels. The insufficient abstract is a cleaning exclusion, not a confirmed negative.

## Eligibility in the final analysis

Only INDIVIDUAL and CLUSTER enter the RCT numerator. Five conditions must hold: an actual prospectively assigned intervention; explicit random allocation; two or more conditions; human participants or human service units with outcomes; and actual post-intervention participant-outcome comparisons between randomized conditions. Null findings can qualify.

The report's principal purpose distinguishes an intervention-effect report from an ancillary mechanism, subgroup, dose, process or explicitly ancillary follow-up report (SECONDARY). Original-team authorship, existing data, a later measurement time or a secondary outcome alone does not determine exclusion. Baseline-only/design reports are PROTOCOL. Qualitative and mixed-methods findings can qualify when they actually compare randomized groups on participant outcomes. Attendance, attrition, acceptability and fidelity alone do not satisfy the outcome condition. Hypothetical-vignette judgment experiments are OTHER. The full category definitions and exceptions remain in the codebook.

A [blank form](REVIEW_FORM.md) makes these fields reusable. It does not imply that all historical reviewers supplied all fields: the public final coding file contains final categories and membership flags, not reconstructed sentence-level justifications.

## Original operational benchmark

Brian's original enriched reference sets (609 journal records and 300 conference abstracts) had a separate model-validation function. The documented journal provenance was 66 manually read, 536 agent-agreement and 7 author-adjudicated records; conference provenance was 288 agent-agreement and 12 author-adjudicated records. These are author-accepted operational reference sets, not universally independently double-human-coded gold standards.

Their source-reported aggregate labels, provenance and performance are retained in [benchmark JSON](../materials/original_reference_benchmark.json) and [Table S1](../tables/Table_S1_original_reference.md). They are not substituted for the completed 1,622-ID verification workbench or used to claim full-corpus sensitivity. Earlier draft totals and superseded record decisions are not reintroduced as current results.

## Final results and public files

Journal concordant positives retained 375/385; disagreements added 11/71; targeted negatives added 2/287 classifiable unique records. Conference counts were 527/531, 28/55 and 4/288. The final identified totals are 388 and 559 reports. A separate purpose-specific additional decision retained one journal record as SECONDARY; it is outside the workbench's sampling denominators.

- [Final workbench classifications](../data/reference_coding.jsonl)
- [Additional final classification](../data/additional_reference_coding.jsonl)
- [Record-level results and cleaning flags](../data/record_level_results.jsonl)
- [Actual review-worklist recovery](../scripts/export_review_worklist.py)
