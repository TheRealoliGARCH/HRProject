from hrproject.harmonization import harmonize_row, harmonize_rows


def valid_analysis_row() -> dict[str, object]:
    return {
        "organization_id": "IND002",
        "country": "India",
        "industry": "Information Technology",
        "year": 2021,
        "group_id": "gender_female",
        "group_definition": "Women employees as defined by the source.",
        "employment_begin": 100,
        "employment_end": 105,
        "hires": 20,
        "firings": 5,
        "quits": 8,
        "layoffs": None,
        "layoffs_and_discharges_bls": None,
        "other_separations": 2,
        "flow_concept": "firings",
        "source_id": "ORG_PUBLIC",
        "measurement_status": "reported",
        "firing_quality": "directly_reported",
        "source_definition": "Source-defined group-specific employee flows.",
        "notes": "",
        "observation_unit": "count",
    }


def test_analysis_row_is_harmonized_without_rewriting_source_fields():
    row = valid_analysis_row()
    result = harmonize_row(row)
    assert result["organization_id"] == "IND002"
    assert result["group_id"] == "gender_female"
    assert result["firings"] == 5
    assert result["source_definition"] == row["source_definition"]


def test_percentage_evidence_is_not_admitted_as_a_count():
    row = valid_analysis_row()
    row["observation_unit"] = "percent"
    row["hires"] = 35.2
    row["firings"] = None
    row["measurement_status"] = "missing"
    row["firing_quality"] = "missing"
    try:
        harmonize_row(row)
    except ValueError as exc:
        assert "count observations" in str(exc)
    else:
        raise AssertionError("percentage evidence must not enter the count panel")


def test_missing_firing_remains_missing():
    row = valid_analysis_row()
    row["firings"] = None
    row["measurement_status"] = "missing"
    row["firing_quality"] = "missing"
    result = harmonize_row(row)
    assert result["firings"] is None


def test_jolts_broad_category_is_not_relabelled():
    row = valid_analysis_row()
    row["source_id"] = "US_JOLTS"
    row["flow_concept"] = "layoffs_and_discharges_bls"
    row["layoffs_and_discharges_bls"] = 25
    row["firings"] = None
    row["firing_quality"] = "missing"
    result = harmonize_row(row)
    assert result["flow_concept"] == "layoffs_and_discharges_bls"
    assert result["firings"] is None


def test_duplicate_organization_group_year_is_rejected():
    row = valid_analysis_row()
    try:
        harmonize_rows([row, dict(row)])
    except ValueError as exc:
        assert "duplicate analysis observation" in str(exc)
    else:
        raise AssertionError("duplicate organization-group-year observations must fail")
