"""Validation rules for the HRProject empirical dataset."""

from __future__ import annotations

from typing import Any, Mapping

COUNT_FIELDS = (
    "employment_begin",
    "employment_end",
    "hires",
    "firings",
    "quits",
    "layoffs",
    "other_separations",
)

MEASUREMENT_STATUSES = {
    "observed",
    "reported",
    "reconstructed",
    "estimated",
    "missing",
}

FIRING_QUALITIES = {
    "directly_reported",
    "officially_derived",
    "reconstructed",
    "estimated",
    "missing",
    "ambiguous",
}


def validate_nonnegative_counts(row: Mapping[str, Any]) -> list[str]:
    """Return validation errors for observed count fields.

    Missing values are allowed. Negative observed counts are not.
    """
    errors: list[str] = []
    for field in COUNT_FIELDS:
        value = row.get(field)
        if value is None:
            continue
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            errors.append(f"{field}: count must be numeric or missing")
            continue
        if value < 0:
            errors.append(f"{field}: count must be non-negative")
    return errors


def validate_missing_not_zero(
    row: Mapping[str, Any],
) -> list[str]:
    """Require explicit status when a firing count is unavailable."""
    errors: list[str] = []
    firings = row.get("firings")
    quality = row.get("firing_quality")

    if firings is None and quality not in {"missing", "ambiguous"}:
        errors.append(
            "firings: missing firing count requires firing_quality="
            "'missing' or 'ambiguous'"
        )

    return errors


def validate_categories(row: Mapping[str, Any]) -> list[str]:
    """Validate controlled categorical fields."""
    errors: list[str] = []

    status = row.get("measurement_status")
    if status is not None and status not in MEASUREMENT_STATUSES:
        errors.append(f"measurement_status: invalid value {status!r}")

    quality = row.get("firing_quality")
    if quality is not None and quality not in FIRING_QUALITIES:
        errors.append(f"firing_quality: invalid value {quality!r}")

    return errors


def validate_row(row: Mapping[str, Any]) -> list[str]:
    """Run all row-level validation rules."""
    return (
        validate_nonnegative_counts(row)
        + validate_missing_not_zero(row)
        + validate_categories(row)
    )
