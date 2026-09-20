# BLS JOLTS benchmark ingestion

PR #2 adds the first parser for the project's official benchmark layer.

The ingestion layer reads official BLS JOLTS bulk files for hires, quits,
layoffs and discharges, and other separations.

The parser preserves the BLS flow concept in flow_concept and records
source_id=US_JOLTS and the source filename.

## Measurement rule

The JOLTS Layoffs and Discharges series is not renamed to firings. BLS
includes firings within the broader employer-initiated layoffs-and-discharges
category. The benchmark therefore documents the relationship without claiming
that the published series is a firing series.

## Missingness

Rows with a blank published value are skipped rather than converted to zero.

## Reproducibility

Raw acquisition remains the responsibility of scripts/acquire_bls_jolts.py.
This parser operates only on files already present in data/raw/bls_jolts/.
The parser tests require no external network connection.
