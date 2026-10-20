# Figure AI Index: Annotation quality-control platform

Published-system-inspired exercise; not a verified interview prompt.

## References

- [Figure: Introducing Index](https://www.figure.ai/news/introducing-index)

## Published System Context

Figure says Index produces hierarchical text captions for episodes after filtering, fraud review, deduplication, and rebalancing. Human analysts audit contributor samples for fraud. The article does not specify a human annotation assignment, adjudication, or quality-control platform; the review workflow below is an inferred exercise opportunity, not a reported implementation.

## Problem Statement

Design an annotation operations backend for a human-video collection platform. Assume automatic captioning produces drafts that authorized annotators and reviewers may inspect and correct. Data operations managers need to manage the workload and measure quality, while training researchers need reliable annotation releases. Contributor fraud review and annotation correctness are separate concerns.

All requirements below are proposed exercise scope, not claims about Index.

## Functional Requirements

- Import eligible episodes and proposed captions while retaining their source time ranges, generating-model version, and applicable annotation instructions.
- Let managers define annotation projects, label structures, reviewer eligibility, and acceptance criteria; support episode summaries and time-local descriptions.
- Let annotators obtain work, save progress, submit corrections, and return incomplete tasks. Define the result when a late submission conflicts with reassigned or revised work.
- Let reviewers approve, reject, or escalate annotations and resolve disagreements without losing earlier submissions or the reasons for decisions.
- Measure quality by task and annotation category against agreed evaluation criteria. Surface ambiguous instructions and systematic errors rather than treating agreement alone as correctness.
- Publish approved annotation releases for dataset builders and training consumers. Preserve which source, instructions, model, human edits, and approval produced each included label.
- Support targeted re-review after a captioning-model change, schema correction, or discovered quality issue; identify affected releases and notify their owners within the exercise platform.
- Expose interfaces for project administration, work submission, review status, quality reporting, and release retrieval.

## Non-Functional Requirements

Proposed exercise assumptions, not Figure's reported service guarantees:

- Completed work and review history must survive routine service failures.
- Concurrent edits and retried submissions must not silently overwrite accepted decisions.
- Annotators may access only the footage needed for their authorized work.
- Quality reports must distinguish reviewed evidence from estimated quality.
- Growing review backlogs must be visible before release deadlines are missed.

## Requirements to Clarify

Agree on annotation languages, task duration, reviewer capacity, quality thresholds, sensitive-content handling, and release cadence. Decide whether independent labels, specialist review, or appeals are required. Establish latency and recovery targets without assuming Figure's staffing or volumes.
