"""Historical evaluation/submission transport shapes, with fresh configuration.

These helpers make external requests only when explicitly called. Their server
contracts must be checked against the actual service before use.
"""

from pathlib import Path
from urllib.parse import urlparse

from .settings import required_env


def _post(endpoint_env: str, payload: dict) -> dict:
    import requests

    endpoint = required_env(endpoint_env)
    parsed = urlparse(endpoint)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError(f"{endpoint_env} must be an HTTP(S) URL")
    response = requests.post(
        endpoint,
        headers={
            "Content-Type": "application/json",
            "Authorization": required_env("EVAL_AUTH_EMAIL"),
        },
        json=payload,
        timeout=60,
    )
    response.raise_for_status()
    result = response.json()
    if not isinstance(result, dict):
        raise ValueError("Evaluator response must be a JSON object")
    return result


def _validate_selection(config_path: str, object_ids: list[str]) -> None:
    if not isinstance(config_path, str) or not config_path.strip() or not Path(config_path).name:
        raise ValueError("Case filename must be nonempty")
    if (not isinstance(object_ids, list) or len(object_ids) != 10
            or any(not isinstance(value, str) or not value.strip() for value in object_ids)):
        raise ValueError("Selection must contain exactly ten nonempty string IDs")
    if len(set(object_ids)) != len(object_ids):
        raise ValueError("Selection must contain ten distinct IDs")


def evaluate(config_path: str, object_ids: list[str]) -> dict:
    """Evaluate selected original IDs for one case; return the full feedback."""
    _validate_selection(config_path, object_ids)
    return _post("EVAL_ENDPOINT", {
        "config_path": Path(config_path).name,
        "object_ids": object_ids,
    })


def submit(config_candidates: dict[str, list[str]]) -> dict:
    """Submit a final case-to-IDs mapping as a separate explicit action."""
    if not isinstance(config_candidates, dict) or not config_candidates:
        raise ValueError("Final submission must be a nonempty case-to-IDs mapping")
    for filename, ids in config_candidates.items():
        _validate_selection(filename, ids)
        if Path(filename).name != filename:
            raise ValueError("Final submission keys must be case filenames, not paths")
    return _post("GRADE_ENDPOINT", {"config_candidates": config_candidates})
