"""Acquire the official BLS JOLTS benchmark files.

The script preserves the BLS source categories. In particular, JOLTS
"layoffs and discharges" is stored as layoffs_and_discharges_bls and is
never relabeled as firings.

Usage:
    python scripts/acquire_bls_jolts.py --output data/raw/bls_jolts
"""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.request import urlretrieve
from datetime import date

BASE = "https://download.bls.gov/pub/time.series/JT/"
FILES = (
    "jt.series",
    "jt.industry",
    "jt.period",
    "jt.seasonal",
    "jt.data.3.Hires",
    "jt.data.5.Quits",
    "jt.data.6.LayoffsDischarges",
    "jt.data.7.OtherSeparations",
)


def acquire(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    manifest = []
    for name in FILES:
        destination = output / name
        urlretrieve(BASE + name, destination)
        manifest.append(
            f"{name},{BASE + name},{date.today().isoformat()},{destination}"
        )
        print(f"acquired {name} -> {destination}")

    (output / "acquisition_manifest.csv").write_text(
        "artifact,official_url,retrieval_date,local_path\n"
        + "\n".join(manifest)
        + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/raw/bls_jolts"),
    )
    args = parser.parse_args()
    acquire(args.output)


if __name__ == "__main__":
    main()
