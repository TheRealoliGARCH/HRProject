# HRProject — Project Description

HRProject is the empirical implementation repository for a three-paper research program on group-specific employee flows.

The project asks whether employee inflows and outflows can be measured by employee group in a sufficiently consistent way to permit cross-organization empirical analysis. It connects a measurement paper, a theoretical paper, and an empirical-testing paper without collapsing their distinct roles.

## Research sequence

**Paper 1 — Group-Specific Employee Flow Rates**

Defines the measurement framework for group-specific employee flows.

**Paper 2 — The Effects of Group-Specific Employee Flows**

Develops the theoretical implications of those flows.

**Paper 3 — An Empirical Test of Group-Specific Employee Flow Effects**

Implements the empirical test using a heterogeneous organization-group-time panel.

## Empirical principle

The repository does not assume that the propositions of Paper 2 are empirically true. It builds the data and estimation system needed to test them.

The empirical design therefore emphasizes:

- heterogeneous organizations;
- multiple employee groups;
- multiple industries and countries;
- repeated observations over time;
- explicit source definitions;
- non-negative flow counts;
- separation of observed, reconstructed, estimated, and missing values;
- provenance and data-quality flags;
- robustness and sensitivity analysis.

The principal observation is $(i,g,t)$: organization $i$, employee group $g$, and time $t$.

## Data principle

The project uses a layered data architecture:

raw source data → validation → harmonization → analysis → estimation → robustness.

Official statistical sources are used as benchmarks and, where their granularity permits, as potential components of the empirical panel. Organization-level disclosures are evaluated separately and are not treated as interchangeable with aggregate labor-market statistics.

The repository currently targets an initial panel of approximately 50--100 organizations and an initial 2018--2025 annual window, subject to actual data availability.

## Reproducibility principle

Every analytical observation should be traceable to a source and a documented transformation. Missing values must remain missing unless a documented reconstruction rule is applied. Source terminology must not be changed merely to make datasets appear comparable.

The purpose of HRProject is therefore not simply to produce an HR dataset. It is to establish a reproducible empirical system for determining what can actually be learned from group-specific employee-flow data.
