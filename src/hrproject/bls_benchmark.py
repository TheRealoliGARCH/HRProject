"""Build and validate an analysis-ready BLS JOLTS benchmark flow file.

The benchmark preserves BLS source concepts. In particular,
layoffs_and_discharges_bls is never relabeled as firings.
"""
from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from .bls_jolts import parse_jolts_directory
from .validation import validate_nonnegative_counts


def build_benchmark_rows(directory: Path) -> list[dict[str, Any]]:
    """Parse supported JOLTS flow files into validated benchmark rows."""
    rows = parse_jolts_directory(directory)
    output: list[dict[str, Any]] = []
    for row in rows:
        concept = row["flow_concept"]
        benchmark = {
            "series_id": row["series_id"],
            "year": row["year"],
            "period": row["period"],
            "flow_concept": concept,
            "value": row["value"],
            "source_id": row["source_id"],
            "source_variable": row["source_variable"],
            "source_definition": row["source_definition"],
            "footnote_codes": row.get("footnote_codes", ""),
            "measurement_status": "observed",
            "firing_quality": "missing",
        }
        errors = validate_nonnegative_counts(
            {
                "hires": benchmark["value"] if concept == "hires" else None,
                "quits": benchmark["value"] if concept == "quits" else None,
                "layoffs_and_discharges_bls": (
                    benchmark["value"]
                    if concept == "layoffs_and_discharges_bls"
                    else None
                ),
                "other_separations": (
                    benchmark["value"] if concept == "other_separations" else None
                ),
            }
        )
        if errors:
            raise ValueError("; ".join(errors))
        output.append(benchmark)
    return output


def write_benchmark_csv(rows: list[dict[str, Any]], output: Path) -> None:
    """Write benchmark observations as a deterministic CSV artifact."""
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "series_id",
        "year",
        "period",
        "flow_concept",
        "value",
        "source_id",
        "source_variable",
        "source_definition",
        "footnote_codes",
        "measurement_status",
        "firing_quality",
    ]
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
