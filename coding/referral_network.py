"""Model a directed referral network.

Problem
    Record who referred whom. Support creating people and inserting referrals,
    then expose the network for traversal and ranking.

Starter choices, not fixed domain requirements
    Person identifiers are nonempty strings. An edge points from the referrer
    to the referred person. Multiple referrers and cycles are allowed, but
    self-referrals are rejected. Adding an existing person or edge is a no-op.
    Both people must exist before a referral is added. Nodes and edges cannot
    be removed in this version. Change these choices if your use case differs.

TODO
    Implement the API and document its invariants and error behavior. Add tests
    for a single node, chains, branches, disconnected components, a diamond,
    cycles, duplicate operations, unknown people, and invalid identifiers.
    Return snapshots rather than mutable internal collections.

Optional acyclic-policy variant
    Require a directed acyclic graph instead. Define cycle-rejection behavior
    for edge insertion, then test a back edge and concurrent insertions.
    Acyclicity alone does not impose one referrer per person or define a flow
    score. Keep this optional policy separate from the cyclic starter above.

Related files: referral_rankings.py and referral_growth.py.
"""

from collections.abc import Mapping


class ReferralNetwork:
    """Starter API; all domain operations remain to be implemented."""

    def __init__(self) -> None:
        self._referrals: dict[str, set[str]] = {}

    def add_person(self, person_id: str) -> None:
        """Create a person; raise ValueError for an invalid identifier."""
        # TODO: Validate the identifier and establish the node invariant.
        raise NotImplementedError

    def add_referral(self, referrer_id: str, referred_id: str) -> None:
        """Add an edge; reject self-referrals and missing people."""
        # TODO: Define exact exceptions, enforce the policy, and add the edge.
        raise NotImplementedError

    def direct_referrals(self, person_id: str) -> frozenset[str]:
        """Return a snapshot of one person's outgoing neighbors."""
        # TODO: Implement lookup and unknown-person behavior.
        raise NotImplementedError

    def snapshot(self) -> Mapping[str, frozenset[str]]:
        """Return an independent adjacency snapshot including isolated people."""
        # TODO: Avoid exposing internal mutable sets.
        raise NotImplementedError


if __name__ == "__main__":
    print("TODO: implement ReferralNetwork and add focused tests.")
