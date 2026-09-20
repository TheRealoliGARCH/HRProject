# HRProject

Empirical implementation repository for the three-paper research program on group-specific employee flows.

## Research architecture

1. **Paper 1 — Group-Specific Employee Flow Rates**: measurement framework.
2. **Paper 2 — The Effects of Group-Specific Employee Flows**: theoretical implications.
3. **Paper 3 — An Empirical Test of Group-Specific Employee Flow Effects**: heterogeneous-panel empirical test.

Paper 3 uses the measure from Paper 1 and tests the propositions from Paper 2. It does not redefine either.

## Data architecture

```
raw data
    -> validation
    -> harmonization
    -> analysis dataset
    -> estimation
    -> robustness
```

The target panel is approximately 50--100 organizations, multiple employee groups, and an initial 2018--2025 annual window, subject to data availability and quality.

## Core principles

- Hires and firings are non-negative counts.
- Missing is never silently converted to zero.
- Source definitions are preserved.
- Raw observations are not overwritten.
- Organization-level observations are distinguished from aggregate labor-market benchmarks.
- The sample is selected by data requirements, not anticipated results.
- Causal claims require a separate identification strategy.

## Repository layout

- `data/raw/` — immutable source-derived observations.
- `data/validated/` — observations passing validation.
- `data/analysis/` — harmonized panel and derived measures.
- `metadata/` — data dictionary and source registry.
- `src/hrproject/` — validation and measurement code.
- `tests/` — automated data-integrity tests.
- `docs/` — research and data documentation.

## Primary organization-level fields

`organization_id`, `country`, `industry`, `year`, `group_id`,
`group_definition`, `employment_begin`, `employment_end`, `hires`,
`firings`, `quits`, `layoffs`, `other_separations`, `source_id`,
`measurement_status`, and `firing_quality`.

## Data integrity

For count variables:

$$
N_{igt} \geq 0, \qquad h_{igt} \geq 0, \qquad f_{igt} \geq 0.
$$

If a firing count is not reported, it is missing; it is not zero.

## Indian statistical sources

The India module should include Labour Bureau sources such as Indian Labour Statistics, Quarterly Employment Survey, Annual Survey of Industries, and statistics concerning industrial disputes, closures, retrenchments, and lay-offs. These are benchmark and source datasets; they are not automatically treated as organization-level observations.

## Status

The repository currently contains Papers 1 and 2 as PDFs. The empirical implementation is being built on the `empirical-design` branch.
