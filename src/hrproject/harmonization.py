"""Admission and harmonization helpers for the Paper 3 analysis panel."""
from __future__ import annotations

from typing import Any, Iterable

from .validation import validate_row

ANALYSIS_KEY = ("organization_id", "group_id", "year")
IDENTIFIER_FIELDS = (
    "organization_id",
    "country",
    "industry",
    "year",
    "group_id",
    "group_definition",
)
ANALYSIS_FIELDS = (
    "organization_id",
    "country",
    "industry",
    "year",
    "group_id",
    "group_definition",
    "employment_begin",
    "employment_end",
    "hires",
    "firings",
    "quits",
    "layoffs",
    "layoffs_and_discharges_bls",
    "other_separations",
    "flow_concept",
    "source_id",
    "measurement_status",
    "firing_quality",
    "source_definition",
    "notes",
)


def analysis_admission_errors(row: dict[str, Any]) -> list[str]:
    """Return errors for a prospective organization-group-year observation.

    This is an admission gate, not an eligibility classifier. It does not
    impute missing values, decompose source categories, or infer causality.
    """
    errors: list[str] = []

    for field in IDENTIFIER_FIELDS:
        if field not in row or row[field] in (None, ""):
            errors.append(f"missing analysis identifier: {field}")

    if "year" in row and row["year"] is not None:
        try:
            if int(row["year"]) < 2018:
                errors.append("year must be >= 2018")
        except (TypeError, ValueError):
            errors.append("year must be an integer")

    if row.get("observation_unit") != "count":
        errors.append("analysis panel requires count observations")

    if not str(row.get("source_definition", "")).strip():
        errors.append("source_definition cannot be empty")

    errors.extend(validate_row(row))
    return errors


def harmonize_row(row: dict[str, Any]) -> dict[str, Any]:
    """Return an analysis-row copy after validation.

    Only fields already present in the source observation are carried forward.
    No percentages are converted to counts and no broader separation category
    is relabeled as firings.
    """
    errors = analysis_admission_errors(row)
    if errors:
        raise ValueError("; ".join(errors))

    return {field: row.get(field) for field in ANALYSIS_FIELDS}


def harmonize_rows(rows: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Harmonize unique organization-group-year observations."""
    output: list[dict[str, Any]] = []
    seen: set[tuple[Any, ...]] = set()

    for row in rows:
        harmonized = harmonize_row(row)
        key = tuple(harmonized[field] for field in ANALYSIS_KEY)
        if key in seen:
            raise ValueError(f"duplicate analysis observation: {key!r}")
        seen.add(key)
        output.append(harmonized)

    return output
