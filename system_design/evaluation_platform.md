# Evaluation platform

## Core prompt

Design a platform for evaluating AI, comparing changes, and investigating
regressions.

Choose a model, retrieval pipeline, or tool-using agent. Define the workload,
quality objectives, latency, and cost constraints.

## Questions to resolve

- Are evaluations batch experiments, online measurements, or both?
- What identifies an evaluation case and the expected behavior?
- Which datasets, model versions, prompts, configurations, and dependencies must
  be pinned or recorded?
- Which results use deterministic checks, model-based scoring, or human review?
- How are rubric changes, reviewer disagreements, and uncertain judgments handled?
- What metrics, data slices, and baselines support meaningful comparisons?
- Who can access inputs, outputs, and traces, and how is sensitive data protected?

## Optional design directions

Trace submission to a reviewable comparison. Consider:

- How runs expand into tasks, receive budgets, and record progress.
- How sandboxing isolates evaluated code and constrains external tool actions.
- How timeouts, retries, duplicate execution, and partial results affect scoring.
- How artifacts preserve lineage from dataset and configuration through outputs,
  scores, review decisions, and aggregate reports.
- How scorers and reviewers are versioned and calibrated.
- How slice metrics expose regressions hidden by aggregate improvements.
- How sampling, stochastic outputs, and measurement uncertainty affect conclusions.
- How quotas, caching, retention, and observability control cost.

Distinguish reproducible configuration from identical outputs. Explain what can
be replayed when an external model or dependency changes. For online evaluations,
clarify whether the platform observes existing traffic or changes live behavior.

## Validation scenarios

1. A worker fails after a model call but before saving its output.
2. A dataset changes while an evaluation run is in progress.
3. A scoring-model update reverses the ranking of two candidate systems.
4. The overall score improves while an important slice regresses.
5. Reviewers disagree on a case with an ambiguous rubric.
6. A run exhausts its budget with only some cases completed.

Identify authoritative artifacts, recovery, and what each comparison may conclude.

## Related exercises

- [Job scheduler and task execution](job_scheduler.md) focuses on durable execution.
- [Human annotation and quality control](annotation_quality_control.md) covers review workflows.
