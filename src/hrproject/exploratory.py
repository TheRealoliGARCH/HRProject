"""Source-preserving exploratory profiling for Paper 3 evidence.

This module profiles the evidence layer. It does not convert percentages to
counts, infer missing observations, or relabel source-defined concepts.
"""
from __future__ import annotations

from collections import Counter
from typing import Iterable, Mapping


def evidence_profile(rows: Iterable[Mapping[str, str]]) -> dict[str, object]:
    """Return descriptive coverage and measurement summaries.

    The function treats each supplied row as an evidence observation. It does
    not infer absent observations or collapse distinct source concepts.
    """
    rows = list(rows)
    return {
        "observation_count": len(rows),
        "organizations": len({r.get("organization_id", "") for r in rows if r.get("organization_id")}),
        "source_ids": sorted({r.get("source_id", "") for r in rows if r.get("source_id")}),
        "flow_concepts": dict(Counter(
            r.get("flow_concept", "") for r in rows if r.get("flow_concept")
        )),
        "units": dict(Counter(r.get("unit", "") for r in rows if r.get("unit"))),
        "measurement_status": dict(Counter(
            r.get("measurement_status", "")
            for r in rows if r.get("measurement_status")
        )),
        "screening_status": dict(Counter(
            r.get("screening_status", "")
            for r in rows if r.get("screening_status")
        )),
        "group_dimensions": dict(Counter(
            r.get("group_dimension", "")
            for r in rows if r.get("group_dimension")
        )),
    )


def flow_concept_counts(rows: Iterable[Mapping[str, str]]) -> dict[str, int]:
    """Count evidence observations by source-defined flow concept."""
    return dict(Counter(
        r.get("flow_concept", "") for r in rows if r.get("flow_concept")
    ))


def organization_coverage(rows: Iterable[Mapping[str, str]]) -> dict[str, int]:
    """Count evidence observations by organization."""
    return dict(Counter(
        r.get("organization_id", "") for r in rows if r.get("organization_id")
    ))


def measurement_status_counts(rows: Iterable[Mapping[str, str]]) -> dict[str, int]:
    """Count evidence observations by measurement status."""
    return dict(Counter(
        r.get("measurement_status", "")
        for r in rows if r.get("measurement_status")
    ))
