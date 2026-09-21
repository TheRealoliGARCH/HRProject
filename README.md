# HRProject

## Project description

**HRProject is the empirical/data-science implementation repository for a three-paper research program on group-specific employee flows.** The project develops a measurement framework for employee inflows and outflows by group, develops theoretical implications of those flows, and then explores the resulting evidence using a heterogeneous panel of organizations.

The empirical objective is deliberately narrower than a generic HR analytics project: determine whether group-specific employee-flow measures are observable and statistically informative across organizations, industries, countries, and time, while preserving the original definitions and limitations of the underlying sources.

The project treats **measurement, theory, and empirical validation as separate stages**:

1. **Paper 1 — Group-Specific Employee Flow Rates:** measurement framework.
2. **Paper 2 — The Effects of Group-Specific Employee Flows:** theoretical implications.
3. **Paper 3 — Exploratory Analysis of Group-Specific Employee Flows:** heterogeneous-panel data-science analysis. A later confirmatory/econometric paper may be developed from sufficiently clean subsets of the exploratory dataset.

Paper 3 uses the measurement framework from Paper 1 and the theoretical propositions from Paper 2 as conceptual inputs. It does not assume that those propositions are true, and exploratory findings are not treated as causal evidence.

## Exploratory Data Science Design

The primary Paper 3 workflow is now exploratory rather than confirmatory. The objective is to build and characterize a heterogeneous organizational employee-flow dataset while preserving source definitions, measurement uncertainty, missingness, and provenance.

The Data Science pipeline is:

```text
source discovery
      |
      v
acquisition and extraction
      |
      v
raw observations + provenance
      |
      v
validation
      |
      v
definition harmonization
      |
      v
exploratory analysis dataset
      |
      v
EDA: distributions, heterogeneity, missingness, temporal patterns
      |
      v
visualization + descriptive statistics
      |
      v
robustness and sensitivity checks
      |
      v
research findings + candidate hypotheses
      |
      v
optional confirmatory/econometric follow-up
```

The pipeline permits heterogeneous observation types. A source can contribute useful evidence without establishing group-specific firing counts. Workforce stocks, hires, quits, layoffs, turnover, and other source-defined measures remain distinct. The absence of a firing observation is itself recorded as missing evidence rather than converted into zero.

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
exploratory analysis
      |
      v
robustness and sensitivity analysis
      |
      v
optional estimation/confirmatory analysis
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

Papers 1 and 2 are present in the repository as PDFs. The exploratory implementation is being developed through the data-science pipeline. The repository retains the original empirical-design machinery because it may support a later confirmatory study.

The branch currently contains the validation layer, data dictionary, source registry, organization-registry scaffold, acquisition plan, source-acquisition protocol, tests, and analysis-data scaffolding.
