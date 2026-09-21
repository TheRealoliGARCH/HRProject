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


def test_generator_uses_computed_values():
    rows = [
        {"organization_id": "A", "flow_concept": "hires", "unit": "count",
         "reporting_period": "Y1", "screening_status": "Secondary",
         "measurement_status": "reported", "group_dimension": "gender"},
        {"organization_id": "A", "flow_concept": "employee_turnover", "unit": "percent",
         "reporting_period": "Y1", "screening_status": "Secondary",
         "measurement_status": "reported", "group_dimension": "gender"},
    ]
    paper = generate_paper(rows)
    assert "2 observations from 1 organizations" in paper
    assert "| hires | 1 |" in paper
    assert "| employee_turnover | 1 |" in paper
    assert "0 firing observations" in paper


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
    assert "firing observations**" in paper
    assert "0" in paper
