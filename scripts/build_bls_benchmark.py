"""Build the analysis-ready BLS JOLTS benchmark flow CSV."""
from __future__ import annotations

import argparse
from pathlib import Path

from hrproject.bls_benchmark import build_benchmark_rows, write_benchmark_csv


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/raw/bls_jolts"),
        help="Directory containing acquired BLS JOLTS bulk files.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/analysis/bls_jolts_flows.csv"),
        help="Output CSV path.",
    )
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"Input directory does not exist: {args.input}")

    rows = build_benchmark_rows(args.input)
    if not rows:
        raise SystemExit("No supported BLS JOLTS observations were found.")

    write_benchmark_csv(rows, args.output)
    print(f"Wrote {len(rows)} observations to {args.output}")


if __name__ == "__main__":
    main()
