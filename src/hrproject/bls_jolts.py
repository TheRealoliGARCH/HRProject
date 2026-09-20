"""Parsing helpers for official BLS JOLTS bulk files."""
from __future__ import annotations
import csv
from pathlib import Path

FLOW_FILES = {
    "jt.data.3.Hires": "hires",
    "jt.data.5.Quits": "quits",
    "jt.data.6.LayoffsDischarges": "layoffs_and_discharges_bls",
    "jt.data.7.OtherSeparations": "other_separations",
}

def read_bulk_file(path: Path) -> list[dict[str, str]]:
    """Read a BLS tab-delimited bulk time-series file."""
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return [{k.strip(): v.strip() for k, v in row.items() if k is not None}
                for row in reader]

def parse_flow_file(path: Path, flow_concept: str) -> list[dict[str, object]]:
    """Parse one JOLTS flow file into normalized observations."""
    rows = read_bulk_file(path)
    output = []
    for row in rows:
        value = row.get("value", "")
        if not value:
            continue
        output.append({
            "series_id": row["series_id"],
            "year": int(row["year"]),
            "period": row["period"],
            "value": float(value),
            "flow_concept": flow_concept,
            "source_id": "US_JOLTS",
            "source_variable": path.name,
            "source_definition": "BLS JOLTS published flow category; definition retained from BLS metadata.",
        })
    return output

def parse_jolts_directory(directory: Path) -> list[dict[str, object]]:
    """Parse supported JOLTS flow files in a raw-data directory."""
    observations = []
    for filename, concept in FLOW_FILES.items():
        path = directory / filename
        if path.exists():
            observations.extend(parse_flow_file(path, concept))
    return observations
