# Final study method

## Unit and scope

The unit is a journal report or conference abstract, not a distinct trial. The journal extract covers 1989–2025 and the conference extract 2005–2026. Duplicate indices and the author-designated insufficient abstract are excluded from analysis; unreviewed model negatives remain clearly labelled as such.

## Dual-model consensus and final decisions

Each record was screened separately by two locally hosted Qwen-family models using prompt v2. INDIVIDUAL and CLUSTER both count as RCT calls. If both models call an RCT, the record is concordant positive, including disagreements about allocation level. If neither calls an RCT, it is concordant negative. Otherwise it is a binary disagreement.

Let A and B be the sets each model calls an RCT. Concordant positives are their intersection, A ∩ B; binary disagreements are their symmetric difference; concordant negatives are Aᶜ ∩ Bᶜ. The intersections define screening groups, not a rule that discards a contrary final reference decision.

Model consensus routes records; final accepted reference coding determines reviewed eligibility. All 385 journal and 531 conference concordant positives and all 71/55 binary disagreements received final classifications. Coding was allocated by corpus, with replacement coverage and final adjudication; it was not a fully crossed independent two-human rating of every record. Author-accepted operational reference coding is retained. This study does not compute a human–human kappa from replacement files.

Current identified counts are 375 + 11 + 2 = **388 journal reports** and 527 + 28 + 4 = **559 conference reports**. Only final INDIVIDUAL/CLUSTER reports are included. Known non-RCT classifications override a positive consensus; reviewed eligible records override a negative model call. A purpose-specific additional record was finally classified SECONDARY, without changing these totals or entering the random-audit denominators.

## Targeted negative audit

The original review package sampled 150 records from each of two candidate frames per corpus: a boundary frame with either model's trial-label score ≥0.02, and a frame containing explicit allocation wording. Frame sizes were 392/435 in journals and 276/1,015 in conferences. Frame overlaps were 51 and 131; sampled-ID overlaps were 8 and 12. The original workbench therefore contained 748 journal and 874 conference IDs, 1,622 in all.

Removing four duplicate journal indices and one insufficient abstract leaves 287 classifiable unique journal negative-sample records and 288 conference records. Two and four eligible reports were found and retained. Sample NPV is 285/287 (99.30%) and 284/288 (98.61%). It describes these targeted samples, not the complete negative pool; corpus-wide sensitivity is not identified. No sampling-weighted correction of the primary total is applied. Workbench memberships, rather than a newly generated random sample, are the analysis inputs.

The source metadata record seed 20260905, but the original RNG implementation, independent-draw mechanism, without-replacement implementation and order of sampling versus duplicate handling cannot be established from the retained generator. Unknown details remain null in the configuration; this repository does not manufacture them.

## Eligibility

The final codebook defines all categories and five RCT conditions. An eligible report evaluates a prospectively assigned actual intervention, explicitly random allocation, at least two conditions, human participant outcomes, and actual post-intervention randomized-group outcome findings. Later measurement alone does not exclude an otherwise eligible report. Ancillary mechanism, process, subgroup and explicitly ancillary follow-up reports are SECONDARY. Recruitment, baseline, attendance, attrition or fidelity alone do not establish an eligible outcome report. Qualitative/mixed-methods classification depends on actual randomized-group outcome comparisons, not the data type. Hypothetical-vignette experiments remain OTHER.

## Analysis and linkage

Rates use cleaned denominators. Wilson intervals describe identified-report proportions and do not include screening or linkage error. Journal ranking uses observed counts, not weighted estimates. Binary kappa compares models. Periods and all source-level summaries use the same final reference decisions.

Linkage searches use the entire 64,417-record journal frame, not just the identified journal RCT subset. Recorded candidate pairs are assessed for same-trial outcome reports, ancillary/development relationships or different/indeterminate identity. A ranking score or shared author does not by itself establish a match. SAME takes precedence, followed by an unresolved identity, then RELATED_ONLY, then NOT_IDENTIFIED. One conference report may have several article links; repeated presentations remain separate reports. Frozen ancillary classifications are respected. Pair identity does not automatically change a journal abstract's own eligibility label.

The current recorded assessments yield 83 same-trial, 68 related-only, 29 indeterminate and 379 not-identified outcomes among 559 conference reports. These assisted assessments are not an independent human linkage gold standard; author verification remains appropriate. Not identified does not mean unpublished. Timing uses the earliest identified SAME article and article year minus conference year, with before/same/after reported separately. Source abstracts and the full private candidate-evidence trail are not redistributed here.

## Reproducibility scope

The scripts reconstruct screening decisions, recover actual review-workbench IDs, recalculate descriptive results and aggregate recorded linkage assessments. The documented initial prompt and configuration are provided. The original model job runner, weight digests, exact execution dates, truncation/retry implementation and original sampling generator were not retained; this repository does not claim to reproduce an undocumented original inference job or regenerate its sample. Codebook definitions, final coding and retained outputs are sufficient to reproduce the reported primary analysis.
