from hrproject.organization_screening import (
    primary_panel_requirements,
    validate_screening_record,
)


def valid_record() -> dict[str, str]:
    return {
        "organization_id": "IND001",
        "organization_unit": "Corporate workforce",
        "group_id": "group_a",
        "group_definition": "Source-defined group A",
        "period_start": "2020",
        "period_end": "2025",
        "employment_denominator": "Annual workforce count",
        "hiring_source": "Official workforce report",
        "firing_source": "Official workforce report",
        "separation_source": "Official workforce report",
        "source_definition": "Source-defined employee flow categories.",
        "provenance_status": "verified",
        "definition_consistency": "verified",
        "measurement_status": "reported",
        "screening_status": "Eligible",
        "screening_rationale": "All required source and definition evidence verified.",
    }


def test_valid_screening_record():
    assert validate_screening_record(valid_record()) == []


def test_invalid_status_is_rejected():
    record = valid_record()
    record["screening_status"] = "Preferred"
    assert "invalid screening_status: 'Preferred'" in validate_screening_record(record)


def test_screening_does_not_infer_eligibility():
    record = valid_record()
    record["firing_source"] = ""
    flags = primary_panel_requirements(record)
    assert flags["firing_source"] is False
    assert record["screening_status"] == "Eligible"


def test_empty_source_definition_is_rejected():
    record = valid_record()
    record["source_definition"] = ""
    assert "source_definition cannot be empty" in validate_screening_record(record)
