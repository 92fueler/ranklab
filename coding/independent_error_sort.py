"""Fully order hidden-valued items using an independently noisy paid comparator.

Problem
    Order distinct-valued items using only a comparator that is correct on
    90% of calls. Each invocation costs one cent. Analyze total calls, price,
    and the probability that the entire output order is correct.

Explicit variant choices
    Errors are independent across invocations, including repeated comparisons
    of the same pair. Items have unique string identifiers and no true ties.
    compare(left, right) returns -1 if left is smaller and 1 otherwise, subject
    to error. Return identifiers in ascending hidden-value order. The requested
    whole-order success probability satisfies 0 < target_success < 1.

TODO
    Implement a strategy, justify its reliability bound, and report actual
    call count. Explain how cost changes with input size and target success.
    Do not assume an adaptive algorithm has a fixed number of calls or that
    every erroneous call necessarily causes an incorrect final order.
    Test empty/singleton inputs, duplicate identifiers, and seeded noisy fakes.
    Empirical success rates complement, but do not replace, the analysis.

Separate variant
    unreliable_comparator.py has persistent pair errors and a top-k goal.
    Repeating comparisons there does not provide independent evidence.
"""

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal, Protocol

COST_PER_CALL_CENTS = 1


class IndependentComparator(Protocol):
    def compare(self, left: str, right: str) -> Literal[-1, 1]:
        """Return an independently noisy comparison."""
        ...


@dataclass(frozen=True)
class SortResult:
    ordered_items: tuple[str, ...]
    comparator_calls: int


def sort_with_noisy_comparisons(
    items: Sequence[str],
    comparator: IndependentComparator,
    *,
    target_success: float,
) -> SortResult:
    """TODO: state and justify the achievable whole-order reliability."""
    # TODO: Implement the strategy and account for every paid invocation.
    raise NotImplementedError


if __name__ == "__main__":
    print("TODO: implement independent-error sorting and cost/reliability tests.")
