# Exploratory Analysis of Group-Specific Employee Flows

## Abstract

This paper develops an exploratory data-science analysis of publicly reported group-specific employee-flow evidence across heterogeneous organizations. The study operationalizes the measurement framework of Paper 1 and uses the theoretical propositions of Paper 2 as conceptual inputs without assuming that those propositions are empirically true. The current evidence layer contains 108 observations from seven organizations in India, the United Kingdom, and the United States. The observations cover hires, source-defined employee turnover, workforce-stock measures, and other separations, but contain no directly observed group-specific firing counts. The evidence also spans heterogeneous group definitions, units, and reporting periods. These characteristics make the measurement structure itself an empirical object of interest. The paper therefore emphasizes provenance, source-definition preservation, missingness, comparability, and descriptive heterogeneity rather than causal estimation. The results establish a reproducible exploratory baseline and identify measurement gaps that should guide subsequent data acquisition and any later confirmatory analysis.

**Keywords:** employee flows; employee turnover; group-specific measurement; exploratory data science; workforce composition; organizational reporting; measurement uncertainty; human resources.

---

## 1. Introduction

Employee-flow research commonly distinguishes inflows from outflows, but public organizational reporting does not necessarily expose these quantities at a common level of definition or aggregation. Organizations may report hires, attrition, turnover, layoffs, involuntary turnover, workforce stocks, or other separation measures using organization-specific definitions. Group dimensions may likewise differ across gender, age, region, employment category, or combinations of these dimensions.

This paper treats that heterogeneity as a data problem before treating it as an estimation problem.

The study is the third component of a research program. Paper 1 develops a framework for group-specific employee-flow measurement. Paper 2 develops theoretical implications of group-specific employee flows. The present paper asks what can actually be observed in heterogeneous organizational data and how far those observations can be compared without silently changing their meanings.

The central research question is therefore:

> **What does publicly available organizational evidence reveal about the observability, structure, and comparability of group-specific employee flows?**

Several narrower questions follow:

1. Which employee-flow concepts are actually reported?
2. Which group dimensions are available?
3. How heterogeneous are the reported units and definitions?
4. How much longitudinal coverage is available?
5. Where are the principal measurement gaps?
6. Which empirical questions can reasonably be pursued next?

The paper is explicitly exploratory. It does not assume the theoretical propositions of Paper 2, does not convert missing observations into zeros, and does not interpret descriptive associations as causal effects.

---

## 2. Conceptual Framework

The observational architecture is an organization-group-time observation:

$$
(i,g,t),
$$

where $i$ denotes an organization, $g$ an employee group, and $t$ a reporting period.

The project distinguishes several employee-flow concepts rather than treating them as interchangeable. In particular:

- hires are inflows;
- quits are voluntary separations where the source defines them as such;
- layoffs and discharges are retained under the source definition;
- employee turnover and attrition retain their source-defined meanings;
- workforce stocks describe employment levels rather than flows;
- firings are treated as a distinct concept only when the source actually supports that interpretation.

This distinction is critical because a broader source-defined category may contain a narrower theoretical component without providing a separately observed numerical value for that component.

The same principle applies to missingness. If a source does not report a group-specific firing count, the observation is missing. It is not a zero:

$$
	ext{not reported} 
eq 0.
$$

The empirical pipeline is consequently:

[
	ext{source discovery}
ightarrow
	ext{acquisition}
ightarrow
	ext{validation}
ightarrow
	ext{definition harmonization}
ightarrow
	ext{exploratory analysis}
ightarrow
	ext{robustness}
ightarrow
	ext{candidate hypotheses}.
]

Any later confirmatory or econometric analysis is a separate stage.

---

## 3. Data and Sources

The current evidence layer contains **108 observations from seven organizations**:

- five Indian organizations;
- one United Kingdom organization;
- one United States organization.

All seven organizations are currently classified as secondary evidence rather than members of a completed primary estimation panel.

The organizations are:

1. Tata Consultancy Services;
2. Infosys;
3. Wipro;
4. HCLTech;
5. Tech Mahindra;
6. HSBC Holdings;
7. Alphabet.

The evidence was extracted from official organizational reporting and retained with source identifiers, document titles, reporting periods, official URLs, evidence types, group dimensions, source-defined flow concepts, units, measurement status, and notes.

The current reporting-period distribution is:

| Reporting period | Observations |
|---|---:|
| FY2018-19 | 61 |
| FY2024 | 31 |
| FY2024-25 | 15 |
| FY2025 | 1 |

The evidence is consequently not a balanced annual panel. The current data should be understood as an exploratory evidence collection rather than a completed longitudinal panel.

---

## 4. Measurement Structure

### 4.1 Flow concepts

The 108 observations decompose as follows:

| Flow concept | Observations |
|---|---:|
| Hires | 55 |
| Employee turnover | 48 |
| Employment-end/workforce-stock observations | 4 |
| Other separations | 1 |
| Firings | 0 |

The most important finding is therefore not an estimate of firing behavior. It is the absence of directly observed group-specific firing counts in the acquired organizational evidence.

That result is a statement about **measurement availability**, not about the incidence of firing.

### 4.2 Units

The evidence contains:

- 96 count observations;
- 10 percentage observations;
- 2 percentage-women observations.

The analysis does not transform percentages into counts without a defensible denominator. This preserves the distinction between reported rates and reported quantities.

### 4.3 Group dimensions

The evidence contains multiple group structures, including:

- gender;
- age;
- region;
- employment group;
- turnover category;
- overall observations;
- combined employment-group/gender/age classifications;
- combined region/age/gender classifications.

These dimensions are not assumed to be directly interchangeable. A gender-specific turnover rate and an age-by-region-by-gender hiring count represent different observational structures.

---

## 5. Exploratory Findings

### 5.1 Hiring information is substantially more observable than firing information

The current evidence contains 55 hire observations but no group-specific firing observations.

This asymmetry suggests that public organizational reporting may be substantially richer for employee entry than for the specific employer-initiated separation concept required by the theoretical framework.

The correct inference is a measurement one:

> Public reporting currently provides considerably more usable group-specific evidence for hiring than for firing.

The data do not establish whether the underlying incidence of firing is low, high, stable, or heterogeneous.

### 5.2 Turnover is observable but conceptually heterogeneous

Employee-turnover observations account for 48 observations. Some are counts; others are rates. Some are voluntary turnover measures, while others are source-defined involuntary or total turnover measures.

Consequently, turnover can be analyzed descriptively, but it should not automatically be substituted for firing.

For example, an involuntary-turnover observation may contain several employer-initiated separation mechanisms. Without a source-supported decomposition, assigning the entire quantity to firings would introduce measurement error by construction.

### 5.3 Workforce stocks provide contextual information rather than flow measurements

Four observations are classified as employment-end/workforce-stock observations.

These observations can describe workforce composition or employment levels, but they do not directly measure the number of employees entering or leaving during the period.

They can therefore provide context for employee-flow evidence without being treated as employee-flow observations.

### 5.4 Organizational reporting is heterogeneous

The evidence differs along at least four dimensions:

1. the employee-flow concept reported;
2. the group dimension reported;
3. the unit reported;
4. the reporting period.

This heterogeneity is not merely a nuisance to be eliminated. It determines which comparisons are defensible.

---

## 6. Measurement and Comparability

The central methodological implication is that harmonization should be conservative.

A source-defined quantity should enter the exploratory dataset under its original conceptual identity. Harmonization should standardize metadata and analytical structure where possible, but should not manufacture conceptual equivalence.

The distinction can be represented as:

$$
	ext{source quantity}
ightarrow
	ext{validated observation}
ightarrow
	ext{comparable subset},
$$

rather than:

$$
	ext{source quantity}
ightarrow
	ext{assumed common construct}.
$$

This approach preserves measurement uncertainty and allows later researchers to determine whether a particular subset supports a stronger comparison.

The same logic applies to the primary/secondary distinction. A source may provide valuable evidence without satisfying the requirements for the intended firing analysis. Such evidence remains useful for exploratory analysis and for identifying measurement gaps.

---

## 7. Robustness and Sensitivity Framework

The current dataset suggests several natural sensitivity exercises for subsequent versions of the analysis:

### Specification A: all evidence

Use all source-preserving observations while keeping units and flow concepts distinct.

### Specification B: count-only evidence

Restrict analysis to observations reported as counts.

### Specification C: group-specific evidence

Exclude observations that do not identify a substantive group dimension.

### Specification D: flow-only evidence

Exclude workforce-stock observations.

### Specification E: organization-level aggregation

Summarize coverage at the organization level rather than treating every source observation as an independent statistical unit.

These specifications should be understood as sensitivity analyses, not as competing attempts to obtain a preferred result.

---

## 8. Implications for Future Empirical Work

The current evidence does not justify immediately estimating a causal firing-effects model.

Instead, the next acquisition phase should target the principal information gaps:

1. Canada and Australia;
2. manufacturing;
3. healthcare;
4. retail;
5. telecommunications;
6. energy;
7. transportation;
8. consumer goods;
9. multi-year organizational reporting;
10. group-specific employer-initiated separation measures.

The approximately 50-organization target is therefore a coverage objective rather than a quota.

A future confirmatory study would require a substantially cleaner subset with sufficiently consistent definitions, repeated observations, defensible denominators where rates are used, and an explicit identification strategy.

---

## 9. Candidate Hypotheses for Later Testing

The exploratory evidence can motivate hypotheses without treating them as established results.

### H1: Reporting asymmetry

Organizations are more likely to publicly report group-specific hiring information than group-specific firing information.

### H2: Definition heterogeneity

The comparability of employee-flow observations decreases as the number of source-defined concepts and group structures increases.

### H3: Longitudinal scarcity

Public organizational reporting provides substantially less repeated group-specific flow information than would be required for a balanced longitudinal panel.

These are **candidate hypotheses generated by the exploratory stage**, not confirmed propositions.

---

## 10. Limitations

Several limitations are fundamental.

First, the sample is currently small and purposively assembled for coverage and source quality rather than statistical representativeness.

Second, the evidence is concentrated in a small number of reporting periods.

Third, organizations differ in reporting conventions, definitions, and group classifications.

Fourth, the absence of firing observations reflects lack of observed measurement and cannot be interpreted as evidence of zero firing.

Fifth, secondary evidence may be highly informative descriptively while remaining unsuitable for a particular confirmatory specification.

Finally, the present study is observational and descriptive. It does not establish causal effects.

---

## 11. Conclusion

The first exploratory evidence layer demonstrates that group-specific employee-flow information is observable, but unevenly and under heterogeneous definitions.

The current dataset contains 108 observations across seven organizations. Hires are substantially represented, employee turnover is also represented, workforce-stock information provides contextual observations, and other separations appear in limited form. Directly observed group-specific firing counts are currently absent.

The principal contribution of this stage is therefore methodological as much as substantive: it establishes a source-preserving empirical architecture in which measurement availability, definition heterogeneity, missingness, and comparability are themselves observable features of the data.

The appropriate next step is not to infer unobserved firing counts. It is to expand the evidence strategically, quantify comparability, perform reproducible exploratory analysis, and identify subsets capable of supporting stronger future tests.

The exploratory stage thus provides the bridge between the measurement framework of Paper 1, the theoretical framework of Paper 2, and any later confirmatory empirical study.
