# Reliable payment integration

## Core prompt

Design an integration with an external payment provider. Address:

- Error handling, retries, and idempotency.
- The data that must be stored.
- Database selection, including transaction guarantees and availability.

## Questions to resolve

- Which payment operations are in scope: charge, authorize, capture, refund, or others?
- What idempotency and status-query capabilities does the provider expose?
- How are provider events authenticated, deduplicated, and ordered?
- What request identity does the caller preserve across retries?
- What consistency, availability, audit, and retention requirements apply?

## Optional design directions

Define a durable operation identifier and an explicit state model. Possible
states include pending, succeeded, failed, and unresolved; adapt the model to the
provider's actual contract.

Consider storing the operation identifier, relevant request attributes,
provider identifiers, status, attempt history, timestamps, and reconciliation
information. Decide what is necessary without storing unnecessary payment
credentials or sensitive data.

Explain:

1. Which errors are retryable and which have an unknown outcome.
2. How retries preserve provider-supported idempotency semantics.
3. What happens if the same identifier is reused with different request contents.
4. How reconciliation uses status queries or verified provider events.
5. How audit records support investigation without exposing secrets.
6. Which database access patterns and correctness requirements drive the choice.

A local database transaction cannot, by itself, make an unrelated external
charge atomic. Identify this boundary explicitly and explain recovery rather
than promising an unsupported guarantee.

## Failure-window analysis

Trace the sequence: request received, provider called, local result stored,
response returned.

- The process stops before calling the provider.
- The provider succeeds but its response is lost.
- The provider succeeds but the local database write fails.
- The database write succeeds but the client never receives the response.
- A duplicate request or repeated provider event arrives.

For each case, state what is known, what remains uncertain, what may safely be
retried, and how the system reaches a resolved outcome. A timeout is not proof
that the payment failed.

## Related exercises

- [Interrupted external payment](../debugging/interrupted_payment.py) turns the failure-window analysis into a debugging exercise.
- [Event-ticketing platform](event_ticketing.md) combines payment with limited inventory.
- [Workflow orchestration](workflow_orchestration.md) explores durable execution and retries.
