# Mercor – Event-ticketing platform (reported system-design topic)

## References

- [Mercor report collection](mercor_system_design_reports.md): user-supplied report; original public URL unavailable.
- [Related payment-integration exercise](payment_integration.md).

## Evidence status

A supplied report names event ticketing as a system-design topic for a marketplace-oriented role. It does not provide detailed purchase rules, traffic figures, or a complete prompt. Every expanded requirement below is an original practice assumption, not a confirmed requirement from the reported interview.

## Problem statement

Design a platform where customers discover an event, select available tickets, and complete a purchase. Choose reserved seats or general-admission quantities before designing the system; neither model is established by the report.

## Functional requirements

For the proposed exercise:

- Show events, ticket categories, prices, and current purchase availability.
- Let customers select tickets and learn whether their purchase succeeded.
- Prevent confirmed sales from exceeding the selected inventory.
- Define whether selections temporarily reserve inventory and when any reservation expires.
- Handle repeated checkout attempts and uncertain payment outcomes without silently creating additional purchases.
- Make purchased tickets retrievable by their authorized owner.
- Define what happens when payment completes after inventory is no longer available.

Refunds, cancellation, resale, transfer, and admission scanning are optional extensions, not assumed features.

## Non-functional requirements

Choose targets for peak demand, response latency, availability, and recovery. Also clarify:

- Inventory correctness during concurrent purchases.
- Acceptable freshness of displayed availability versus checkout decisions.
- Fair access during demand spikes and limits on abusive requests.
- Protection of customer information and traceability of purchase outcomes.
- Maximum time an unresolved purchase may remain pending.

No numerical service targets were reported.

## Optional failure conditions

Two customers request the last ticket; a hold expires during checkout; payment succeeds but no ticket is visible; a successful response is lost; demand suddenly exceeds capacity. State what customers should observe and which business outcomes are permitted, without selecting an implementation.
