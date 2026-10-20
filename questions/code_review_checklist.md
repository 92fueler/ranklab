# Code-review checklist

Apply this checklist to a supplied function or small module. No particular code
snippet or defect is assumed.

## Intended behavior

- What should the code do?
- What are the input and output contracts?
- Which invariants must always hold?
- What assumptions are implicit or missing?

## Correctness

- Do ordinary inputs produce the intended result?
- Are empty, boundary, invalid, duplicate, and missing inputs handled?
- Are ordering, equality, and numeric behavior appropriate?
- Can a plausible counterexample disprove the current implementation?

## Failure modes

- What can fail before, during, or after an external effect?
- Are exceptions handled without losing necessary context?
- Can retries duplicate work or cause inconsistent state?
- Does the caller distinguish a confirmed failure from an unknown outcome?

## Resource use

- What are the time and space costs?
- Can storage, cache size, queues, or output grow without a bound?
- Are resources released when an operation fails?
- Is there avoidable repeated work or copying?

## Concurrency

- Which state is shared?
- Are updates atomic where required?
- Are thread safety, duplicate in-flight work, and idempotency treated separately?
- Could locking create contention or deadlocks?

## Tests and smallest useful fix

- Write a focused test that demonstrates each important defect.
- Prioritize correctness and consequential failure modes over cosmetic changes.
- Propose the smallest change that restores the intended invariant.
- Add regression coverage and explain any remaining limitation.
- Separate confirmed defects from risks that depend on unstated requirements.

## Related exercises

- [Interrupted external payment](../debugging/interrupted_payment.py) provides a concrete failure-window exercise.
- [Technical communication and validation](technical_communication.md) covers explaining assumptions, evidence, and trade-offs.
