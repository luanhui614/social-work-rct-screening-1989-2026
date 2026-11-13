# RCT screening codebook

These are the eligibility criteria and seven substantive categories stated in the current manuscript, grounded in the supplied original manuscript and written screening codebook. The same substantive criteria govern model screening and final human verification. The [documented v2 prompt](MODEL_PROMPT_v2.md) is preserved verbatim rather than rewritten retrospectively. Record-level category decisions are retained in the reference-coding snapshot; publication-identity and label-consistency checks remain open as listed in [Data quality status](DATA_QUALITY_STATUS.md).

A record qualifies as an RCT report only when its abstract supports all five conditions:

1. Investigators prospectively delivered or assigned an actual intervention, rather than merely observing a condition or re-analysing another study's data.
2. Participants or intact clusters were allocated by an explicitly random mechanism stated in the abstract.
3. At least two conditions were compared, including an active comparator, usual treatment, attention control, placebo or waitlist.
4. Participants were human and outcomes were measured on them.
5. Outcome results were reported in the abstract.

|Label|Definition|Included as RCT|
|---|---|---|
|INDIVIDUAL|All five conditions met; individuals, families, couples or dyads randomized|Yes|
|CLUSTER|All five conditions met; intact groups such as schools, clinics, agencies or communities randomized|Yes|
|QUASI|Actual intervention evaluation without established random allocation, including single-arm designs; group labels alone are insufficient evidence of randomization|No|
|SECONDARY|Analysis of a trial conducted and reported elsewhere, including ancillary moderator, mediator or subgroup analysis; randomization in a parent trial alone does not qualify the current report|No|
|PROTOCOL|Protocol, registration, design or baseline report without outcome results|No|
|REVIEW|Review or synthesis of other studies, including systematic reviews, scoping reviews and meta-analyses of RCTs|No|
|OTHER|Other reports, including observational, theoretical, commentary, instrument-validation and randomized-stimulus vignette or analogue judgment experiments|No|

## Decision rules

If an abstract describes an intervention evaluation without stating random allocation, classify it as QUASI rather than inferring an RCT from treatment/control terminology. Random sampling is not random allocation.

Random assignment to hypothetical scenarios, vignettes or case descriptions that elicit respondent judgments does not constitute an intervention delivered to participants and is excluded as OTHER. Assess the study actually reported, not merely a trial mentioned in the text. Data type alone does not determine eligibility.

A later measurement occasion does not itself make a report SECONDARY. The original codebook clarification permits a trial team reporting its own later-timepoint, between-arm outcomes to qualify. A protocol or baseline description without outcome findings does not qualify, even if recruitment and randomization have occurred. Null findings can qualify; statistical significance is not an inclusion condition.

UNCERTAIN was an interim review status, not an eighth substantive category. Retained classifiable source records have substantive final labels. The author-designated insufficient abstract is a cleaning exclusion, not a confirmed non-RCT.

## Authority and provenance

Criteria and category definitions follow the current manuscript's Eligibility Criteria and Table 1 and the supplied written codebook. The full-corpus run configuration is documented separately; an earlier pilot configuration is not substituted for the documented final model setup. No new human decisions are inferred from this explanatory document. Source-document fingerprints are in [provenance](../materials/source_document_provenance.json).
