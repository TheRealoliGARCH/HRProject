# Current Exploratory Evidence Coverage Report

## Scope

This report profiles the **106 evidence observations** currently recorded in `metadata/organization_source_evidence.csv` on `main`.

The evidence covers **7 organizations**:

- India: 5
- United Kingdom: 1
- United States: 1

All seven organizations are currently classified as **Secondary**. The report therefore describes the acquired evidence; it does not treat the organizations as a completed primary estimation panel.

## Flow-concept coverage

| Source-defined flow concept | Evidence observations |
| --- | ---: |
| hires | 55 |
| employee_turnover | 46 |
| employment_end | 4 |
| other_separations | 1 |
| firings | 0 |

The absence of firing observations is an important measurement result. No firing count has been inferred from turnover, attrition, layoffs, workforce stocks, or other separation measures.

## Unit coverage

The acquired evidence contains both count and non-count observations.

- Count observations: 95
- Percentage / percentage-like observations: 11

Percentage observations remain percentages. They are not converted into counts.

## Group-dimension coverage

The evidence includes multiple group structures:

- gender
- age
- region
- employment group
- turnover category
- overall
- combined dimensions such as employment group + gender + age and region + age + gender

This is already heterogeneous enough to support exploratory comparisons, but the dimensions are not directly interchangeable. For example, gender-by-region-by-age observations should not be treated as equivalent to a simple gender observation.

## Organization-level coverage

| Organization | Country | Evidence profile |
| --- | --- | --- |
| TCS | India | hires distribution, workforce composition, attrition |
| Infosys | India | group-specific hires and turnover counts, workforce stock, turnover rate |
| Wipro | India | group-specific hires, attrition, workforce composition |
| HCLTech | India | group-specific hires, gender turnover rates |
| Tech Mahindra | India | group-specific hires, employment-group/gender/age turnover rates |
| HSBC Holdings | UK | group-specific hires and voluntary/involuntary turnover counts |
| Alphabet | US | workforce stock |

## Measurement gaps

The current evidence layer has four immediate gaps.

### 1. Firing observations

There are currently **zero directly observed group-specific firing observations** in the acquired organization evidence.

This prevents a firing-effects regression from being the immediate next analytical step.

### 2. Country coverage

The registry contains Canada and Australia candidates, but the acquired evidence layer currently contains no Canadian or Australian organization.

### 3. Industry coverage

The current acquired organizations are concentrated in information technology and financial services. Additional acquisition should therefore deliberately expand industry coverage.

### 4. Temporal coverage

The evidence is concentrated in FY2018-19 and FY2024-25/FY2025, with limited longitudinal organization-level coverage. A useful next acquisition wave should prioritize organizations with multiple comparable reporting periods.

## Exploratory interpretation

The data currently support an exploratory study of **heterogeneous employee-flow measurement**, particularly:

1. group-specific hiring patterns;
2. source-defined turnover patterns;
3. workforce-stock composition;
4. differences in group dimensions across organizations;
5. differences in reporting practices;
6. measurement availability and missingness.

They do **not** yet support a general empirical claim about group-specific firing effects.

## Acquisition rule for the next wave

The next organizations should be selected to fill information gaps rather than simply increase the organization count.

Priority dimensions:

1. Canada and Australia;
2. manufacturing, healthcare, retail, telecommunications, energy, transportation, and consumer goods;
3. multi-year reporting;
4. group-specific separation measures;
5. group-specific employer-initiated separation measures;
6. richer age/gender/organizational group cross-classifications.

The approximate 50-organization target remains a coverage objective, not a quota.

## Pipeline position

```
Evidence acquisition
        |
        v
CURRENT COVERAGE PROFILE  <-- this report
        |
        v
Gap-directed acquisition
        |
        v
Harmonized exploratory dataset
        |
        v
EDA and visualization
        |
        v
Candidate hypotheses
        |
        v
Optional confirmatory analysis
```
