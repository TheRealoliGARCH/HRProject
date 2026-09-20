# Source acquisition protocol

## Objective
Construct the first defensible version of the heterogeneous organization panel without conditioning source selection on empirical outcomes.

## India
The Labour Bureau is the primary official Indian benchmark source family.

QES is an establishment-based survey covering establishments with 10 or more workers across nine selected sectors. It is used for employment-change benchmarks rather than automatically treated as organization-level demographic flow data.

ASI is the principal source of Indian industrial statistics and includes labour statistics such as employment, labour cost, absenteeism and labour turnover. The current Labour Bureau report list extends through ASI 2023-24.

Indian Labour Statistics provides historical national labour-market context.

Industrial-dispute, closure, retrenchment and lay-off statistics provide a separate employer-initiated separation benchmark.

## United States
JOLTS is a benchmark source for hires and separations. Its separation categories are quits, layoffs and discharges, and other separations. BLS defines layoffs and discharges as involuntary separations initiated by the employer and explicitly includes firings among that broader category. The repository therefore stores the published JOLTS measure as `layoffs_and_discharges_bls` and does not rename or decompose it into `firings` without a separately documented firing observation or defensible official derivation. This distinction is part of the pre-specified measurement protocol.

## Organization sources
Preferred sources, in descending order of directness:
1. regulatory filings or official workforce reports;
2. official company workforce disclosures;
3. audited reports containing workforce-flow information;
4. government establishment records where legally available;
5. documented secondary sources only when the underlying definition can be verified.

## Inclusion
An organization becomes eligible for the primary panel only when the required fields and definitions can be documented for the relevant period.

## Exclusion
Do not exclude an organization because its measured flow is inconvenient or unusual.

Exclude or place in the secondary dataset when group definitions cannot be harmonized, employment denominators are unavailable, flow categories are irreconcilable, source provenance cannot be established, or firing/separation data are too ambiguous for the intended specification.

## Provenance
Every imported observation must carry source_id, source title, source URL or stable document identifier, retrieval date, reporting period, source definition, original value, and transformation status.

## Empirical discipline
Source acquisition rules are fixed before estimation. If a later result suggests a data problem, the observation is re-examined using the same validation rules rather than selectively rewritten.
