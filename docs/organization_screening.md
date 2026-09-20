# Organization Screening Protocol

The organization registry is a candidate universe, not an empirical dataset. PR #5 makes the screening protocol operational without admitting any candidate to the empirical panel.

## Screening record

Each group-level screening record should document:

1. the organization and organizational unit;
2. a stable group identifier and source-defined group definition;
3. the reference period;
4. the employment denominator required for Paper 1 flow rates;
5. evidence for group-specific hiring;
6. evidence for group-specific firing, or an explicitly mapped source-defined involuntary-separation measure;
7. separation information needed for the intended specification;
8. source-defined terminology;
9. provenance;
10. cross-period definition consistency;
11. a pre-specified screening outcome and rationale.

The schema is stored in metadata/organization_screening_schema.csv.

## Screening outcomes

Use only:

- Eligible: all primary-panel requirements verified.
- Secondary: useful for benchmarks or robustness, but insufficient for the primary organization-level panel.
- Pending: source verification remains incomplete.
- Excluded: fails a pre-specified inclusion rule.

The screening code validates these categories but does not assign an outcome automatically.

## Measurement firewall

A screening record must not transform a broad source-defined category into firings merely to satisfy the schema. The source definition remains part of the record.

The screening process also does not convert missing flow counts into zero.

## Primary-panel requirements

The helper in src/hrproject/organization_screening.py exposes requirement flags for organization unit, group definition, employment denominator, hiring evidence, firing/separation evidence, provenance, and definition consistency.

These flags are diagnostic. They are not an eligibility model and do not use observed flow magnitudes to determine admission.

## Acquisition boundary

PR #5 does not claim that organization-level observations have been acquired. The existing organization registry remains a candidate universe, and the screening records remain evidence-driven inputs for later acquisition and harmonization.
