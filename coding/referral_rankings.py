"""Return the top k people by referral reach and a defined flow score.

Problem
    Rank people by direct and indirect referral reach. Also rank people by a
    flow concept: how often a person appears on paths through the network.

Starter choices and open decisions
    Use string identifiers and a directed adjacency mapping. Include isolated
    nodes as keys and require every neighbor to have its own key. Reach counts
    unique reachable people, not paths, and excludes the starting person even
    when a cycle returns to it. Break score ties by ascending identifier.
    k must be nonnegative; k = 0 yields an empty list and k larger than the
    network size returns every person.

    Flow is deliberately NOT defined as standard betweenness centrality. Before
    implementing a FlowScorer, write down which paths qualify (shortest, simple,
    or another finite family), endpoint inclusion, weighting, normalization,
    and cycle handling. Include a worked example with expected scores. A walk
    definition on a cyclic graph may require a length bound to be finite.

TODO
    Implement both rankings and a separately specified flow scorer. State the
    complexity of score calculation and top-k selection. Explain caching and
    invalidation under graph updates. Test overlapping descendants, isolated
    nodes, cycles, invalid k, ties, and incomplete or non-finite flow scores.
"""

from collections.abc import Collection, Mapping
from typing import Protocol

Graph = Mapping[str, Collection[str]]


class FlowScorer(Protocol):
    """Implementations must document a complete, finite path-scoring policy."""

    def __call__(self, graph: Graph) -> Mapping[str, float]:
        """Return one finite score for every graph node."""
        ...


def top_k_by_reach(graph: Graph, k: int) -> list[tuple[str, int]]:
    """Return (identifier, unique-reach count), highest score first."""
    # TODO: Validate, compute cycle-safe unique reach, and select deterministically.
    raise NotImplementedError


def top_k_by_flow(
    graph: Graph, k: int, scorer: FlowScorer
) -> list[tuple[str, float]]:
    """Rank using an explicitly specified scorer; no path policy is implied."""
    # TODO: Validate the graph, k, and scorer output before selecting results.
    raise NotImplementedError


if __name__ == "__main__":
    print("TODO: specify flow semantics, implement rankings, and add tests.")
