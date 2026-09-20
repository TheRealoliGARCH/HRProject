from pathlib import Path
import csv


def read_rows() -> list[dict[str, str]]:
    path = Path("metadata/organization_source_evidence_infosys.csv")
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_infosys_has_group_specific_hire_and_turnover_evidence():
    rows = read_rows()
    assert rows
    assert any(row["organization_id"] == "IND002" for row in rows)
    assert any(
        row["flow_concept"] == "hires"
        and row["evidence_type"] == "new_hire_count"
        for row in rows
    )
    assert any(
        row["flow_concept"] == "employee_turnover"
        and row["evidence_type"] == "employee_turnover_count"
        for row in rows
    )


def test_infosys_turnover_is_not_relabelled_as_firings():
    rows = read_rows()
    turnover_rows = [
        row for row in rows if row["flow_concept"] == "employee_turnover"
    ]
    assert turnover_rows
    assert all(row["flow_concept"] != "firings" for row in turnover_rows)
    assert all(row["screening_status"] == "Secondary" for row in turnover_rows)
