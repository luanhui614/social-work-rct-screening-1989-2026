# Documented model execution

Source: Brian's supplied classification write-up, section 4 and embedded summary statistics. These are documented report-level settings and summaries, not independently recovered execution logs. Source filenames and SHA-256 fingerprints are in [provenance](../materials/source_document_provenance.json).

|Item|Documented value|
|---|---|
|Screener A identifier|`qwen3.8:27b-mlx`|
|Screener B identifier|`qwen3.8-flash-next:125b-mlx`|
|Serving interface|Local Ollama native chat endpoint|
|Input|Title and abstract; exact [v2 system and user messages](MODEL_PROMPT_v2.md)|
|Thinking|`false`|
|Temperature|`0`|
|Output budget|`num_predict: 6`|
|Output|Exactly one of seven categorical labels, with no explanation|
|Recorded alternatives|First-output-token log probabilities, `top_logprobs: 5`|
|Fine-tuning / few-shot examples|Neither, according to the source report|
|Failed or thinking-leaked records|Source report states zero for each model|
|Exact run dates, model-weight digests|Not established from retained materials|
|Input truncation, timeout and retry implementation|Not established; no original inference runner retained|

The names above are transcribed from the source report; they do not independently verify a model release, parameter count or weight build. Records were classified separately by each screener. Shared model family and prompt mean their errors should not be assumed statistically independent.

## Source-reported performance of execution

|Corpus|Screener|Median seconds per abstract|Accumulated model hours|Wall-clock hours|
|---|---|---:|---:|---:|
|Journal|A|2.295|42.975|10.809|
|Journal|B|4.891|88.965|11.280|
|Conference|A|5.617|41.348|10.410|
|Conference|B|8.600|55.452|7.113|

Unrounded reported summary values are retained in [JSON](../materials/documented_model_run_summary.json). Accumulated processing time and wall-clock time differ because requests were concurrent; the final run's concurrency setting is not established here. A review-workbench generation timestamp is not a model execution date.

## Interpretation of scores

The reported chosen-label confidence is an output-label score. The negative-audit boundary rule uses either model's trial-label score of at least 0.02; this is not a calibrated 2% probability that a record is a true RCT. The original log-probability-to-trial-score implementation is not reconstructed without its generator. The retained frame memberships determine this study's audit sample.

The original runner, raw execution logs and undocumented retry behavior are not fabricated. The public scripts reproduce decisions and analyses from retained classifications and final reference decisions; they do not claim to rerun the original inference job.
