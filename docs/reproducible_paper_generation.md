# Reproducible Paper Generation

Paper 3 is generated as LaTeX source from the source-preserving evidence CSV rather than maintained as a manually edited statistical narrative.

From the repository root, run:

```bash
python scripts/generate_paper.py
```

The command reads:

`metadata/organization_source_evidence.csv`

and writes:

`outputs/exploratory_paper.tex`

The generator computes observation counts, organization coverage, flow-concept counts, unit counts, and reporting-period counts directly from the evidence. It does not infer missing values, convert percentages into counts, or relabel source-defined concepts.

The generated artifact is a complete `article`-class LaTeX document using the `booktabs` package for tables. It can be compiled independently with a standard LaTeX installation.

The generator is the source of all numerical values in the generated paper. Tests verify the current evidence totals and the source-preserving behavior.
