# Mercor – Dataset deep-copy API (reported technical-screen design question)

## References

- [Public candidate account](https://prachub.com/interview-experiences/mercor-software-engineer-interview-experience-half-hour-online-round-of-code-review-and-design-questions).
- [Expanded public practice question](https://prachub.com/interview-questions/design-an-api-to-deep-copy-a-dataset-with-its-tasks-model-responses-and-grades).

## Evidence status

The public edited account supports copying a dataset hierarchy and discussing larger, recoverable operations. The practice page supplies a fuller formulation. These are third-party reports, not an official specification. Core copy semantics are source-supported; the operational targets and unresolved product choices below remain exercise assumptions.

## Problem statement

Design an API that copies a relational dataset, its tasks, model responses, and grades. The destination must have independent identities and internal relationships so that later edits to either dataset do not alter the other.

## Functional requirements

- Create a copy with fresh identifiers and valid references within the copied hierarchy.
- Handle a small copy and a larger operation that cannot finish during one request.
- Expose progress and a clear completion or failure outcome for long-running copies.
- Resume interrupted work without corrupting or duplicating the destination.
- Distinguish a retried request from an intentional request for another copy.
- Define what users can see while copying is incomplete.
- Specify which source version is copied if edits occur concurrently.

Clarify authorization, ownership, external file references, and whether related users or rubrics are shared or copied. Cancellation is an optional extension.

## Non-functional requirements

Proposed constraints to establish:

- Maximum hierarchy size, copy frequency, completion time, and database workload budget.
- Reference integrity and source/destination independence throughout recovery.
- Recovery time, retained progress, and acceptable impact on other users.
- Access control and visibility into failed or abandoned copies.

## Optional failure conditions

A response is lost after a copy starts; two workers overlap; a worker restarts after partial progress; source records change; cleanup is interrupted. Define the required observable outcome without prescribing coordination or persistence mechanisms.
