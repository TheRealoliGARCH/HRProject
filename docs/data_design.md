# HRProject Data Design

## Objective

Build a heterogeneous organization panel to test the theoretical propositions in Paper 2 using the measurement framework in Paper 1.

## Observation

The fundamental observation is:

`(organization_id, group_id, year)`.

## Layers

### Raw

Preserve source observations exactly as reported, together with source metadata.

### Validated

Apply count, missingness, category, duplicate, period, and definition checks.

### Analysis

Harmonize definitions and calculate derived measures only from validated observations.

## Organization panel

Initial target:

- approximately 50--100 organizations;
- multiple industries;
- multiple countries;
- annual observations beginning in 2018 and extending through 2025 where available.

The final sample is determined by data quality, not expected results.

## Benchmark datasets

Official aggregate or establishment-level statistics are contextual benchmarks. They are not automatically converted into organization-level observations.

The India module should include Labour Bureau sources:

- Indian Labour Statistics;
- Quarterly Employment Survey;
- Annual Survey of Industries;
- industrial disputes, closures, retrenchments and lay-offs statistics.

The international benchmark layer can include sources such as U.S. BLS JOLTS.

## Flow rules

For observed counts:

```
employment_begin >= 0
employment_end   >= 0
hires            >= 0
firings          >= 0
```

Missing firing information remains missing. It is never imputed as zero merely because a source is silent.

## Data provenance

Every analytical observation must be traceable to:

1. organization;
2. group;
3. period;
4. source;
5. source definition;
6. original reported value;
7. transformation, if any;
8. validation status.

## Empirical sequence

```
source acquisition
    -> raw preservation
    -> validation
    -> definition harmonization
    -> derived measures
    -> descriptive analysis
    -> Paper 2 hypothesis tests
    -> robustness
```

No empirical result should determine inclusion or transformation rules after the results are observed.
