# Atomic membership and insertion

## Core prompt

Design a service holding roughly one million identifiers. Atomically check
whether an identifier exists and insert it if absent. Define each caller's
result when requests for the same identifier overlap.

Compare exact membership with a lower-memory approximation. Explain whether a
false positive could incorrectly reject a genuinely new identifier.

## Questions to resolve

Identifier format, traffic, latency targets, growth, and durability are
unspecified. Establish them before selecting storage.

- What is the realistic memory footprint, including representation, indexing,
  allocation overhead, and spare capacity?
- Where is the check-and-insert atomicity boundary?
- How does correctness change with multiple application servers?
- If approximate membership is used, what error rate is acceptable, and how
  are uncertain decisions checked?
- What survives a restart, and how is persisted state recovered?
- How do partitioning, rebalancing, and deletion affect membership?

## Additional engineering choices

Define behavior for these optional extensions:

- Two servers insert the same absent identifier concurrently.
- A caller times out after an insertion may have committed.
- A partition moves while requests remain in flight.
- An identifier is deleted and immediately inserted again.

