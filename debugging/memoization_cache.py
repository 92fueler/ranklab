"""Diagnose a memoization cache with intentionally missing safeguards.

Problem
    A global dictionary returns a cached value when present. Otherwise, an
    expensive computation runs, its result is stored, and that value is
    returned. Review capacity, concurrency, failure handling, and input rules.

Intentional defects and open policies
    The runnable example below is INTENTIONALLY BUGGY: storage is unbounded,
    concurrent misses can repeat expensive work, and keys have no validation
    beyond dictionary behavior. Computation errors escape without a defined
    failure policy. An exception not being cached is not inherently a bug;
    decide whether retries, error caching, or another policy fits the use case.
    Falsey cached values are valid and must remain cache hits after a repair.

TODO expectations
    Define capacity/eviction, optional expiration, valid keys, and error policy.
    Distinguish safe dictionary access from single-flight work for the same
    key. Do not serialize all unrelated expensive operations unnecessarily.
    Implement a repaired API and add tests for concurrent misses, exceptions,
    invalid keys, capacity/eviction, and falsey cached results. Test against the
    documented policy rather than treating every possible feature as required.

Run this file to observe duplicate work and cache growth. It uses only local
memory and threads; the short barrier coordinates the demonstration.
"""

from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier

_CACHE: dict[object, object] = {}


def cached_value_buggy(key: object, compute: Callable[[object], object]) -> object:
    """INTENTIONALLY BUGGY: no capacity, validation, or in-flight coordination."""
    if key in _CACHE:
        return _CACHE[key]
    value = compute(key)
    _CACHE[key] = value
    return value


def cached_value(key: object, compute: Callable[[object], object]) -> object:
    """TODO: specify and implement a repaired cache API; change it if needed."""
    # TODO: Make storage ownership, configuration, and lifecycle explicit.
    raise NotImplementedError


def demonstrate_bugs() -> None:
    _CACHE.clear()
    rendezvous = Barrier(2)
    computations: list[object] = []

    def expensive_work(key: object) -> str:
        computations.append(key)
        rendezvous.wait(timeout=5)
        return f"value for {key}"

    with ThreadPoolExecutor(max_workers=2) as workers:
        pending = [workers.submit(cached_value_buggy, "same-key", expensive_work)
                   for _ in range(2)]
        print("Results:", [future.result() for future in pending])
    print("Computations for one shared miss:", len(computations))

    for number in range(20):
        cached_value_buggy(number, lambda key: key)
    print("Stored entries with no capacity limit:", len(_CACHE))
    print("TODO: define a policy, repair the cache, and add regression tests.")


if __name__ == "__main__":
    demonstrate_bugs()
