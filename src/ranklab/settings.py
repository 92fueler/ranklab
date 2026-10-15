"""Environment-backed configuration; no credentials or historical endpoints."""

import os


def required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if (not value or ".invalid" in value.lower()
            or value.upper().startswith(("REDACTED", "YOUR_", "REPLACE_ME"))):
        raise ValueError(f"Set {name} to a valid value before using this helper")
    return value
