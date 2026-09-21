# HRProject — Project Description

HRProject is the empirical and data-science repository for a three-paper research program on group-specific employee flows.

The project investigates whether employee inflows and outflows can be measured by employee group with sufficient consistency to support cross-organization empirical analysis. It keeps measurement, theory, and empirical exploration distinct. A later confirmatory or econometric study may be developed from sufficiently clean subsets of the exploratory evidence.

## Research sequence

**Paper 1 — Group-Specific Employee Flow Rates**

Defines the measurement framework for group-specific employee flows.

**Paper 2 — The Effects of Group-Specific Employee Flows**

Develops theoretical implications of those flows.

**Paper 3 — Exploratory Analysis of Group-Specific Employee Flows**

Builds and characterizes a heterogeneous organization-group-time evidence layer while preserving source definitions, missingness, measurement uncertainty, and provenance.

## Empirical principle

The repository does not assume that the propositions of Paper 2 are empirically true. Paper 3 first determines what the available evidence can measure and compare; any confirmatory or econometric analysis is a subsequent stage.

The empirical design emphasizes:

- heterogeneous organizations;
- multiple employee groups;
- multiple industries and countries;
- repeated observations over time where available;
- explicit source definitions;
- non-negative flow counts;
- separation of observed, reconstructed, estimated, and missing values;
- provenance and data-quality flags;
- robustness and sensitivity analysis.

The principal observational key is $(i,g,t)$: organization $i$, employee group $g$, and time $t$.

## Data principle

The project follows a layered pipeline:

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
exploratory analysis
      |
      v
robustness and sensitivity
      |
      v
candidate hypotheses
      |
      v
optional confirmatory/econometric follow-up
```

Official statistical sources may provide labor-market benchmarks or, where their granularity permits, components of the empirical panel. Organization-level disclosures are evaluated separately and are not treated as interchangeable with aggregate labor-market statistics.

Source-defined concepts remain distinct. In particular, turnover, layoffs, other separations, workforce stocks, and firings are not treated as interchangeable measures. Missing firing observations remain missing rather than being inferred from other measures.

The repository has an initial coverage objective of approximately 50--100 organizations and an initial 2018--2025 annual window, subject to actual source availability and data quality. This is a coverage objective, not a quota.

## Current evidence

The current exploratory evidence layer contains 108 observations from 7 organizations. All seven organizations are currently classified as Secondary evidence rather than as a completed primary estimation panel. The acquired evidence contains hires, source-defined turnover, employment-end/workforce-stock observations, and other separations, but no directly observed group-specific firing observations.

These coverage figures describe the current evidence state and are expected to change as additional sources are acquired and validated.

## Reproducibility principle

Every analytical observation should be traceable to a source and a documented transformation. Missing values remain missing unless a documented reconstruction rule is applied. Source terminology is preserved rather than changed merely to make heterogeneous datasets appear comparable.

The reviewed Paper 3 publication source is maintained separately from the generated LaTeX artifact. This preserves a human editorial checkpoint while retaining a deterministic, testable generation pipeline.

The purpose of HRProject is therefore not simply to produce an HR dataset. It is to establish a reproducible empirical system for determining what can actually be learned from group-specific employee-flow data.
