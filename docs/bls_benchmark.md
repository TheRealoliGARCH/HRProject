# BLS JOLTS Benchmark

## PR #2: ingestion

The benchmark ingestion layer parses official BLS JOLTS bulk flow files and preserves the source-defined concepts:

- hires;
- quits;
- layoffs and discharges;
- other separations.

The repository stores the third category as `layoffs_and_discharges_bls`. It is not relabeled as `firings`.

## PR #3: metadata normalization

PR #3 adds a metadata normalization layer for the official BLS bulk files:

- `jt.series`;
- `jt.industry`;
- `jt.period`;
- `jt.seasonal`.

The normalization joins metadata by identifiers supplied by BLS while preserving source-defined fields. It does not invent a new industry, seasonal-adjustment, or period taxonomy.

The executable entry point is `scripts/normalize_bls_jolts.py`. Its default output is `data/analysis/bls_jolts_series.csv`.

The script requires `jt.series` to have been acquired into `data/raw/bls_jolts/`. The repository does not claim that external BLS artifacts have been downloaded merely because acquisition and normalization scripts exist.

## Measurement firewall

JOLTS publishes hires, quits, layoffs and discharges, and other separations. A missing firing count remains missing. The benchmark therefore supplies a source-defined aggregate employer-initiated separation measure without manufacturing a firing decomposition.

## Validation boundary

PR #3 normalizes metadata. It does not yet create the organization-level empirical panel or make causal claims. Raw acquisition, parsing, validation, harmonization, estimation, and robustness remain distinct stages.
