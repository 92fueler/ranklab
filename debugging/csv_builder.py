"""Repair an intentionally faulty CSV-building routine.

Problem
    A routine repeatedly concatenates cells, appends a comma after every cell,
    and appends a newline after every row. Review correctness, data policies,
    and the cost of producing large outputs.

Intentional defects and starter choices
    The runnable Python model below is INTENTIONALLY BUGGY: it emits an extra
    trailing column and does not escape commas, quotes, or embedded newlines.
    Cells here are strings or None; the buggy version stringifies None without
    an explicit null policy. It uses '\\n' and emits one blank line for an
    empty row. These choices are behavior to review, not required CSV semantics.

TODO expectations
    Define null versus empty-string behavior, empty-row behavior, line endings,
    and validation. Repair delimiter placement and quoting. Assess incremental
    immutable-string construction and memory use at the actual output size;
    consider streaming and a well-tested CSV writer. Add round-trip tests using
    a CSV parser for commas, quotes, newlines, empty input, empty rows, nulls,
    and large inputs. Do not assume all target consumers use identical rules.

Run this file to inspect the malformed output and how a CSV parser reads it.
"""

import csv
import io
from collections.abc import Iterable, Sequence

Cell = str | None


def build_csv_buggy(rows: Iterable[Sequence[Cell]]) -> str:
    """INTENTIONALLY BUGGY: concatenation, trailing delimiters, no escaping."""
    result = ""
    for row in rows:
        for cell in row:
            result += str(cell) + ","
        result += "\n"
    return result


def build_csv(rows: Iterable[Sequence[Cell]]) -> str:
    """TODO: document the chosen dialect and null policy, then implement."""
    # TODO: Produce valid CSV with tested delimiter and quoting behavior.
    raise NotImplementedError


def demonstrate_bugs() -> None:
    rows: list[list[Cell]] = [
        ["name", "note"],
        ["Ada", "hello, world"],
        ["Lin", 'says "hello"'],
        ["Sam", "two\nlines"],
        ["No value", None],
    ]
    output = build_csv_buggy(rows)
    print("Malformed CSV:")
    print(output)
    print("Rows read back:", list(csv.reader(io.StringIO(output))))
    print("TODO: repair the writer and add round-trip regression tests.")


if __name__ == "__main__":
    demonstrate_bugs()
