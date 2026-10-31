# Targeted concordant-negative audit

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

## Completed quality assurance

Four duplicate journal indices and one insufficient journal abstract leave 287 classifiable unique journal negative-sample records; conference records remain 288. Final review identified 2 and 4 eligible reports, respectively. These observed records are retained in the identified report lists.

Sample negative predictive values are 285/287 (99.30%) and 284/288 (98.61%). Their intervals are provided in [Table S6](../tables/Table_S6_verification_intervals.md). They describe the targeted samples; they do not establish the sensitivity or NPV of the entire negative pool. No sampling-weighted adjustment of the primary report counts is applied.

The resulting dataset is an observed, verified-where-reviewed inventory with explicit unreviewed model-negative statuses. It is not a design-unbiased estimate of all RCT reports. Adding an observed eligible record corrects that record's classification; it does not imply extrapolation to unobserved records.
