# Technical communication and validation

Use these questions when documenting an implementation, design, or experiment.

## Define the problem

- What behavior is required, and what is outside the scope?
- Which inputs, outputs, invariants, and failure cases matter?
- Which statements are requirements, and which are assumptions or design choices?
- What missing information could change the solution?

## Explain the design

- What is the simplest solution that satisfies the chosen scope?
- Why was this approach selected over a credible alternative?
- Which trade-offs affect correctness, complexity, latency, cost, or maintainability?
- Where do consistency, recovery, or execution guarantees stop?
- What evidence would justify revisiting the design?

Be concise, but preserve distinctions that affect correctness. For example,
thread-safe cache access is different from preventing duplicate in-flight
computations, and a timeout is different from a confirmed failed payment.

## Validate the implementation

- Which tests demonstrate ordinary behavior, boundaries, and failure recovery?
- Which properties or invariants can be checked independently?
- Are complexity claims consistent with the operations actually performed?
- What did measurements reveal, and which hypotheses remain untested?
- Can another person reproduce the result with the documented inputs and configuration?

## Validate generated contributions

When a model or code generator contributes to the work:

- Distinguish the intended requirements from suggestions produced by the tool.
- Inspect generated code and explain its behavior.
- Check dependencies, interfaces, edge cases, and security assumptions.
- Test outputs independently instead of treating successful execution as proof of correctness.
- Record which changes improved measured behavior and which did not.

## Useful summary structure

1. Problem and explicit assumptions.
2. Chosen approach and alternatives considered.
3. Correctness argument or key invariants.
4. Tests, measurements, and observed limitations.
5. Remaining uncertainty and the next useful validation step.

## Related exercises

- [Code-review checklist](code_review_checklist.md) turns these questions into a focused review.
- [Reliable payment integration](../system_design/payment_integration.md) requires careful statements about uncertain outcomes.
- [End-to-end candidate search](../ai_projects/candidate_search.md) uses experiment logs to connect changes to evidence.
