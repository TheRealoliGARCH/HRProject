# HRProject

## Project description

**HRProject is the empirical implementation repository for a three-paper research program on group-specific employee flows.** The project develops a measurement framework for employee inflows and outflows by group, develops theoretical implications of those flows, and then tests the resulting propositions using a heterogeneous panel of organizations.

The empirical objective is deliberately narrower than a generic HR analytics project: determine whether group-specific employee-flow measures are observable and statistically informative across organizations, industries, countries, and time, while preserving the original definitions and limitations of the underlying sources.

The project treats **measurement, theory, and empirical validation as separate stages**:

1. **Paper 1 — Group-Specific Employee Flow Rates:** measurement framework.
2. **Paper 2 — The Effects of Group-Specific Employee Flows:** theoretical implications.
3. **Paper 3 — An Empirical Test of Group-Specific Employee Flow Effects:** heterogeneous-panel empirical test.

Paper 3 uses the measure from Paper 1 and tests propositions developed in Paper 2. It does not redefine either paper.

## Empirical design

The core observational unit is:

$$
(i,g,t),
$$

where $i$ denotes an organization, $g$ an employee group, and $t$ a time period.

The initial target is an approximately 50--100 organization panel, spanning multiple industries and countries, with an initial 2018--2025 annual window, subject to actual source availability and data quality.

The project distinguishes:

- organization-level observations from aggregate labor-market benchmarks;
- hires from separations;
- quits from employer-initiated separations;
- directly reported counts from reconstructed or estimated quantities;
- missing values from genuine zeros.

No organization, country, industry, or group is included because its data are expected to support a particular result. Inclusion is determined by pre-specified data requirements and source quality.

## Data architecture

```
raw source data
      |
      v
validation
      |
      v
definition harmonization
      |
      v
analysis panel
      |
      v
estimation
      |
      v
robustness and sensitivity analysis
```

The repository is designed so that raw source-derived observations are preserved and transformations are reproducible. Source verification, data acquisition, and variable validation are separate gates: identifying a credible source does not mean that the required observations have already been acquired.

## Core variables

The organization-group-time panel is built around:

`organization_id`, `country`, `industry`, `year`, `group_id`,
`group_definition`, `employment_begin`, `employment_end`, `hires`,
`firings`, `quits`, `layoffs`, `other_separations`, `source_id`,
`measurement_status`, and `firing_quality`.

All count variables must satisfy:

$$
N_{igt} \geq 0,\qquad h_{igt} \geq 0,\qquad f_{igt} \geq 0.
$$

A missing firing count is **missing**. It is never silently converted to zero.

## Source discipline

Source terminology is retained rather than silently normalized. For example, the U.S. Bureau of Labor Statistics JOLTS program defines “layoffs and discharges” as employer-initiated involuntary separations and explicitly includes firings among several categories. Therefore, JOLTS observations must not be relabeled as “firings” merely because firings are a component of that measure.

For India, Labour Bureau's Quarterly Employment Survey is an establishment-based survey covering establishments with 10 or more workers across nine selected sectors. It is therefore useful as an official labor-market benchmark and potential source for establishment-level evidence, but its aggregate estimates are not automatically treated as organization-level observations.

## Repository layout

- `data/raw/` — immutable source-derived observations.
- `data/validated/` — observations passing validation.
- `data/analysis/` — harmonized panel and derived measures.
- `metadata/` — data dictionary, source registry, organization registry, and acquisition plan.
- `src/hrproject/` — validation and measurement code.
- `tests/` — automated data-integrity tests.
- `docs/` — research and data documentation.

## Integrity principles

- Hires and firings are non-negative counts.
- Missing is never silently converted to zero.
- Source definitions are preserved.
- Raw observations are not overwritten.
- Provenance is recorded for analysis observations.
- Organization-level data are distinguished from aggregate benchmarks.
- Sample selection is based on data requirements, not anticipated results.
- Causal claims require a separate identification strategy.
- Measurement uncertainty is retained rather than hidden.
- Source verification is not treated as data acquisition.
- Broad source categories are not silently decomposed into narrower concepts.

## Current status

Papers 1 and 2 are present in the repository as PDFs. The empirical implementation is being developed on the `empirical-design` branch.

The branch currently contains the validation layer, data dictionary, source registry, organization-registry scaffold, acquisition plan, source-acquisition protocol, tests, and analysis-data scaffolding.
