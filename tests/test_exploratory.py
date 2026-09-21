from hrproject.exploratory import (
    evidence_profile,
    flow_concept_counts,
    measurement_status_counts,
    organization_coverage,
)


def rows():
    return [
        {
            "organization_id": "IND002",
            "source_id": "ORG_PUBLIC",
            "flow_concept": "hires",
            "unit": "count",
            "measurement_status": "reported",
            "screening_status": "Secondary",
            "group_dimension": "gender",
        },
        {
            "organization_id": "IND002",
            "source_id": "ORG_PUBLIC",
            "flow_concept": "employee_turnover",
            "unit": "percent",
            "measurement_status": "reported",
            "screening_status": "Secondary",
            "group_dimension": "gender",
        },
        {
            "organization_id": "UK001",
            "source_id": "ORG_PUBLIC",
            "flow_concept": "employee_turnover",
            "unit": "count",
            "measurement_status": "reported",
            "screening_status": "Secondary",
            "group_dimension": "age",
        },
    ]


def test_profile_describes_evidence_without_recasting_units():
    result = evidence_profile(rows())
    assert result["observation_count"] == 3
    assert result["organizations"] == 2
    assert result["flow_concepts"]["hires"] == 1
    assert result["flow_concepts"]["employee_turnover"] == 2
    assert result["units"]["percent"] == 1
    assert result["units"]["count"] == 2


def test_flow_concept_counts_preserve_source_concepts():
    result = flow_concept_counts(rows())
    assert result == {"hires": 1, "employee_turnover": 2}


def test_measurement_status_counts_are_descriptive_only():
    assert measurement_status_counts(rows()) == {"reported": 3}


def test_organization_coverage_counts_evidence_rows():
    assert organization_coverage(rows()) == {"IND002": 2, "UK001": 1}
