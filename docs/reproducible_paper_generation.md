# Reproducible Paper Generation

Paper 3 is generated from the source-preserving evidence CSV rather than maintained as a manually edited statistical narrative.

From the repository root, run:

```bash
python scripts/generate_paper.py
```

The command reads:

`metadata/organization_source_evidence.csv`

and writes:

`outputs/exploratory_paper.md`

The generator computes observation counts, organization coverage, flow-concept counts, unit counts, and reporting-period counts directly from the evidence. It does not infer missing values, convert percentages into counts, or relabel source-defined concepts.

The generated Markdown is an analysis artifact. The checked-in draft in `docs/exploratory_paper_draft.md` remains a readable research draft, while `outputs/exploratory_paper.md` is the reproducible generated version.

Tests verify the current evidence totals and the generator's source-preserving behavior.
