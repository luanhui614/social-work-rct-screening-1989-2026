# Verification of records both models classified as non-trials

Source: Brian's classification report, section 12 and embedded `review` objects; original workbench membership is retained in the public data. [Original design metadata](../materials/original_review_design.json) preserve the source-reported values, including frame-label distributions and timestamps.

## Candidate frames

Start with records for which neither model calls INDIVIDUAL or CLUSTER. The boundary frame contains records with either model's trial-label score ≥0.02. The keyword frame contains records with explicit allocation wording under the following source-reported expression:

```regex
\b(random(?:ly)?[- ](?:assign|allocat)\w*|randomi[sz](?:ed|ation)|RCT|random[- ]assignment|random[- ]allocation)\b
```

The expression is retained verbatim. The original generator's regex flags and exact text-normalization implementation are not established. The actual retained frame membership is used rather than regenerating membership under guessed settings.

|Quantity before analysis cleaning|Journal|Conference|
|---|---:|---:|
|Concordant-negative pool|64,834|23,207|
|Boundary frame|392|276|
|Keyword frame|435|1,015|
|Frame overlap|51|131|
|Frame union|776|1,160|
|Sampled from each frame|150|150|
|Overlap among selected IDs|8|12|
|Unique selected negative IDs|292|288|

Frame overlap, sample overlap and positive findings are different quantities. No independence of the overlapping frames is assumed.

## Sampling documentation

The source report states random samples of 150 from each candidate frame and seed **20260905**. Metadata generation timestamps are 2026-09-05 09:35 UTC (journal) and 20:44 UTC (conference); these are not independently established inference dates. The original RNG implementation, independent-draw procedure, without-replacement implementation and order of sampling versus deduplication are not recoverable from the retained source. No replacement generator is represented as the original.

The journal workbench is 71 disagreements + 385 positives + 150 + 150 − 8 overlapping sampled IDs = 748. The conference workbench is 55 + 531 + 150 + 150 − 12 = 874. The public worklist export recovers these exact selected IDs; it does not resample them.

## Interpretation and current status

The reference-coding snapshot identifies the observed eligible and non-eligible sampled records. Analysis must first apply record-identity and abstract-information exclusions, then calculate sample NPV within retained sampled records. This evaluates the analyzed targeted samples, not the complete negative pool. No whole-corpus sensitivity or sampling-weighted primary count is inferred.

The final cleaning retains 286 journal and 288 conference sampled records. Human review identifies two and four RCT reports, respectively; sample NPV is 284/286 (99.3%) and 284/288 (98.6%). Cleaning decisions are recorded in [Data quality status](DATA_QUALITY_STATUS.md). These targeted candidate-pool definitions must not be described as two different model-specific negative pools.

Current frozen counts and the original-versus-cleaned worklist denominators are in [Count flow](COUNT_FLOW.md). Final source flags and category decisions are in the frozen record file; source duplicate flags alone are not the full cleaning procedure.
