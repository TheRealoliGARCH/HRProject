#!/usr/bin/env python3
"""Generate the current exploratory Paper 3 from repository evidence."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hrproject.paper import write_paper  # noqa: E402


if __name__ == "__main__":
    path = write_paper(ROOT / "metadata/organization_source_evidence.csv",
                       ROOT / "outputs/exploratory_paper.md")
    print(path)
