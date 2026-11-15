# Model configuration

Both models classified titles and abstracts with the same written codebook. The system message and user-message template are preserved in the [verbatim v2 prompt](MODEL_PROMPT_v2.md) and [JSON](../materials/initial_screening_prompt_v2.json). Settings below are transcribed from the study's supplied classification report.

|Setting|Value|
|---|---|
|Screener A identifier|`qwen3.8:27b-mlx`|
|Screener B identifier|`qwen3.8-flash-next:125b-mlx`|
|Serving interface|Local Ollama native chat endpoint|
|Input|Title and abstract|
|Thinking|`false`|
|Temperature|`0`|
|Output budget|`num_predict: 6`|
|Output|One of seven category labels|
|Recorded output alternatives|First-output-token log probabilities; `top_logprobs: 5`|
|Fine-tuning|None|
|Few-shot examples|None|
|Source-reported failed or thinking-leaked records|Zero for each model|

The released analysis scripts use the retained classifications and final reference decisions as inputs. Model trial-label scores determine the score-based negative candidate pool. [Sampling documentation](NEGATIVE_AUDIT.md) describes that use of the scores.
