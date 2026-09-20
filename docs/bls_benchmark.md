# BLS JOLTS Benchmark

## PR #2: ingestion

The benchmark ingestion layer parses official BLS JOLTS bulk flow files and preserves the source-defined concepts:

- hires;
- quits;
- layoffs and discharges;
- other separations.

The third category is stored as `layoffs_and_discharges_bls`. It is not relabeled as `firings`.

## PR #3: metadata normalization

PR #3 adds a metadata normalization layer for the official BLS bulk files:

- `jt.series`;
- `jt.industry`;
- `jt.period`;
- `jt.seasonal`.

The normalization joins metadata by identifiers supplied by BLS while preserving source-defined fields. It does not invent a new industry, seasonal-adjustment, or period taxonomy.

## PR #4: benchmark flow normalization and validation

PR #4 adds the analysis-ready benchmark builder in `src/hrproject/bls_benchmark.py` and the executable entry point `scripts/build_bls_benchmark.py`.

The builder:

1. parses all available supported JOLTS flow files;
2. retains the BLS series identifier, year, period, source file, and footnote codes;
3. preserves the BLS flow concept;
4. assigns an explicit observed measurement status;
5. routes observations through the central validation layer;
6. rejects invalid negative counts and invalid firing treatment.

The default output is `data/analysis/bls_jolts_flows.csv`. The output is generated only after the official raw BLS files have actually been acquired.

### Validation boundary

The benchmark validation layer checks the observation-level integrity rules already established for the project. In particular:

- counts cannot be negative;
- missing firing counts cannot silently become zero;
- JOLTS `layoffs_and_discharges_bls` cannot be relabeled as `firings`;
- a JOLTS firing value would require a separately documented observation or official derivation;
- controlled measurement fields must use permitted values.

The benchmark builder does not infer firings from layoffs and discharges.

### Provenance

Each benchmark observation retains:

- `series_id`;
- `year`;
- `period`;
- `source_id`;
- `source_variable`;
- `source_definition`;
- `footnote_codes`;
- `measurement_status`;
- `firing_quality`.

## Measurement firewall

JOLTS provides a benchmark for source-defined employee flows. It does not provide a separate numerical firing series in the supported bulk flow files. Consequently, the benchmark is useful for validating the empirical pipeline and for aggregate labor-flow context, but it is not substituted for the organization-level group-specific panel required by Paper 3.

## Acquisition status

The repository contains acquisition and processing code, but code presence is not evidence that external BLS artifacts have been downloaded. Raw BLS files must be acquired before the benchmark CSV is generated.

The automated test workflow uses local fixtures and therefore does not depend on external network access.
