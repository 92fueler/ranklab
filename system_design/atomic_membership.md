# Mercor – Atomic membership and insertion (technical-screen design discussion)

## References

- [Public candidate report](https://prachub.com/interview-experiences/mercor-software-engineer-interview-experience-technical-screen-with-bloom-filter-and-payment-idempotency-debugging).
- [Expanded public practice question](https://prachub.com/interview-questions/check-and-insert-for-a-million-user-ids-balancing-latency-memory-and-accuracy).

## Evidence status

The edited candidate report describes checking and adding approximately one million identifiers, with latency, memory, and accuracy trade-offs. This was a technical-screen discussion alongside code review, not a verified standalone system-design round. The candidate's implementation choices are not requirements. The exercise below adds explicit behavioral assumptions; unspecified scale and service targets remain yours to choose.

## Problem statement

Design a service that tells a caller whether an identifier was already present and adds it when absent. Explore how the contract changes as memory becomes constrained, requests overlap, and the collection grows.

## Functional requirements

For this practice version:

- Accept an identifier and return whether this operation inserted it or found it already present.
- Treat concurrent check-and-insert requests consistently: only one request may report inserting the same previously absent identifier.
- Define invalid identifier handling and the result of retrying after a lost response.
- Specify whether accepted insertions survive restarts.
- If approximate answers are allowed, identify the permitted error direction and its effect on admitting a new identifier.
- Treat deletion and multiple service instances as optional extensions, with explicit behavior.

## Non-functional requirements

Proposed constraints to clarify, not reported targets:

- Identifier representation, expected growth, request rate, and read/write mix.
- Memory budget, tail-latency objective, availability, and recovery time.
- Exactness requirements and any acceptable error probability.
- Operational visibility into rejected requests, resource consumption, and recovery.

## Optional failure conditions

Consider overlapping inserts, a timeout after acceptance, a restart during an insertion, and deletion concurrent with reinsertion. Describe expected outcomes without assuming a particular data structure or storage engine.
