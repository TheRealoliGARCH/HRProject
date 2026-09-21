"""Source-preserving exploratory profiling for Paper 3 evidence.

This module profiles the evidence layer. It does not convert percentages to
counts, infer missing observations, or relabel source-defined concepts.
"""
from __future__ import annotations

from collections import Counter
from typing import Iterable, Mapping


def evidence_profile(rows: Iterable[Mapping[str, str]]) -> dict[str, object]:
    """Return descriptive coverage and measurement summaries."""
    rows = list(rows)
    flow_concepts = Counter(
        row.get("flow_concept", "")
        for row in rows
        if row.get("flow_concept")
    )
    units = Counter(
        row.get("unit", "")
        for row in rows
        if row.get("unit")
    )
    measurement_status = Counter(
        row.get("measurement_status", "")
        for row in rows
        if row.get("measurement_status")
    )
    screening_status = Counter(
        row.get("screening_status", "")
        for row in rows
        if row.get("screening_status")
    )
    group_dimensions = Counter(
        row.get("group_dimension", "")
        for row in rows
        if row.get("group_dimension")
    )

    return {
        "observation_count": len(rows),
        "organizations": len({
            row.get("organization_id", "")
            for row in rows
            if row.get("organization_id")
        }),
        "source_ids": sorted({
            row.get("source_id", "")
            for row in rows
            if row.get("source_id")
        }),
        "flow_concepts": dict(flow_concepts),
        "units": dict(units),
        "measurement_status": dict(measurement_status),
        "screening_status": dict(screening_status),
        "group_dimensions": dict(group_dimensions),
    }


def flow_concept_counts(rows: Iterable[Mapping[str, str]]) -> dict[str, int]:
    """Count evidence observations by source-defined flow concept."""
    return dict(Counter(
        row.get("flow_concept", "")
        for row in rows
        if row.get("flow_concept")
    ))


def organization_coverage(rows: Iterable[Mapping[str, str]]) -> dict[str, int]:
    """Count evidence observations by organization."""
    return dict(Counter(
        row.get("organization_id", "")
        for row in rows
        if row.get("organization_id")
    ))


def measurement_status_counts(rows: Iterable[Mapping[str, str]]) -> dict[str, int]:
    """Count evidence observations by measurement status."""
    return dict(Counter(
        row.get("measurement_status", "")
        for row in rows
        if row.get("measurement_status")
    ))
