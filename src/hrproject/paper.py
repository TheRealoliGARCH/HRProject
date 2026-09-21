"""Deterministic generator for the exploratory Paper 3.

The generator reads source-preserving evidence and computes all reported
coverage statistics from the current CSV. It does not infer missing values,
recast source-defined concepts, or convert units.
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from typing import Iterable, Mapping


DEFAULT_EVIDENCE = Path("metadata/organization_source_evidence.csv")
DEFAULT_OUTPUT = Path("outputs/exploratory_paper.md")


def load_evidence(path: Path = DEFAULT_EVIDENCE) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def counts(rows: Iterable[Mapping[str, str]], field: str) -> dict[str, int]:
    return dict(Counter(row.get(field, "") for row in rows if row.get(field, "")))


def profile(rows: list[Mapping[str, str]]) -> dict[str, object]:
    return {
        "observation_count": len(rows),
        "organization_count": len({r["organization_id"] for r in rows if r.get("organization_id")}),
        "organizations": sorted({r["organization_id"] for r in rows if r.get("organization_id")}),
        "flow_concepts": counts(rows, "flow_concept"),
        "units": counts(rows, "unit"),
        "reporting_periods": counts(rows, "reporting_period"),
        "screening_status": counts(rows, "screening_status"),
        "measurement_status": counts(rows, "measurement_status"),
        "group_dimensions": counts(rows, "group_dimension"),
    }


def _table(mapping: Mapping[str, int], label: str) -> str:
    lines = [f"| {label} | Observations |", "| --- | ---: |"]
    lines.extend(f"| {key} | {value} |" for key, value in mapping.items())
    return "\n".join(lines)


def generate_paper(rows: list[Mapping[str, str]]) -> str:
    p = profile(rows)
    flows = p["flow_concepts"]
    units = p["units"]
    periods = p["reporting_periods"]
    n = p["observation_count"]
    orgs = p["organization_count"]
    count_units = units.get("count", 0)
    noncount = n - count_units

    return f"""# Exploratory Analysis of Group-Specific Employee Flows

## Abstract

This paper develops an exploratory data-science analysis of publicly reported group-specific employee-flow evidence across heterogeneous organizations. The current evidence layer contains **{n} observations from {orgs} organizations**. The study preserves source-defined concepts, units, provenance, and missingness rather than assuming conceptual equivalence across organizations. The current evidence contains **{flows.get("hires", 0)} hire observations**, **{flows.get("employee_turnover", 0)} employee-turnover observations**, **{flows.get("employment_end", 0)} employment-end/workforce-stock observations**, and **{flows.get("other_separations", 0)} other-separation observations**. Directly observed group-specific firing observations are currently absent. The paper therefore treats measurement availability and comparability as empirical objects and does not interpret exploratory patterns as causal effects.

**Keywords:** employee flows; employee turnover; group-specific measurement; exploratory data science; workforce composition; organizational reporting; measurement uncertainty; human resources.

---

## 1. Introduction

Employee-flow research distinguishes inflows from outflows, but public organizational reporting does not necessarily expose these quantities at a common level of definition or aggregation. Organizations may report hires, attrition, turnover, layoffs, involuntary turnover, workforce stocks, or other separation measures using organization-specific definitions.

This paper treats that heterogeneity as a data problem before treating it as an estimation problem.

The study is the third component of a research program. Paper 1 develops a framework for group-specific employee-flow measurement. Paper 2 develops theoretical implications of group-specific employee flows. The present paper asks what can actually be observed in heterogeneous organizational data and how far those observations can be compared without silently changing their meanings.

The central research question is:

> **What does publicly available organizational evidence reveal about the observability, structure, and comparability of group-specific employee flows?**

The paper is explicitly exploratory. It does not assume the theoretical propositions of Paper 2, does not convert missing observations into zeros, and does not interpret descriptive associations as causal effects.

---

## 2. Conceptual Framework

The observational architecture is an organization-group-time observation:

$$
(i,g,t),
$$

where $i$ denotes an organization, $g$ an employee group, and $t$ a reporting period.

Source-defined employee-flow concepts remain distinct. Hires are inflows; quits are voluntary separations where the source defines them as such; layoffs and discharges remain under the source definition; employee turnover and attrition retain their source-defined meanings; and workforce stocks describe employment levels rather than flows.

The same principle applies to missingness:

$$
\\text{{not reported}} \\neq 0.
$$

If a source does not report a group-specific firing count, the value remains missing rather than being converted to zero.

The empirical pipeline is:

$$
\\text{{source discovery}}
\\rightarrow
\\text{{acquisition}}
\\rightarrow
\\text{{validation}}
\\rightarrow
\\text{{definition harmonization}}
\\rightarrow
\\text{{exploratory analysis}}
\\rightarrow
\\text{{robustness}}
\\rightarrow
\\text{{candidate hypotheses}}.
$$

---

## 3. Data and Sources

The current evidence layer contains **{n} observations from {orgs} organizations**. The organization registry currently spans India, the United Kingdom, the United States, Canada, and Australia, but acquired evidence is presently concentrated in India, the United Kingdom, and the United States.

All acquired organization evidence is currently classified as secondary rather than as a completed primary estimation panel.

The evidence is retained with source identifiers, document titles, reporting periods, official URLs, evidence types, group dimensions, source-defined flow concepts, units, measurement status, and notes.

### Reporting-period coverage

{_table(periods, "Reporting period")}

The evidence is therefore not a balanced annual panel.

---

## 4. Measurement Structure

### 4.1 Flow concepts

{_table(flows, "Source-defined flow concept")}

There are currently **{flows.get("firings", 0)} directly observed firing observations**.

This is a measurement-availability result, not evidence that the underlying incidence of firing is zero.

### 4.2 Units

The evidence contains **{count_units} count observations** and **{noncount} non-count observations**.

Percentage observations remain percentages. They are not converted into counts without a defensible denominator.

### 4.3 Group dimensions

The evidence contains heterogeneous group structures, including gender, age, region, employment group, turnover category, overall observations, and combinations of these dimensions. These structures are not assumed to be directly interchangeable.

---

## 5. Exploratory Findings

### 5.1 Hiring information versus firing information

The current evidence contains **{flows.get("hires", 0)} hire observations** and **{flows.get("firings", 0)} firing observations**.

The defensible conclusion is about reporting availability: the current evidence provides substantially more observable group-specific hiring information than group-specific firing information.

The data do not establish whether the underlying incidence of firing is low, high, stable, or heterogeneous.

### 5.2 Turnover is observable but conceptually heterogeneous

Employee-turnover observations account for **{flows.get("employee_turnover", 0)} observations**. Turnover may be reported as counts or rates and may be voluntary, involuntary, or total depending on the source.

Turnover should therefore not automatically be substituted for firing.

### 5.3 Workforce stocks provide contextual information

Employment-end/workforce-stock observations account for **{flows.get("employment_end", 0)} observations**. These describe employment levels or composition and do not directly measure the number of employees entering or leaving during the period.

### 5.4 Organizational reporting is heterogeneous

The evidence differs in flow concept, group dimension, unit, and reporting period. This heterogeneity determines which comparisons are defensible.

---

## 6. Measurement and Comparability

Harmonization should be conservative.

A source-defined quantity enters the exploratory dataset under its original conceptual identity. Harmonization standardizes metadata and analytical structure where possible, but does not manufacture conceptual equivalence.

The distinction is:

$$
\\text{{source quantity}}
\\rightarrow
\\text{{validated observation}}
\\rightarrow
\\text{{comparable subset}},
$$

rather than:

$$
\\text{{source quantity}}
\\rightarrow
\\text{{assumed common construct}}.
$$

This preserves measurement uncertainty and allows later analysis to identify subsets supporting stronger comparison.

---

## 7. Robustness and Sensitivity Framework

The evidence supports several sensitivity exercises:

1. **All evidence:** retain source-preserving observations while keeping concepts and units distinct.
2. **Count-only evidence:** restrict analysis to count observations.
3. **Group-specific evidence:** exclude observations without a substantive group dimension.
4. **Flow-only evidence:** exclude workforce-stock observations.
5. **Organization-level summaries:** summarize coverage by organization rather than treating evidence rows as independent statistical units.

These are sensitivity specifications, not competing attempts to obtain a preferred result.

---

## 8. Implications for Future Empirical Work

The current evidence does not justify immediately estimating a causal firing-effects model.

The next acquisition phase should target measurement gaps, particularly:

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

The approximately 50-organization target remains a coverage objective rather than a quota.

---

## 9. Candidate Hypotheses for Later Testing

The exploratory evidence motivates, but does not establish, candidate hypotheses:

### H1: Reporting asymmetry

Organizations may be more likely to publicly report group-specific hiring information than group-specific firing information.

### H2: Definition heterogeneity

Comparability may decrease as the number of source-defined concepts and group structures increases.

### H3: Longitudinal scarcity

Public organizational reporting may provide substantially less repeated group-specific flow information than would be required for a balanced longitudinal panel.

These hypotheses require later testing.

---

## 10. Limitations

The current sample is small and assembled for coverage and source quality rather than statistical representativeness. Evidence is concentrated in a small number of reporting periods, organizations differ in definitions and group classifications, and the current data do not provide directly observed group-specific firing counts.

The absence of firing observations reflects lack of observed measurement and cannot be interpreted as evidence of zero firing.

The study is observational and descriptive. It does not establish causal effects.

---

## 11. Conclusion

The current exploratory evidence demonstrates that group-specific employee-flow information is observable, but unevenly and under heterogeneous definitions.

The evidence layer contains **{n} observations across {orgs} organizations**. Hiring information is substantially represented, employee turnover is also observable, workforce-stock information provides contextual observations, and other separations appear in limited form. Directly observed group-specific firing counts are currently absent.

The contribution of this stage is methodological as much as substantive: it establishes a source-preserving empirical architecture in which measurement availability, definition heterogeneity, missingness, and comparability are observable features of the data.

The next step is to expand the evidence strategically, quantify comparability, perform reproducible exploratory analysis, and identify subsets capable of supporting stronger future tests.
"""


def write_paper(
    evidence_path: Path = DEFAULT_EVIDENCE,
    output_path: Path = DEFAULT_OUTPUT,
) -> Path:
    rows = load_evidence(evidence_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(generate_paper(rows), encoding="utf-8")
    return output_path
