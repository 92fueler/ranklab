"""Determine whether every car can park given preferred positions.

Problem
    Cars have preferred parking positions. Determine whether all cars can
    park. Parking and fallback rules must be defined before implementation.

Explicit starter version
    Spaces are integers from 0 through space_count - 1. Cars arrive in the
    supplied order, and each occupies one space permanently. A car's permitted
    spaces are its preferred space plus its explicitly listed fallback spaces.
    Any permitted free space may be chosen, even if its preferred space is
    free. The question is whether some assignment parks every car, not whether
    a particular greedy policy succeeds. Different cars may share preferences.
    No unstated rule such as "drive to the next free space" is assumed.

Separate variant
    parking_forward_only.py uses a fixed next-free-space policy. It does not
    allow arbitrary choices among fallback spaces.

TODO
    Implement feasibility for these chosen rules and validate all positions.
    As a separate extension, enumerate valid assignments with backtracking and
    pruning. Define the meaning of an empty input and of zero spaces. Test
    repeated preferences, insufficient spaces, boundary/invalid positions,
    duplicate fallback entries, and choices that block a later car. Compare
    feasibility strategies and state their worst-case complexity.
"""

from collections.abc import Iterator, Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class Car:
    preferred_space: int
    fallback_spaces: tuple[int, ...] = ()


def can_all_park(cars: Sequence[Car], space_count: int) -> bool:
    """Return whether a legal complete assignment exists."""
    # TODO: Validate the rules and implement feasibility without a greedy assumption.
    raise NotImplementedError


def enumerate_assignments(
    cars: Sequence[Car], space_count: int
) -> Iterator[tuple[int, ...]]:
    """Optional extension: yield each unique assignment in arrival order."""
    # TODO: Implement enumeration separately; avoid duplicate output assignments.
    raise NotImplementedError


if __name__ == "__main__":
    print("TODO: implement parking feasibility and optional assignment enumeration.")
