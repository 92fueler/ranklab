# Humanoid KinetIQ: Data, training, and evaluation platform

Published-system-inspired exercise; not a verified interview prompt.

## References

- [Humanoid: KinetIQ AI Stack Overview](https://thehumanoid.ai/technology/kinetiq-ai-stack-overview/)

## Published System Context

Humanoid describes multi-camera, language, and state inputs with flow-matching or autoregressive action heads, action-prefix conditioning, and tools for collection, training, and evaluation. It records teleoperation and autonomous execution, captures interventions, and describes temporal preprocessing that preserves fragile behavior phases. The exercise targets supporting infrastructure, not reproducing KinetIQ's control stack.

## Problem Statement

Design a capability-development backend for robot trainers, ML researchers, and evaluation operators. It should turn demonstrations, autonomous runs, and intervention records into reviewable datasets, training runs, and capability reports. Researchers must compare data and model variations without confusing improvements in task speed with improvements in task reliability.

All requirements below are proposed exercise scope, not claims about Humanoid's private infrastructure.

## Functional Requirements

- Ingest recording sessions with synchronized camera streams, language goals, state, actions, controller/model versions, and collection mode; capture transitions between autonomy and human control.
- Preserve interventions and outcomes as distinct evidence. Let reviewers identify why intervention occurred rather than automatically labeling every intervened episode unsuccessful.
- Let trainers inspect, label, select, and combine task segments into versioned datasets, retaining their original context and supervision provenance.
- Support configurable preprocessing recipes, including temporal adjustments. Record changed timing and protected task phases so consumers can audit whether transformed labels remain valid.
- Let researchers specify supported action-head variants and action-prefix training inputs without silently changing the data contract between runs.
- Submit, monitor, cancel, and recover distributed training experiments; persist checkpoints with dataset, preprocessing, model, and configuration versions.
- Manage evaluation suites and compare task success, throughput, intervention frequency, and important failure conditions using consistent measurement definitions.
- Expose recording-registration, dataset-review, experiment-control, checkpoint, and evaluation-result interfaces. Promotion to live robot operation requires separate approval.

## Non-Functional Requirements

Proposed exercise assumptions, not Humanoid's reported service guarantees:

- Lost connectivity must not silently erase accepted recordings or intervention evidence.
- Train/evaluation separation must survive segment reuse and dataset revisions.
- Routine worker failures must not corrupt released datasets or checkpoints.
- Compute contention, data-processing delays, and experiment costs must be observable.
- Access controls must protect operational footage and allow only authorized dataset changes.

## Requirements to Clarify

Agree on robot types, recording rates, intervention semantics, episode volumes, trainer concurrency, and training budgets. Which temporal changes are allowed, and how are they validated? Set capability acceptance criteria, recovery targets, and evaluation capacity. Keep real-time control latency separate from this offline platform's service targets.
