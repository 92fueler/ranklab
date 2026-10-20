# Physical Intelligence π0.5: Mixed-supervision training platform

Published-system-inspired exercise; not a verified interview prompt.

## References

- [Physical Intelligence: A VLA with Open-World Generalization](https://www.pi.website/blog/pi05)

## Published System Context

Physical Intelligence describes π0.5 co-training on robot demonstrations, image/text tasks, bounding boxes, subtask labels, and verbal instructions across robot types. Its high-level text predictions use autoregressive decoding; continuous low-level actions use flow matching. The exercise is the infrastructure supporting such mixed supervision, not a request to redesign the model.

## Problem Statement

Design a shared training platform for researchers comparing mixtures of robot and general multimodal data. They need to launch distributed experiments, recover interrupted work, and understand which data and objectives produced a checkpoint. An experiment may contain examples with different available labels; not every example contains robot actions.

All requirements below are proposed exercise scope, not claims about Physical Intelligence's infrastructure.

## Functional Requirements

- Register versioned datasets with their modalities, supervision types, robot embodiments, permitted uses, and train/evaluation partitions.
- Let researchers submit an experiment specifying model initialization, code and configuration versions, dataset mixture, objective selection, resource needs, and evaluation plan.
- Validate that requested objectives match available labels and compatible action semantics. Distinguish recorded actions from inferred targets and absent supervision.
- Support distributed job admission, progress inspection, cancellation, and recovery after worker failure. Users must be able to determine whether a repeated request created additional work.
- Track actual data exposure and task-specific training measurements so researchers can detect a mixture imbalance or a modality that contributes no valid supervision.
- Persist checkpoints and run records sufficient to explain and resume the agreed training state; state the reproducibility guarantees when exact numerical replay is unavailable.
- Compare checkpoints on held-out robot tasks, instruction following, and relevant generalization slices, linking each result to its evaluation inputs and configuration.
- Provide interfaces for dataset lookup, experiment submission, run control, checkpoint retrieval, and comparison. Producing a checkpoint does not automatically authorize robot deployment.

## Non-Functional Requirements

Proposed exercise assumptions, not the company's reported service guarantees:

- Concurrent teams must not access one another's restricted datasets or checkpoints.
- Resource contention and failures must have visible effects on job status and cost.
- Interrupted work must recover within an agreed loss-of-progress budget.
- Training readers must sustain the selected experiment scale without changing mixture semantics.
- Released checkpoints and evaluations must have auditable lineage.

## Requirements to Clarify

Set dataset sizes, accelerator availability, job concurrency, priorities, checkpoint frequency, and retention budget. Decide whether users supply training code or only approved recipes. Which generalization axes must remain held out, and what operational evidence is required before a checkpoint is eligible for separate deployment review?
