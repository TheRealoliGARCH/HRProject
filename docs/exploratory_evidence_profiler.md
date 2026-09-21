# Exploratory Evidence Profiler

The exploratory pipeline begins at the **evidence layer**, before any count-panel admission.

The profiler provides descriptive summaries of the evidence already acquired:

- observation count;
- organization coverage;
- source coverage;
- flow-concept coverage;
- units;
- measurement status;
- screening status;
- group dimensions.

It deliberately does **not**:

- convert percentages to counts;
- convert turnover into firings;
- infer zeros from missing observations;
- collapse source-defined concepts;
- infer causality;
- decide that an organization belongs in the primary panel.

This creates the first reproducible EDA layer:

```
organization_source_evidence.csv
        |
        v
evidence profiler
        |
        +--> coverage
        +--> flow concepts
        +--> units
        +--> measurement status
        +--> group dimensions
        |
        v
subsequent harmonization / EDA
```

The profiler is therefore descriptive infrastructure, not an estimation procedure.
