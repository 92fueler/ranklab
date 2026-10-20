# Event-ticketing platform

## Core prompt

Design an event-ticketing platform.

The initial prompt does not prescribe reserved seating, general admission,
payment methods, traffic volume, or purchase rules. Choose and document a scope
before treating any of the following as requirements.

## Questions to resolve

- Is inventory allocated to individual seats, ticket categories, or both?
- What is the purchase journey from event discovery to confirmed ticket?
- Are temporary holds needed? If so, how long do they last?
- What happens when payment finishes after a hold expires?
- Can tickets be cancelled, refunded, or transferred?
- What peak demand, latency, and availability targets apply?

## Optional design directions

For a reserved-seat implementation, consider inventory, seat selection,
temporary holds, checkout, and hold expiration.

- How do concurrent requests avoid selling the same seat twice?
- What data model and transaction boundary protect inventory?
- How are hold ownership and expiration enforced?
- How do duplicate checkout requests behave?
- How are payment outcomes reconciled with ticket issuance?
- How do traffic spikes, queues, admission control, and backpressure affect users?
- Which failures can be recovered automatically, and which need manual resolution?

If selecting general admission instead, explain how the design changes when
protecting a quantity rather than a particular seat.

## Validation scenarios

Choose scenarios appropriate to the selected product:

1. Two users attempt to hold the same seat simultaneously.
2. A hold expires while checkout is running.
3. Payment succeeds but ticket issuance fails.
4. The client loses the successful checkout response and retries.
5. A major event creates a sudden spike in demand.

For each scenario, identify authoritative state, consistency requirements, and
the recovery path.

## Related exercises

- [Reliable payment integration](payment_integration.md) focuses on payment outcomes and reconciliation.
- [Interrupted external payment](../debugging/interrupted_payment.py) examines concrete failure windows.
- [Workflow orchestration](workflow_orchestration.md) covers coordinating durable multi-step work.
