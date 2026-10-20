# Figure AI Index: Human-video data platform

Published-system-inspired exercise; not a verified interview prompt.

## References

- [Figure: Introducing Index](https://www.figure.ai/news/introducing-index)

## Published System Context

Figure describes Index as a creator app and pipeline collecting human activity videos for Helix training. Its published processing stages include filtering, fraud review, deduplication, rebalancing, and hierarchical episode captioning. Figure also describes continuous processing and feedback to contributors. The source does not disclose its complete backend architecture.

## Problem Statement

Design the backend for a similar collection platform serving contributors, data operations staff, and training researchers. For this exercise, assume the submitted footage is first-person video. Contributors need dependable uploads and useful feedback; researchers need searchable, traceable training datasets. Design the platform supporting these workflows, not the learning model or a replica of Figure's private infrastructure.

All requirements below are proposed exercise scope, not claims about Index.

## Functional Requirements

- Let contributors register recording sessions, submit video and task metadata, recover interrupted submissions, and inspect acceptance or rejection status.
- Let operations staff define collection tasks and eligibility rules, inspect processing failures, and provide actionable feedback without exposing restricted footage.
- Support technical and semantic assessment, duplicate detection, diversity selection, and caption generation as configurable processing capabilities. Retain the decisions and versions behind each result.
- Let researchers find eligible clips by task, object, environment, collection period, and available annotations, with previews and source provenance.
- Create reproducible dataset releases whose selected clips, captions, transformations, and inclusion criteria can be inspected and consumed by distributed training jobs.
- Handle corrections, consent withdrawal, and authorized deletion across recordings, derived artifacts, search results, and affected dataset releases.
- Expose interfaces for submission, processing status, search, and dataset export; preserve meaningful progress when processing fails or work is repeated.

## Non-Functional Requirements

Proposed exercise assumptions, not Figure's reported service guarantees:

- Accepted recordings and release histories must remain durable under ordinary worker failures.
- Upload bursts and expensive processing must not make contributor status unavailable.
- Dataset consumers must distinguish complete releases from unfinished work.
- Access restrictions and deletion obligations must apply to derived data as well as originals.
- Processing delay, retained coverage, failure rates, and cost must be measurable.

## Requirements to Clarify

Agree on upload volume, clip sizes, geographic constraints, feedback latency, retention periods, and concurrent training-reader throughput. Decide which collection restrictions are mandatory and whether creator compensation is outside scope. Choose explicit availability and recovery targets before designing capacity.
