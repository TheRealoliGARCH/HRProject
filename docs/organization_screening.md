# Organization Screening Protocol

The organization registry is a candidate universe, not an empirical dataset. No organization is admitted to the primary panel merely because it is large, public, or known to publish diversity information.

## Primary-panel admission

An organization may be marked `eligible_primary_panel=Yes` only after source verification establishes, for a common and documented time window:

1. An identifiable organization-level unit.
2. At least one reproducible group definition.
3. Employment stocks or denominators needed to construct Paper 1's group-specific employee flow rates.
4. Group-specific hiring observations.
5. Group-specific firing observations, or a source-defined involuntary-separation measure that can be mapped without changing the source definition.
6. Sufficient separation information to distinguish voluntary from employer-initiated flows where the analysis requires it.
7. A documented reference period.
8. Source provenance sufficient to reproduce the observation.
9. Definitions that remain comparable across the organization's observation period.
10. No silent conversion of missing observations into zero.

## Firing variable rule

The registry must preserve the source's terminology. A source category such as "layoffs and discharges" must not be renamed "firings" merely to fit the analysis. For example, U.S. JOLTS defines layoffs and discharges as a broader category that includes firings, layoffs, and other employer-initiated involuntary separations. Such observations can be stored under the source-defined field and mapped to an analytical category only with an explicit mapping rule.

## Screening outcomes

Use the following outcomes:

- `Eligible`: all primary-panel requirements verified.
- `Secondary`: useful for benchmarks or robustness, but not sufficient for the primary organization-level panel.
- `Pending`: candidate requires source verification.
- `Excluded`: fails a pre-specified inclusion rule.

Screening decisions must be based on data and definition requirements, not on the observed direction or magnitude of group-specific flows.

## Current registry status

The initial registry contains candidate organizations across India, the United States, the United Kingdom, Canada, and Australia. All entries are currently `Pending`; no group-specific observations are implied by their inclusion.
