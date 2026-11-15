# Selection and verification of concordant-negative records

Within records both models classified as non-RCTs, two candidate pools were defined separately for each corpus:

1. **Score pool:** either model's trial-label score was at least 0.02.
2. **Keyword pool:** allocation-related wording matched the source expression below.

```regex
\b(random(?:ly)?[- ](?:assign|allocat)\w*|randomi[sz](?:ed|ation)|RCT|random[- ]assignment|random[- ]allocation)\b
```

The score is an output-label score, not a calibrated probability of study eligibility. The pools overlap. Each contributed 150 selected source records; a source record selected through both pools was reviewed once. The retained selection metadata are in [sampling design](../materials/sampling_design.json). Record-level `sample_membership` flags identify the selected samples.

|Selection quantity|Journal|Conference|
|---|---:|---:|
|Score-pool source records|392|276|
|Keyword-pool source records|435|1,015|
|Overlap between candidate pools|51|131|
|Selected from each pool|150|150|
|Overlap between selected samples|8|12|
|Unique selected source records|292|288|
|Records retained for verification after cleaning|286|288|
|Human-confirmed RCT reports|2|4|
|Human-confirmed non-RCT reports|284|284|
|Sample NPV|99.3%|98.6%|

The selected source-ID lists are fixed; data-cleaning exclusions are applied before calculating performance. Sample NPV is calculated within the retained targeted samples. Final RCT counts include the eligible reports actually identified through review, without sampling-weighted expansion. These results describe the candidate samples and do not estimate sensitivity or NPV for the complete concordant-negative pool.
