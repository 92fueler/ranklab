"""Select top-k items with a persistently unreliable comparator.

Problem
    A comparator has a stated 10% error rate. An erroneous comparison remains
    erroneous when the same pair is compared again. Find the top k among n
    items, while considering both comparator-call count and elapsed time when
    a call takes approximately five seconds.

Open decisions
    A 10% error rate alone does not define a probability model: specify how
    corrupted pairs are selected and whether they are independent. Specify
    whether exact recovery is required, what approximation is acceptable, and
    whether any evidence besides comparisons is available. Do not promise exact
    recovery from arbitrary deterministic inconsistencies. Repeated votes on
    one pair do not remove that pair's persistent error.

Starter API choices
    Items have distinct string identifiers. compare(left, right) returns -1
    when left is worse, 1 when left is better, and 0 for a tie. Calls are
    deterministic per ordered pair. Any assumed symmetry between reversed
    pairs must be stated in the implementation's error model. k must satisfy
    0 <= k <= len(items). The result orders its selected items best first;
    its docstring must state the quality guarantee, if any.

TODO
    Choose and document an error model and algorithm. Consider cached pair
    results, different opponents, tournament/ranking heuristics, and bounded
    concurrency for independent calls. Measure call count, wall time, and
    ranking quality separately using synthetic true orders and fixed corrupted
    pairs. A fake clock or short configurable delay can replace real five-second
    sleeps in tests. Cover k = 0, k = n, invalid k, duplicates, ties, and cycles
    in the comparison relation.
"""

from collections.abc import Sequence
from typing import Literal, Protocol

Comparison = Literal[-1, 0, 1]


class Comparator(Protocol):
    def compare(self, left: str, right: str) -> Comparison:
        """Return a possibly incorrect, persistent pair comparison."""
        ...


def select_top_k(
    items: Sequence[str], k: int, comparator: Comparator
) -> list[str]:
    """TODO: state the algorithm's assumptions and achievable result quality."""
    # TODO: Implement the chosen strategy; repeated identical votes are not a fix.
    raise NotImplementedError


if __name__ == "__main__":
    print("TODO: define the error model, implement selection, and measure quality.")
