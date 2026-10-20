"""Collect people within friendship distance k using few API calls.

Problem
    Friendships are mutual. Return all people at graph distance at most k
    from origin, including origin, using a neighbors API.

Explicit starter choices
    The finite graph stays unchanged; origin is valid. One neighbors(person)
    call returns the complete neighbor list, possibly with duplicates.
    Pagination, batching, rate limits, and hard budgets are not assumed.
    API errors propagate instead of yielding an apparently complete partial
    result. Negative k raises ValueError; k = 0 needs no API calls.

Boundary
    Return the node set and API-call count. For node collection, do not expand
    people whose shortest distance is k. This is not the induced subgraph:
    edges between boundary people can remain unknown.

TODO
    Avoid repeated fetches and cycle loops. Test isolation, disconnected nodes,
    duplicates, multiple routes, k = 0, and invalid k with a fake API.

Optional discussion
    Compare call lower bounds under pagination, shared budgets, caching,
    rate limits, high-degree nodes, failures, and graph updates. Complete
    induced-edge collection is a separate goal.

Separate variant
    social_graph_connection.py searches for a path using a directed,
    paginated API with a hard call budget.
"""

from dataclasses import dataclass
from typing import Protocol


class FriendshipAPI(Protocol):
    def neighbors(self, person: str) -> tuple[str, ...]:
        """Return all neighbors in one API call."""
        ...


@dataclass(frozen=True)
class NeighborhoodResult:
    people: frozenset[str]
    api_calls: int


def collect_neighborhood(
    api: FriendshipAPI, origin: str, k: int
) -> NeighborhoodResult:
    """Return the complete radius-k node set and API-call count."""
    # TODO: Validate k and implement collection.
    raise NotImplementedError


if __name__ == "__main__":
    print("TODO: implement neighborhood collection and call-accounting tests.")
