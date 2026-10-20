# General – VLM and video evaluation

## References

- [Official Ego4D natural-language-query evaluator](https://github.com/EGO4D/episodic-memory/blob/main/NLQ/VSLNet/utils/evaluate_ego4d_nlq.py): a concrete temporal-localization scoring reference.
- [Evaluation-metrics notes](../questions/evaluation_metrics.md).
- [General evaluation-platform exercise](evaluation_platform.md).

## Evidence status

This is an original practice exercise, not an actual reported FigureAI system-design question. Ego4D provides a task-specific evaluation implementation, not a company interview prompt or a complete VLM evaluation specification. All platform requirements and operational targets below are proposed exercise assumptions. Metrics must match the chosen task rather than being transferred indiscriminately from that benchmark.

## Problem statement

Design an evaluation system for a vision-language model operating on video, so that model or dataset changes can be compared and failures can inform later data work. Select a primary task, such as video question answering or locating a described event in time.

## Functional requirements

For the proposed scope:

- Define evaluation cases with video references, prompts, expected behavior, and relevant labels.
- Identify the exact input preparation, model configuration, and scoring rules used in each run.
- Record predictions, supporting time ranges where relevant, and execution failures.
- Compare versions overall and across meaningful scene or activity categories.
- Support review of ambiguous labels, unsupported answers, and scorer disagreements.
- Detect or flag related footage crossing training and evaluation boundaries.
- Preserve prior results when labels or scoring rules are corrected.

## Non-functional requirements

Clarify corpus size, clip lengths, run frequency, completion time, and compute budget. Set access and retention requirements for recorded footage. Require interpretable coverage, uncertainty, and failure reporting. Define repeatability expectations, temporal-alignment tolerance, and the treatment of unanswerable or missing cases. No fixed quality threshold or latency target is assumed.

## Optional failure conditions

A plausible answer lacks video evidence; a predicted event window is shifted; near-duplicate footage leaks into the test set; a judge systematically disagrees with reviewed examples; one activity regresses despite a higher aggregate score. State expected evaluation behavior without prescribing model architecture or infrastructure.
