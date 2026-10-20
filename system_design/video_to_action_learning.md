# 1X World Model: Video-to-action learning platform

Published-system-inspired exercise; not a verified interview prompt.

## References

- [1X: From Video to Action](https://www.1x.tech/discover/world-model-self-learning)

## Published System Context

1X describes a world model generating future video from a text prompt and starting frame, then a separate inverse-dynamics model (IDM) deriving robot actions. World-model adaptation uses selected robot demonstrations; IDM training includes broader, unfiltered motions. The published setup uses video as a plan, not an action-conditioned forward simulator.

## Problem Statement

Design a research backend supporting this two-model workflow. Researchers need to curate the models' different training inputs, run distributed training experiments, generate candidate video plans, derive action trajectories, and evaluate the resulting artifacts. Treat both model implementations as supplied components. Physical robot execution requires a separate authorized evaluation workflow.

All requirements below are proposed exercise scope, not claims about 1X's infrastructure.

## Functional Requirements

- Register human-video and robot-recording collections with captions, timestamps, available state/action labels, embodiment metadata, and provenance.
- Let researchers create independently versioned world-model and IDM training datasets with different eligibility criteria; do not assume one filter is correct for both objectives.
- Submit, monitor, cancel, and recover distributed training runs while linking resulting checkpoints to data, configuration, and model-component versions.
- Accept generation requests containing a prompt, initial frame, embodiment, and selected world-model checkpoint. Return candidate future-video artifacts and explicit generation status.
- Accept a selected video artifact for action inference with a compatible IDM checkpoint; persist the derived trajectory and its relationship to the source frames.
- Evaluate task adherence, generated-video limitations, action compatibility, and available held-out trajectory evidence. Keep visual plausibility separate from successful physical execution.
- Compare model pairs and dataset revisions, including rejected candidates, failed stages, and later authorized hardware outcomes.
- Expose dataset, training-run, generation, trajectory-retrieval, and evaluation interfaces. Preserve the outcome of repeated requests without unexpectedly duplicating expensive work.

## Non-Functional Requirements

Proposed exercise assumptions, not 1X's reported service guarantees:

- Every trajectory must remain traceable to both model versions and the originating generation request.
- Missing or incompatible action labels must not silently enter IDM training.
- Partial pipeline failures must not appear as completed, validated plans.
- Parallel experiments must respect compute budgets and restricted recording access.
- Published datasets and evaluation artifacts must remain reproducible at the agreed level.

## Requirements to Clarify

Set video duration, action horizon, dataset sizes, accelerator capacity, and interactive versus batch latency. Which candidate checks block action inference versus only flag review? Define the evidence and authorization required before hardware evaluation, plus retention and recovery targets.
