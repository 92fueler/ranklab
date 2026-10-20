"""Diagnose an interrupted external-payment operation using local fakes.

Problem
    A service charges through an external provider, inserts a payment record
    into a database, and returns success. What happens if a client, process,
    provider response, or database write fails during that sequence?

Intentional defects and starter choices
    The runnable example is INTENTIONALLY BUGGY. It has no durable operation
    identifier, idempotency, intermediate state, or reconciliation. Its fake
    provider can charge successfully and then lose the response; its fake
    database can fail before recording a charge. Retrying the whole operation
    can therefore charge twice. These in-memory fakes illustrate failure
    windows only: there is no network access, real account, or real payment.
    Amounts use positive integer minor units for an unspecified single currency.

TODO expectations
    Enumerate failures before a charge, after a charge but before persistence,
    and after persistence but before the response reaches the client. Treat a
    timeout as an unknown outcome, not proof that no charge occurred. Specify
    durable operation identifiers, provider-supported idempotency semantics,
    state transitions (including unresolved outcomes), retries, and recovery.
    Explain why a local database transaction cannot make an unrelated external
    side effect atomic. Test duplicate requests, lost responses, transient
    provider failures, database-write failures, and restart/reconciliation.
    Do not add real provider credentials to this example.

Related design questions: ../system_design/payment_integration.md.
"""

from dataclasses import dataclass, field


@dataclass
class FakeProvider:
    """Local failure simulator, not a real payment integration."""

    charges: list[tuple[str, int]] = field(default_factory=list)
    lose_next_response: bool = False

    def charge(self, amount_minor: int) -> str:
        charge_id = f"charge-{len(self.charges) + 1}"
        self.charges.append((charge_id, amount_minor))
        if self.lose_next_response:
            self.lose_next_response = False
            raise TimeoutError("The charge succeeded but its response was lost.")
        return charge_id


@dataclass
class FakeDatabase:
    """Local persistence simulator with a configurable failed write."""

    records: list[tuple[str, int]] = field(default_factory=list)
    fail_next_write: bool = False

    def insert(self, charge_id: str, amount_minor: int) -> None:
        if self.fail_next_write:
            self.fail_next_write = False
            raise OSError("Database write failed before storing the record.")
        self.records.append((charge_id, amount_minor))


def pay_buggy(
    amount_minor: int, provider: FakeProvider, database: FakeDatabase
) -> str:
    """INTENTIONALLY BUGGY: a blind retry repeats the external side effect."""
    charge_id = provider.charge(amount_minor)
    database.insert(charge_id, amount_minor)
    return "success"


def pay(
    operation_id: str,
    amount_minor: int,
    provider: FakeProvider,
    database: FakeDatabase,
) -> str:
    """TODO: define safe states and extend the fake interfaces as necessary."""
    # TODO: Specify provider guarantees; an operation_id argument alone is not a fix.
    raise NotImplementedError


def demonstrate_bugs() -> None:
    for failure in ("lost provider response", "failed database write"):
        provider = FakeProvider(lose_next_response=failure == "lost provider response")
        database = FakeDatabase(fail_next_write=failure == "failed database write")
        try:
            pay_buggy(1000, provider, database)
        except (TimeoutError, OSError) as error:
            print(f"{failure}: {error}")
        print("Blind retry result:", pay_buggy(1000, provider, database))
        print("Provider charges:", provider.charges)
        print("Database records:", database.records)
    print("TODO: design the recovery contract, repair the flow, and add tests.")


if __name__ == "__main__":
    demonstrate_bugs()
