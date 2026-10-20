"""Find a connection using a constrained social-graph API.

Problem
    Search a friend network while minimizing API calls. The goal, API contract,
    and restrictions must be specified before choosing a search algorithm.

Explicit starter version
    Find any directed path from start to target; shortest-path optimality is
    not required. The graph is finite and unchanged during one search. The
    API lists outgoing neighbors in pages with opaque cursors; a None next
    cursor ends pagination. There is no reverse-neighbor endpoint. Identifiers
    are strings. The caller supplies a nonnegative API-call budget. start equal
    to target has the zero-edge path. API calls, not in-memory operations, are
    the constrained resource. Rate limits, batching, and retries are additional
    policies to define if the real API supports or requires them.

Separate variant
    social_graph_neighborhood.py collects all nodes within a friendship
    distance using a mutual graph and a complete-neighbor-list API.

TODO
    Implement search without exceeding max_calls. Distinguish proven absence
    of a path from an incomplete budget-limited search. Avoid repeated page
    fetches and cycle loops. Test pagination, disconnected graphs, cycles,
    duplicate neighbors, zero budget, start equal to target, and failed calls.
    Compare breadth-first search with bidirectional search only for an API
    variant that actually exposes the directions needed by the latter.
"""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class NeighborPage:
    people: tuple[str, ...]
    next_cursor: str | None = None


class SocialGraphAPI(Protocol):
    def neighbors(self, person: str, cursor: str | None = None) -> NeighborPage:
        """Fetch one page of outgoing neighbors for a person."""
        ...


@dataclass(frozen=True)
class SearchResult:
    path: tuple[str, ...] | None
    # True means a path was found or exhaustive search proved no path exists.
    complete: bool
    api_calls: int


def find_connection(
    api: SocialGraphAPI, start: str, target: str, *, max_calls: int
) -> SearchResult:
    """Return a path or an explicit complete/incomplete no-path outcome."""
    # TODO: Define failed-call accounting and implement budget-aware traversal.
    raise NotImplementedError


if __name__ == "__main__":
    print("TODO: implement a fake paginated API, search, and call-budget tests.")
