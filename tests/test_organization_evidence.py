from pathlib import Path
import csv


def read_rows() -> list[dict[str, str]]:
    path = Path("metadata/organization_source_evidence.csv")
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_tcs_evidence_preserves_source_defined_concepts():
    rows = read_rows()
    assert rows
    assert any(row["organization_id"] == "IND001" for row in rows)
    assert any(
        row["flow_concept"] == "hires"
        and row["evidence_type"] == "new_hire_distribution"
        for row in rows
    )
    assert all(row["screening_status"] == "Secondary" for row in rows)


def test_tcs_attrition_is_not_relabelled_as_firings():
    rows = read_rows()
    attrition_rows = [
        row
        for row in rows
        if row["organization_id"] == "IND001"
        and row["evidence_type"] == "attrition"
    ]
    assert attrition_rows
    assert all(row["flow_concept"] != "firings" for row in attrition_rows)
    assert all(
        row["source_defined_measure"].startswith("IT services attrition")
        for row in attrition_rows
    )

def test_hcltech_evidence_preserves_source_defined_concepts():
    rows = read_rows()
    hcl = [row for row in rows if row["organization_id"] == "IND004"]
    assert hcl
    assert any(
        row["flow_concept"] == "hires"
        and row["evidence_type"] == "new_hire_count"
        and row["unit"] == "count"
        and row["value"] == "7829"
        for row in hcl
    )
    assert all(row["screening_status"] == "Secondary" for row in hcl)
    assert all(row["flow_concept"] != "firings" for row in hcl)
    assert all(
        row["flow_concept"] != "firings"
        for row in hcl
        if row["evidence_type"] == "turnover_rate"
    )

def test_tech_mahindra_evidence_preserves_source_defined_concepts():
    rows = read_rows()
    techm = [row for row in rows if row["organization_id"] == "IND005"]
    assert techm
    assert any(
        row["flow_concept"] == "hires"
        and row["evidence_type"] == "new_hire_count"
        and row["unit"] == "count"
        and row["value"] == "25648"
        for row in techm
    )
    assert all(row["screening_status"] == "Secondary" for row in techm)
    assert all(row["flow_concept"] != "firings" for row in techm)
    assert all(
        row["flow_concept"] != "firings"
        for row in techm
        if row["evidence_type"] == "turnover_rate"
    )

def test_hsbc_evidence_preserves_source_defined_concepts():
    rows = read_rows()
    hsbc = [row for row in rows if row["organization_id"] == "UK001"]
    assert hsbc
    assert any(
        row["flow_concept"] == "hires"
        and row["evidence_type"] == "new_hire_count"
        and row["unit"] == "count"
        and row["value"] == "12685"
        for row in hsbc
    )
    assert any(
        row["flow_concept"] == "employee_turnover"
        and row["evidence_type"] == "employee_turnover_count"
        and row["unit"] == "count"
        and row["value"] == "16683"
        for row in hsbc
    )
    assert all(row["screening_status"] == "Secondary" for row in hsbc)
    assert all(row["flow_concept"] != "firings" for row in hsbc)
    assert all(
        row["flow_concept"] != "firings"
        for row in hsbc
        if row["evidence_type"] in {"employee_turnover_count", "new_hire_count"}
    )
