"""Diagnose asynchronous refund retries using only local synthetic fakes.

Problem
    Load a refund record, skip completed work, and attempt a provider refund
    up to three times. The INTENTIONALLY BUGGY flow below then marks the record
    completed even when every attempt failed.

TODO expectations
    Repair exhaustion handling and define durable states and return outcomes.
    Cover concurrent workers, unknown timeout outcomes, database-write failures,
    replay, and recovery. State the provider's idempotency and reconciliation
    contract, including what happens after an idempotency key expires. Do not
    promise exactly-once external effects from a local transaction.

Original test scaffold
    These in-memory fakes intentionally lack idempotency and coordination.
    Amounts are integer minor units; no real money, account, network request,
    credentials, or provider integration is involved. The example executes
    four deterministic failure scenarios; the repaired entry point is a TODO.

Related variant
    interrupted_payment.py demonstrates a synchronous charge-then-record
    failure window rather than this asynchronous refund-exhaustion defect.
"""

import asyncio
from dataclasses import dataclass, field, replace
from typing import Literal


class ProviderError(RuntimeError):
    """A synthetic failure before the provider performs a refund."""


@dataclass(frozen=True)
class RefundRecord:
    amount_minor: int
    completed: bool = False


@dataclass
class FakeRefundStore:
    records: dict[str, RefundRecord]
    fail_next_write: bool = False

    async def load(self, operation_id: str) -> RefundRecord:
        await asyncio.sleep(0)
        return replace(self.records[operation_id])

    async def mark_completed(self, operation_id: str) -> None:
        await asyncio.sleep(0)
        if self.fail_next_write:
            self.fail_next_write = False
            raise OSError("Synthetic database failure before saving completion.")
        self.records[operation_id] = replace(
            self.records[operation_id], completed=True
        )


@dataclass
class FakeRefundProvider:
    outcomes: list[Literal["fail", "success", "timeout_after_success"]] = field(
        default_factory=list
    )
    refunds: list[int] = field(default_factory=list)
    calls: int = 0

    async def refund(self, amount_minor: int) -> str:
        await asyncio.sleep(0)
        self.calls += 1
        outcome = self.outcomes.pop(0) if self.outcomes else "success"
        if outcome == "fail":
            raise ProviderError("Synthetic provider failure before refund.")
        self.refunds.append(amount_minor)
        if outcome == "timeout_after_success":
            raise TimeoutError("Refund happened, but its response was lost.")
        return f"refund-{len(self.refunds)}"


async def refund_buggy(
    operation_id: str, provider: FakeRefundProvider, store: FakeRefundStore
) -> str:
    """INTENTIONALLY BUGGY: exhaustion, overlap, and replay are unsafe."""
    record = await store.load(operation_id)
    if record.completed:
        return "already completed"
    for _ in range(3):
        try:
            await provider.refund(record.amount_minor)
            break
        except (ProviderError, TimeoutError):
            pass
    await store.mark_completed(operation_id)
    return "completed"


async def refund(
    operation_id: str, provider: FakeRefundProvider, store: FakeRefundStore
) -> str:
    """TODO: define safe outcomes and extend the interfaces where necessary."""
    # TODO: Repair the flow under an explicit provider/storage contract.
    raise NotImplementedError


async def demonstrate_bugs() -> None:
    store = FakeRefundStore({"example": RefundRecord(1000)})
    provider = FakeRefundProvider(["fail", "fail", "fail"])
    result = await refund_buggy("example", provider, store)
    assert result == "completed" and provider.calls == 3 and not provider.refunds
    assert store.records["example"].completed
    print("Exhaustion: falsely completed after three failures and zero refunds.")
    print("Replay after false completion:", await refund_buggy("example", provider, store))

    store = FakeRefundStore({"example": RefundRecord(1000)})
    provider = FakeRefundProvider()
    await asyncio.gather(
        refund_buggy("example", provider, store),
        refund_buggy("example", provider, store),
    )
    assert len(provider.refunds) == 2
    print("Overlapping workers: refunds performed =", len(provider.refunds))

    store = FakeRefundStore({"example": RefundRecord(1000)})
    provider = FakeRefundProvider(["timeout_after_success", "success"])
    await refund_buggy("example", provider, store)
    assert len(provider.refunds) == 2
    print("Uncertain timeout: refunds performed =", len(provider.refunds))

    store = FakeRefundStore({"example": RefundRecord(1000)}, fail_next_write=True)
    provider = FakeRefundProvider()
    try:
        await refund_buggy("example", provider, store)
    except OSError as error:
        print("Persistence failure:", error)
    await refund_buggy("example", provider, store)
    assert len(provider.refunds) == 2
    print("Retry after failed persistence: refunds performed =", len(provider.refunds))
    print("TODO: repair the flow and convert failure scenarios into regression tests.")


if __name__ == "__main__":
    asyncio.run(demonstrate_bugs())
