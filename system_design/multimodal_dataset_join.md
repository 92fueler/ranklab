# NVIDIA GR00T N1: Aligned episode data service

Published-system-inspired exercise; not a verified interview prompt.

## References

- [NVIDIA: GR00T N1 technical report, Appendix D.1](https://arxiv.org/html/2503.14734v1)

## Published System Context

GR00T N1's report describes episode data using MP4 video, Parquet states and actions, and JSON metadata, with synchronized observations and actions and explicit modality semantics. The model combines vision-language processing with a flow-matching action module. This exercise focuses on the backend supplying aligned training examples, not the model architecture.

## Problem Statement

Design a dataset service that joins camera observations, robot state, commands, and task annotations into training episodes across multiple robot types. Collection tools may deliver components at different times, and clocks or metadata may later be corrected. Researchers need usable examples and explicit evidence of missing or uncertain alignment.

All requirements below are proposed exercise scope, not claims about NVIDIA's internal services.

## Functional Requirements

- Accept episode registrations and independently arriving video, state/action records, and metadata. Report missing components and incompatible schemas before release.
- Preserve robot identity, modality definitions, units, coordinate conventions, calibration references, and the meaning of each timestamp.
- Let researchers specify an alignment request and inspect whether each resulting observation was available at the policy's decision time. Distinguish observation inputs from future action targets.
- Represent dropped frames, sensor gaps, uncertain timing, and absent modalities explicitly; missing measurements must not become valid zero-valued observations.
- Support training examples with selected camera views, instruction labels, and action horizons. Reject or clearly mark examples that do not satisfy the requested contract.
- Publish versioned episode collections and quality summaries for distributed training readers, including source references and the alignment decisions behind each example.
- Allow corrected clocks, calibrations, or labels to produce revised outputs and identify affected experiments without silently modifying a released dataset.
- Expose interfaces to submit alignment jobs, inspect failures, retrieve sample previews, and obtain complete dataset releases.

## Non-Functional Requirements

Proposed exercise assumptions, not NVIDIA's reported service guarantees:

- Alignment errors must be observable rather than hidden behind syntactically valid tensors.
- Readers must receive a consistent release even while new components arrive.
- Routine worker failures must not lose accepted inputs or corrupt published episodes.
- Processing cost and read throughput must support the agreed episode volume and training concurrency.
- Related demonstrations must obey the experiment's train/evaluation separation rules.

## Requirements to Clarify

Agree on sensor rates, timing uncertainty, acceptable staleness, episode completeness, and action semantics. Which consumers need causal observations versus offline reconstruction? Decide how late corrections affect existing training runs. Select measurable throughput, recovery, and alignment-quality targets before choosing an implementation.
