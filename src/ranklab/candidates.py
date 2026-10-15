"""Row access adapted from the shared reference implementation."""

from collections.abc import Mapping


def get_attr(row, key, default=None):
    """
    Robustly fetch an attribute/field from a Turbopuffer Row.
    Works whether the row exposes attributes, a dict, or (rarely) .attributes.
    """
    # Check mappings first so fields such as "items" do not return dict methods.
    if isinstance(row, Mapping):
        if key in row:
            return row[key]
        attributes = row.get("attributes")
        return attributes.get(key, default) if isinstance(attributes, Mapping) else default

    if hasattr(row, key):
        return getattr(row, key)

    # ultra-rare: nested attributes dict
    if hasattr(row, "attributes") and isinstance(row.attributes, Mapping):
        return row.attributes.get(key, default)

    return default
