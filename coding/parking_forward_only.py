"""Decide whether every arriving car can park with forward-only overflow.

Problem
    Spaces are numbered 0 through space_count - 1. Cars arrive in the order
    of preferred_spaces. Each takes its preferred space if free; otherwise it
    takes the first free space with a larger index. Cars never move backward,
    wrap around, or displace parked cars. Return whether every car parks.

Contract
    space_count is between 1 and 100,000; at most 100,000 cars arrive.
    Preferences are valid space indices. Empty arrivals succeed.
    More cars than spaces cannot all park.

Examples
    space_count = 3, preferred_spaces = [1, 1] -> True.
    space_count = 3, preferred_spaces = [2, 2] -> False.
    space_count = 3, preferred_spaces = [] -> True.

TODO
    Implement the fixed arrival policy without reordering cars. State time
    and space complexity. Test repeated preferences, a full lot, a free space
    behind a blocked car, the final space, empty input, and maximum-size input.

Separate variant
    parking_feasibility.py asks whether any permitted complete assignment
    exists. Its explicit fallback sets are not this forward-only policy.
"""

from collections.abc import Sequence


def can_all_park_forward_only(
    preferred_spaces: Sequence[int], space_count: int
) -> bool:
    """Return whether the specified arrival policy parks every car."""
    # TODO: Implement the policy at the stated input scale.
    raise NotImplementedError


if __name__ == "__main__":
    print("TODO: implement forward-only parking and boundary/scale tests.")
