"""Find a conversion rate through consistent exchange rates.

Problem
    Each supplied rate converts one source unit into rate target units.
    Reverse conversions use reciprocals; chained conversions multiply rates.
    Return the source-to-target rate, or -1.0 if unreachable.

Contract
    Codes have three uppercase letters. At most 10,000 rates are supplied,
    with no duplicate unordered pair or self-edge. Rates lie in [1e-3, 1e3];
    reachable conversion results lie in [1e-9, 1e9]. Alternative paths give consistent
    results. The relative numerical tolerance is 1e-6.
    Identical source and target return 1.0 even for an absent code.
    Otherwise, unknown or disconnected currencies return -1.0.

Examples
    AAA -> BBB = 2.0 and BBB -> CCC = 3.0 imply AAA -> CCC = 6.0
    and CCC -> AAA = 1 / 6. With no rates, ZZZ -> ZZZ returns 1.0.

TODO
    Implement one query and state complexity. Test direct, reciprocal, and
    multi-hop conversions, consistent cycles, disconnected components,
    unknown codes, identity, and empty input. Compare floats with tolerance.

Optional engineering extension
    Design a reusable interface for repeated queries on unchanged rates.
    Arbitrage detection is outside this consistent-rate contract.
"""

from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class ExchangeRate:
    source: str
    target: str
    rate: float


def conversion_rate(
    rates: Sequence[ExchangeRate], source: str, target: str
) -> float:
    """Return the conversion rate or -1.0 if unreachable."""
    # TODO: Implement conversion.
    raise NotImplementedError


if __name__ == "__main__":
    print("TODO: implement chained currency conversion and numerical tests.")
