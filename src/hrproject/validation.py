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
    "layoffs_and_discharges_bls",
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

FLOW_CONCEPTS = {
    "employment_begin",
    "employment_end",
    "hires",
    "firings",
    "quits",
    "layoffs",
    "layoffs_and_discharges_bls",
    "other_separations",
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


def validate_missing_not_zero(row: Mapping[str, Any]) -> list[str]:
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


def validate_jolts_firing_separation(row: Mapping[str, Any]) -> list[str]:
    """Prevent a JOLTS aggregate from being silently treated as firings."""
    errors: list[str] = []
    concept = row.get("flow_concept")
    source_id = row.get("source_id")
    bls_value = row.get("layoffs_and_discharges_bls")
    firings = row.get("firings")

    if source_id == "US_JOLTS" and bls_value is not None and concept == "firings":
        errors.append(
            "US_JOLTS: layoffs_and_discharges_bls cannot be relabeled as firings"
        )

    if source_id == "US_JOLTS" and firings is not None:
        quality = row.get("firing_quality")
        if quality not in {"directly_reported", "officially_derived"}:
            errors.append(
                "US_JOLTS: a firing value requires a separately documented "
                "source observation or official derivation"
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

    concept = row.get("flow_concept")
    if concept is not None and concept not in FLOW_CONCEPTS:
        errors.append(f"flow_concept: invalid value {concept!r}")

    return errors


def validate_row(row: Mapping[str, Any]) -> list[str]:
    """Run all row-level validation rules."""
    return (
        validate_nonnegative_counts(row)
        + validate_missing_not_zero(row)
        + validate_jolts_firing_separation(row)
        + validate_categories(row)
    )
