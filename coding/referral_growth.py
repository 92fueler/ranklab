"""Estimate expected referral-network size after N days with a lifetime cap.

Problem
    Each eligible person has daily probability p of making one successful
    referral. No person may make more than 10 successful referrals in total.
    Estimate the expected network size after N days.

Starter choices, not universal assumptions
    Start with initial_population people who have made no referrals. All
    referrals create a new distinct person. Events are independent across
    people and days. A person makes at most one referral per day. New people
    become eligible the following day, not immediately. People who have reached
    the cap stay in the population but cannot refer again. No one leaves.
    days is a nonnegative integer, initial_population is a nonnegative integer,
    and p is a finite number in [0, 1]. The lifetime cap is fixed at 10 here.

TODO
    Track expected populations by successful-referral count, including a
    saturated group at 10. Define the day boundary precisely. Implement a
    seeded simulation as an independent check, not as a substitute for the
    expectation calculation. Test N = 0, p = 0, p = 1, an empty starting
    population, invalid inputs, and saturation. Do not silently use unbounded
    exponential growth when the lifetime cap changes the result.
"""

LIFETIME_CAP = 10


def expected_network_size(
    days: int, p: float, initial_population: int = 1
) -> float:
    """Compute the expectation under the explicitly chosen daily model."""
    # TODO: Validate inputs, represent referral-count groups, and update days.
    raise NotImplementedError


def simulate_network_size(
    days: int, p: float, initial_population: int = 1, *, seed: int = 0
) -> int:
    """Run one reproducible realization for comparison with the expectation."""
    # TODO: Use a local seeded random generator and the same day-boundary rules.
    raise NotImplementedError


if __name__ == "__main__":
    print("TODO: implement the capped model, simulation, and boundary tests.")
