"""Validation helpers for organization-level Paper 3 screening records."""
from __future__ import annotations

from typing import Any

SCREENING_STATUSES = {"Pending", "Eligible", "Secondary", "Excluded"}
PROVENANCE_STATUSES = {"pending", "verified", "insufficient"}
DEFINITION_STATUSES = {"pending", "verified", "inconsistent"}
MEASUREMENT_STATUSES = {
    "pending",
    "observed",
    "reported",
    "reconstructed",
    "estimated",
    "missing",
}

REQUIRED_FIELDS = (
    "organization_id",
    "organization_unit",
    "group_id",
    "group_definition",
    "period_start",
    "period_end",
    "employment_denominator",
    "hiring_source",
    "firing_source",
    "separation_source",
    "source_definition",
    "provenance_status",
    "definition_consistency",
    "measurement_status",
    "screening_status",
    "screening_rationale",
)


def validate_screening_record(record: dict[str, Any]) -> list[str]:
    """Return validation errors without making an eligibility decision."""
    errors: list[str] = []

    for field in REQUIRED_FIELDS:
        if field not in record:
            errors.append(f"missing required field: {field}")

    if errors:
        return errors

    for field, allowed in (
        ("provenance_status", PROVENANCE_STATUSES),
        ("definition_consistency", DEFINITION_STATUSES),
        ("measurement_status", MEASUREMENT_STATUSES),
        ("screening_status", SCREENING_STATUSES),
    ):
        if record[field] not in allowed:
            errors.append(f"invalid {field}: {record[field]!r}")

    if not str(record["group_definition"]).strip():
        errors.append("group_definition cannot be empty")
    if not str(record["source_definition"]).strip():
        errors.append("source_definition cannot be empty")
    if not str(record["screening_rationale"]).strip():
        errors.append("screening_rationale cannot be empty")

    return errors


def primary_panel_requirements(record: dict[str, Any]) -> dict[str, bool]:
    """Return requirement flags; this function does not infer eligibility."""
    return {
        "organization_unit": bool(str(record.get("organization_unit", "")).strip()),
        "group_definition": bool(str(record.get("group_definition", "")).strip()),
        "employment_denominator": bool(
            str(record.get("employment_denominator", "")).strip()
        ),
        "hiring_source": bool(str(record.get("hiring_source", "")).strip()),
        "firing_source": bool(str(record.get("firing_source", "")).strip()),
        "separation_source": bool(str(record.get("separation_source", "")).strip()),
        "source_definition": bool(str(record.get("source_definition", "")).strip()),
        "provenance": record.get("provenance_status") == "verified",
        "definition_consistency": record.get("definition_consistency") == "verified",
    }
