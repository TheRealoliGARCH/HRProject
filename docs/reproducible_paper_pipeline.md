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
outputs/exploratory_paper.tex
        |
        v
(optional) LaTeX compilation
```

The generated paper is deterministic conditional on the input evidence file and generator version.

The generator produces LaTeX source, not Markdown. This keeps the computational data pipeline separate from final typesetting and permits the generated source to be reviewed, versioned, and compiled independently.
