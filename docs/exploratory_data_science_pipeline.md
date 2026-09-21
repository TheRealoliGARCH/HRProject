# Exploratory Data Science Pipeline for Paper 3

## Purpose

Paper 3 is an exploratory data-science study of group-specific employee flows. The purpose is to determine what can be measured from heterogeneous public organizational sources, characterize the resulting observations, identify systematic patterns and measurement gaps, and generate candidate hypotheses for later confirmatory work.

The pipeline does **not** assume that the theoretical propositions in Paper 2 are true.

## Research questions

1. Which group-specific employee-flow concepts are observable across organizations?
2. How heterogeneous are observed flows across organizations, groups, industries, countries, and years?
3. Which flow concepts are consistently reported, and which are sparse or source-specific?
4. What patterns appear in hires, quits, employer-initiated separations, layoffs, turnover, workforce stocks, and other separations?
5. Where do missingness and measurement uncertainty concentrate?
6. Which candidate relationships merit subsequent confirmatory or econometric testing?

## Observation architecture

The canonical key remains:

```
(organization_id, group_id, year)
```

The dataset may contain different flow concepts for the same key. It must not manufacture a complete vector of flows merely because one source reports only a subset.

## Pipeline

### 1. Source discovery

Identify official organizational, government, regulatory, sustainability, annual-report, labor-statistics, and other authoritative sources.

Record:

- organization;
- source;
- reporting period;
- official URL;
- source definition;
- available group dimensions;
- available flow concepts;
- measurement unit.

### 2. Acquisition and extraction

Extract observations without changing source terminology.

Examples include:

- workforce stock;
- employment begin/end;
- hires;
- quits;
- layoffs;
- employer-initiated separations;
- turnover;
- other separations.

A source-defined turnover measure is not converted into a firing count.

### 3. Raw evidence layer

Preserve the source-derived observation and provenance before harmonization.

Every observation should retain enough metadata to reconstruct:

```text
source -> observation -> harmonized field
```

### 4. Validation

Apply the repository's validation rules:

- counts must be non-negative;
- missing values remain missing;
- controlled measurement and firing-quality statuses are respected;
- source-defined broad categories are not silently decomposed;
- organization-level observations are distinguished from aggregate benchmarks.

### 5. Harmonization

Map observations into the common schema only where the source supports the mapping.

Harmonization is a representation step, not an inference step.

### 6. Exploratory analysis

The initial EDA should include:

- flow distributions;
- organization-level heterogeneity;
- group-level heterogeneity;
- industry comparisons;
- country comparisons;
- temporal patterns;
- workforce-stock/flow relationships;
- source and measurement-status frequencies;
- missingness maps;
- coverage by group dimension;
- correlations among directly comparable source-defined measures.

### 7. Visualization

Produce reproducible visualizations such as:

- organization-by-year coverage matrices;
- group-by-flow heatmaps;
- flow distributions;
- country/industry coverage maps;
- missingness matrices;
- time-series panels where definitions are comparable.

Visualization must preserve the distinction between observed quantities and unavailable quantities.

### 8. Robustness and sensitivity

Where exploratory statistics depend on inclusion choices, report sensitivity to:

- country;
- industry;
- reporting period;
- group definition;
- measurement status;
- source family;
- direct versus reconstructed observations.

Do not use sensitivity analysis to convert an unavailable measure into an available one.

### 9. Candidate hypotheses

Exploratory patterns may motivate hypotheses for later confirmatory analysis.

The workflow is:

```text
exploration -> candidate hypothesis -> new/held-out evidence -> confirmatory test
```

The exploratory dataset must not be presented as causal identification.

## Primary versus secondary evidence

The existing organization-screening framework remains useful.

- **Primary:** evidence meeting the requirements for the intended analysis.
- **Secondary:** useful verified evidence that does not establish the full firing-flow measurement required for the original confirmatory design. This evidence remains part of the exploratory dataset rather than a completed primary estimation panel.
- **Pending:** source screening or verification incomplete.
- **Excluded:** evidence fails a defined admission requirement.

Secondary observations are not discarded. They can be valuable for descriptive analysis and for understanding the measurement environment.

## Relationship to Papers 1 and 2

Paper 1 supplies the measurement framework.

Paper 2 supplies theoretical propositions.

Paper 3 asks what the available evidence actually permits us to observe.

Thus:

```text
Paper 1: measurement -> Paper 2: theory -> Paper 3: exploration -> future confirmatory testing
```

This ordering prevents the exploratory dataset from being engineered around an expected theoretical result.

## Stopping rule for organization acquisition

The earlier target of approximately 50 organizations remains a useful coverage target, not a requirement.

Acquisition should stop or change direction when additional organizations provide little marginal information relative to:

- country coverage;
- industry coverage;
- group-dimension coverage;
- flow-concept coverage;
- temporal coverage;
- measurement-quality diversity.

The final sample size is therefore data-driven rather than quota-driven.
