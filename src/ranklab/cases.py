"""Normalize raw case field names while preserving their text and criteria."""

from pathlib import Path


def load_case(path: str | Path) -> dict:
    import yaml

    with Path(path).open(encoding="utf-8") as stream:
        case = yaml.safe_load(stream)
    if not isinstance(case, dict):
        raise ValueError("Case must be a YAML mapping")
    normalized = {}
    for key, value in case.items():
        if not isinstance(key, str):
            raise ValueError("Case field names must be strings")
        key = key.strip().lower().replace(" ", "_")
        if key in normalized:
            raise ValueError(f"Duplicate case field after normalization: {key}")
        normalized[key] = value
    for key in ("title", "natural_language_description", "hard_criteria"):
        if key not in normalized:
            raise ValueError(f"Missing raw case field: {key}")
    for key in ("title", "natural_language_description"):
        if not isinstance(normalized[key], str) or not normalized[key].strip():
            raise ValueError(f"{key} must be a nonempty string")
    normalized.setdefault("soft_criteria", [])
    for key in ("hard_criteria", "soft_criteria"):
        values = normalized[key]
        if not isinstance(values, list) or any(
            not isinstance(value, str) or not value.strip() for value in values
        ):
            raise ValueError(f"{key} must be a list of nonempty strings")
    return normalized
