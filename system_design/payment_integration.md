# Mercor – Reliable payment integration (code-review and design discussion)

## References

- [Mercor report collection](mercor_system_design_reports.md): user-supplied reports; original public URLs unavailable.
- [Related public technical-screen report](https://prachub.com/interview-experiences/mercor-software-engineer-interview-experience-technical-screen-with-bloom-filter-and-payment-idempotency-debugging).
- [Expanded charge-then-record exercise](https://prachub.com/interview-questions/make-a-charge-then-record-payment-endpoint-safe-against-timeouts-retries-and-crashes).

## Evidence status

Supplied reports describe payment-provider integration, retries, error handling, idempotency, stored data, and database guarantees within a technical screen. Another describes reviewing a charge followed by a database write. These do not establish a standalone system-design round. Expanded behaviors below are practice assumptions; reported candidate solutions are not mandatory architecture.

## Problem statement

Design an integration that submits a payment operation to an external provider and gives the caller a trustworthy outcome, including when requests, responses, or local persistence fail. Use a simulated provider for the exercise, not real payments.

## Functional requirements

For this practice version:

- Accept a payment request and let the caller inspect its outcome.
- Distinguish confirmed success, confirmed failure, and an outcome that remains unknown.
- Handle repeated submissions of the same intended operation without unintended repeated charges.
- Detect conflicting request contents when the caller claims they represent the same operation.
- Resolve uncertain results using only capabilities the provider actually supports.
- Retain enough history to investigate discrepancies and explain the caller-visible result.

Clarify whether charges, authorizations, captures, or refunds are in scope and what guarantees the provider offers.

## Non-functional requirements

Choose availability, response-time, recovery, throughput, and retention targets. Require auditable outcomes and minimal exposure of financial information. Define the acceptable time to resolve uncertainty and distinguish local consistency from external-provider guarantees. None of these numerical targets is supplied by the reports.

## Optional failure conditions

The provider succeeds but its response is lost; local recording fails; the caller retries after success; duplicate provider notifications arrive; provider deduplication expires. Specify acceptable business outcomes without assuming an implementation can guarantee exactly-once effects.
