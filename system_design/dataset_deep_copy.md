# Dataset deep-copy API

## Core prompt

Design an API to copy a relational dataset, its tasks, model responses, and
grades. Assign fresh IDs and rewrite internal references. Edits to the copy
must not affect the source, or vice versa.

Contrast a small atomic copy with a large background operation.

## Design questions

- Define request, response, authorization, status, progress, and error contracts.
- Which records and external resources belong to the copy?
- What snapshot semantics apply during concurrent source edits or deletion?
- How are old-to-new ID mappings and batch checkpoints persisted?
- How are repeated requests distinguished from intentional additional copies?
- How do leases and ownership checks prevent conflicting or stale workers?
- When is a partial destination visible, editable, or declared complete?
- How do failures, cancellation, reconciliation, and cleanup interact?
- What limits and monitoring protect the database?

## Validation

Trace a worker crash between writing rows and saving its checkpoint, overlapping
workers after lease expiry, a lost client response, source mutation, and
interrupted cleanup.

Show durable state and caller-visible results. Check uniqueness,
reference integrity, source independence, and completion invariants.

## Related exercises

- [Workflow orchestration](workflow_orchestration.md)
- [Payment integration](payment_integration.md)
