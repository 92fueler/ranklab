# NVIDIA Cosmos: Video curation and sampling platform

Published-system-inspired exercise; not a verified interview prompt.

## References

- [NVIDIA Cosmos Cookbook: Data Curation](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/data_curation/overview.html)

## Published System Context

NVIDIA's Cosmos documentation describes video splitting, transcoding, cropping, filtering, captioning, deduplication, and structured sharding. It distinguishes broad pretraining curation from targeted post-training datasets and emphasizes domain coverage, quality, and provenance. These published capabilities motivate the exercise; their described implementation is not a required backend design.

## Problem Statement

Design a curation service that lets data engineers and researchers turn heterogeneous video collections into training-ready datasets. A researcher should compare alternative selection policies, inspect what each retains or excludes, and release a dataset for distributed model training. The exercise concerns data-processing operations and dataset delivery, not inventing a video-generation model.

All requirements below are proposed exercise scope, not claims about Cosmos deployments.

## Functional Requirements

- Register source collections with media references, metadata, usage restrictions, and the intended training domain. Report unreadable or incomplete inputs.
- Let researchers define and version curation requests covering clip boundaries, transformations, quality criteria, captions, duplicate handling, and desired coverage.
- Submit, inspect, cancel, and retry processing jobs. Make the outcome of repeated submissions and partially completed work understandable to callers.
- Provide previews and sampled review sets for accepted and rejected clips, with the reasons and source evidence behind each decision.
- Compare candidate datasets by retained duration, domain composition, rare-event coverage, label quality, and processing cost. Preserve unsuccessful or unusual behavior when the selected objective requires it.
- Publish complete dataset releases containing media, annotations, selection decisions, and lineage that distributed training readers can consume consistently.
- Allow later policy revisions or source corrections to create new releases and identify affected prior outputs without silently changing a running experiment's inputs.
- Expose collection-registration, job-control, preview, comparison, and release-retrieval interfaces; retain durable records linking these operations.

## Non-Functional Requirements

Proposed exercise assumptions, not NVIDIA's reported service guarantees:

- Processing must tolerate individual media failures without misreporting the entire collection as successful.
- Interactive inspection must remain usable during large processing runs.
- Release construction and training access must scale to the workload agreed for the exercise.
- Results must remain traceable to their sources and policy versions.
- Resource consumption and unsuccessful work must be attributable to a request.

## Requirements to Clarify

Set source volume, daily arrivals, supported codecs, quality-review budget, release deadline, and training-reader throughput. Define what counts as a harmful duplicate and which rare events must survive selection. Decide which transforms preserve required temporal evidence and how retention restrictions affect reproducibility.
