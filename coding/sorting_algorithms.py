"""Implement sorting algorithms and explain their complexity.

Problem
    Implement a sorting algorithm with subquadratic worst-case running time.
    Contrast it with a deliberately slow method that generates permutations
    and checks whether each is sorted. Explain the comparison-sorting bound.

Starter choices
    Inputs are finite sequences of integers, including duplicates and negative
    values. Return a new list without mutating the input. Use merge sort for
    the efficient method and deterministic exhaustive permutation enumeration
    for the slow method. The latter is not random repeated shuffling. Restrict
    exhaustive-method tests to tiny inputs so they terminate promptly.

TODO
    Implement both algorithms without delegating their core logic to sorted()
    or list.sort(). Derive merge sort's recurrence, running time, and extra
    space. Account for both generating and checking permutations when bounding
    the exhaustive method. Explain the decision-tree lower bound for worst-case
    comparison sorting on arbitrary distinct elements; do not claim every sort
    always takes exactly n log n time. Explain how duplicate values affect
    enumeration and how exhaustive enumeration differs from random shuffling.
    Test empty/singleton inputs, duplicates, sorted/reverse-sorted data,
    negative values, input preservation, and output multiplicities.
"""

from collections.abc import Sequence


def merge_sort(values: Sequence[int]) -> list[int]:
    """Return an ascending sorted copy using merge sort."""
    # TODO: Implement decomposition, merging, and boundary cases.
    raise NotImplementedError


def exhaustive_permutation_sort(values: Sequence[int]) -> list[int]:
    """Return a sorted permutation through exhaustive search; tiny inputs only."""
    # TODO: Generate permutations and check their ordering explicitly.
    raise NotImplementedError


if __name__ == "__main__":
    print("TODO: implement both sorts, add tests, and derive complexity bounds.")
