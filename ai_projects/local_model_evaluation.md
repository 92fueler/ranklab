# Local model evaluation

## Core project

Build an evaluation harness for a model served locally through Ollama.
Accept cases containing an identifier, prompt, and optional reference output.
Record each case's output, latency, errors, and retries. Summarize task quality
separately from operational performance.

Make model selection, timeout, retry policy, temperature, and concurrency
configurable. Keep evaluation logic backend-independent.

The dataset, quality metric, and acceptable score are unspecified. Define
them; explain how cases without references are assessed.

## Additional engineering choices

These questions are optional extensions:

- How are malformed cases, duplicate identifiers, and invalid settings handled?
- Which failures are retryable, and how are individual attempts recorded?
- Does reported latency include retries and waiting for a concurrency slot?
- How are configurations and results retained for comparison?
- How are cancellations, partial runs, and unavailable backends represented?

## Offline validation

Use a deterministic fake backend to test success, timeout, transient failure,
retry exhaustion, and concurrency limits without model downloads or paid
requests. Distinguish these checks from model-quality measurements.

## Deliverables

- Harness, case format, configuration, and result format.
- Offline tests and an example report.
- Rationale for quality and operational metrics.
