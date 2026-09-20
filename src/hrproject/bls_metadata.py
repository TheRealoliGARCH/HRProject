"""Normalization helpers for official BLS JOLTS metadata files."""
from __future__ import annotations
import csv
from pathlib import Path
from typing import Iterable

METADATA_FILES = {
    "jt.series": "series", "jt.industry": "industry",
    "jt.period": "period", "jt.seasonal": "seasonal",
}

def read_metadata_file(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return [{key.strip(): value.strip() for key, value in row.items() if key is not None}
                for row in reader]

def index_by(rows: Iterable[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        identifier = row.get(key, "")
        if identifier:
            indexed[identifier] = row
    return indexed

def load_jolts_metadata(directory: Path) -> dict[str, list[dict[str, str]]]:
    result: dict[str, list[dict[str, str]]] = {}
    for filename, concept in METADATA_FILES.items():
        path = directory / filename
        if path.exists():
            result[concept] = read_metadata_file(path)
    return result

def normalize_series_metadata(directory: Path) -> list[dict[str, str]]:
    metadata = load_jolts_metadata(directory)
    series_rows = metadata.get("series", [])
    industries = index_by(metadata.get("industry", []), "industry_code")
    periods = index_by(metadata.get("period", []), "period")
    seasonal_rows = metadata.get("seasonal", [])
    seasonals = index_by(seasonal_rows, "seasonal_code")
    if not seasonals:
        seasonals = index_by(seasonal_rows, "seasonal")
    normalized: list[dict[str, str]] = []
    for series in series_rows:
        row = dict(series)
        for key, value in industries.get(series.get("industry_code", ""), {}).items():
            row.setdefault(f"industry_{key}", value)
        for key, value in periods.get(series.get("period", ""), {}).items():
            row.setdefault(f"period_{key}", value)
        seasonal_code = series.get("seasonal_code") or series.get("seasonal", "")
        for key, value in seasonals.get(seasonal_code, {}).items():
            row.setdefault(f"seasonal_{key}", value)
        normalized.append(row)
    return normalized
