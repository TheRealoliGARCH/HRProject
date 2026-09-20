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
