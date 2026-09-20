# Harmonized heterogeneous panel

PR #7 establishes the admission gate and schema for the Paper 3 organization-group-year analysis panel.

## Purpose

The panel is intended to test the propositions developed in Paper 2 using the measurement framework in Paper 1. The empirical unit remains:

`(organization_id, group_id, year)`.

This PR establishes the harmonization layer without manufacturing organization-level observations that have not been verified.

## Admission rules

A prospective analysis observation must have:

- an identifiable organization, country, industry, year, and group;
- a source-defined or explicitly documented group definition;
- a count-based observation rather than a percentage or composition statistic;
- source provenance and a non-empty source definition;
- valid non-negative count fields where counts are observed;
- explicit treatment of missing firing information;
- the exact source-defined flow concept retained.

The admission gate is not an eligibility classifier. It does not select observations based on the magnitude or direction of employee flows.

## Measurement discipline

- A percentage distribution is not converted into a count.
- Missing firing counts remain missing.
- BLS JOLTS `layoffs_and_discharges_bls` remains that source-defined category and is not relabeled as `firings`.
- Source definitions are copied into the analysis row rather than replaced by generic terminology.
- Duplicate `(organization_id, group_id, year)` observations are rejected.

## Current data boundary

The merged PR #6 evidence for TCS contains group-specific new-hire percentages and workforce/attrition measures. Those records remain in the source-evidence ledger and are **not** admitted to the count-based analysis panel by this PR.

Therefore PR #7 establishes the reproducible panel construction mechanism and schema; it does not claim that the target 50--100 organization panel has been acquired.

## Empirical sequence

```
verified source evidence
        ->
count-based admission
        ->
validation
        ->
definition harmonization
        ->
analysis panel
        ->
estimation and robustness
```

No result from the eventual empirical analysis should be used retroactively to alter these admission rules.
