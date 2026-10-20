# General – AI evaluation platform

## References

- [NVIDIA Cosmos evaluation overview](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/evaluation/overview.html): technical inspiration for task-dependent evaluation, not interview evidence.
- [Evaluation-metrics notes](../questions/evaluation_metrics.md).

## Evidence status

This is an original general practice exercise, not an attributed Mercor, FigureAI, or other company interview question. The Cosmos reference concerns evaluation of video-generation model families; it does not specify a universal evaluation platform. The broader product requirements below are exercise assumptions, and no numerical targets are source facts.

## Problem statement

Design a platform that evaluates changes to a selected AI system, compares them with a baseline, and helps users investigate regressions. Choose a model, retrieval system, or tool-using agent and define what successful behavior means for that workload.

## Functional requirements

For the proposed exercise:

- Submit an evaluation with identified cases, system configuration, and scoring rules.
- Record per-case outputs, scores, execution failures, latency, and cost where measurable.
- Show progress and distinguish incomplete runs from complete comparisons.
- Compare versions overall and across relevant data slices.
- Let reviewers inspect disputed cases and record corrections or adjudications.
- Preserve enough provenance to identify the data, configuration, and scoring procedure behind each result.
- Keep execution failures distinct from model-quality failures under a declared scoring policy.

Online experiments and actions affecting live users are outside the default scope.

## Non-functional requirements

Choose run volume, dataset size, completion-time, availability, and budget targets. Define data access, retention, isolation, and recovery expectations. Require transparent uncertainty and comparison coverage. Clarify what reproducibility means when a model is stochastic or an external dependency changes; recorded configuration alone need not guarantee identical outputs.

## Optional failure conditions

A dataset changes during a run; a scorer update reverses a ranking; aggregate performance improves while a critical slice regresses; reviewers disagree; a run stops after exhausting its budget. Specify what users can conclude without selecting a model judge, execution framework, or database.
