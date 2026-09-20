"""Build a normalized BLS JOLTS series metadata artifact."""
from __future__ import annotations
import argparse
import csv
from pathlib import Path
from hrproject.bls_metadata import normalize_series_metadata

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=Path("data/raw/bls_jolts"))
    parser.add_argument("--output", type=Path, default=Path("data/analysis/bls_jolts_series.csv"))
    args = parser.parse_args()
    rows = normalize_series_metadata(args.input_dir)
    if not rows:
        raise SystemExit("No jt.series metadata found. Acquire the official BLS JOLTS artifacts before running normalization.")
    fieldnames = sorted({key for row in rows for key in row})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
