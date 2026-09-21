from pathlib import Path

from hrproject.paper import generate_paper, load_evidence, profile


ROOT = Path(__file__).parents[1]
EVIDENCE = ROOT / "metadata/organization_source_evidence.csv"


def test_current_evidence_profile():
    rows = load_evidence(EVIDENCE)
    result = profile(rows)
    assert result["observation_count"] == 108
    assert result["organization_count"] == 7
    assert result["flow_concepts"]["hires"] == 55
    assert result["flow_concepts"]["employee_turnover"] == 48
    assert result["flow_concepts"]["employment_end"] == 4
    assert result["flow_concepts"]["other_separations"] == 1
    assert result["flow_concepts"].get("firings", 0) == 0
    assert result["units"]["count"] == 96


def test_generator_emits_latex():
    rows = [
        {"organization_id": "A", "flow_concept": "hires", "unit": "count",
         "reporting_period": "Y1", "screening_status": "Secondary",
         "measurement_status": "reported", "group_dimension": "gender"},
        {"organization_id": "A", "flow_concept": "employee_turnover", "unit": "percent",
         "reporting_period": "Y1", "screening_status": "Secondary",
         "measurement_status": "reported", "group_dimension": "gender"},
    ]
    paper = generate_paper(rows)
    assert paper.startswith(r"\documentclass{article}")
    assert "outputs/exploratory_paper.tex" not in paper
    assert r"\usepackage{booktabs}" in paper
    assert r"\begin{document}" in paper
    assert r"\section{Introduction}" in paper
    assert "| hires | 1 |" not in paper
    assert "0 directly observed firing observations" in paper


def test_generator_does_not_recast_missing_firings():
    rows = [{
        "organization_id": "A",
        "flow_concept": "hires",
        "unit": "count",
        "reporting_period": "Y1",
        "screening_status": "Secondary",
        "measurement_status": "reported",
        "group_dimension": "gender",
    }]
    paper = generate_paper(rows)
    assert r"0 directly observed firing observations" in paper


def test_latex_escaping_preserves_generated_commands():
    from hrproject.paper import _escape

    assert _escape(r"source\\name") == r"source\\textbackslash{}name"
    assert _escape("a_b") == r"a\\_b"
    assert _escape("a{b}") == r"a\\{b\\}"
