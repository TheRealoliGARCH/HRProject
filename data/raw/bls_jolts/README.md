# BLS JOLTS raw acquisition

This directory is reserved for source artifacts acquired from the U.S. Bureau
of Labor Statistics Job Openings and Labor Turnover Survey (JOLTS).

## Official source

BLS publishes the JOLTS time-series files under:

https://download.bls.gov/pub/time.series/JT/

The acquisition script is:

`scripts/acquire_bls_jolts.py`

It downloads the official series metadata and the published flow files for:

- hires;
- quits;
- layoffs and discharges;
- other separations.

## Measurement rule

JOLTS defines layoffs and discharges as involuntary employer-initiated
separations and explicitly includes firings among that broader category.
The project therefore stores this source concept as
`layoffs_and_discharges_bls`.

It is **not** converted into `firings`.

A firing observation may enter the primary `firings` field only when a source
separately reports firings or provides a documented official derivation.

## Acquisition status

The presence of this directory and acquisition script does not imply that
observations have already been imported into the analysis panel. Imported
artifacts must be accompanied by retrieval metadata and validation.

## Reproducibility

Run:

```text
python scripts/acquire_bls_jolts.py --output data/raw/bls_jolts
```

The script uses the official BLS download endpoint rather than a third-party
mirror.
