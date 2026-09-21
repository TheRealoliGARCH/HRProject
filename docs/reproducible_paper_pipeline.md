# Reproducible Paper Pipeline

```
metadata/organization_source_evidence.csv
        |
        v
src/hrproject/paper.py
        |
        v
scripts/generate_paper.py
        |
        v
outputs/generated_exploratory_paper.tex
        |
        v
(optional) LaTeX compilation
```

The generated paper is deterministic conditional on the input evidence file and generator version.

The generator produces LaTeX source, not Markdown. The generated source is kept separate from the human-reviewed publication source, preserving a deliberate editorial checkpoint while keeping the computational data pipeline reproducible.
