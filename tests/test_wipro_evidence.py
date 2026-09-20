from pathlib import Path
import csv


def read_rows() -> list[dict[str, str]]:
    path = Path("metadata/organization_source_evidence.csv")
    with path.open(encoding="utf-8", newline="") as handle:
        return [
            row
            for row in csv.DictReader(handle)
            if row["organization_id"] == "IND003"
        ]


def test_wipro_has_group_specific_hire_evidence():
    rows = read_rows()
    assert rows
    assert any(
        row["flow_concept"] == "hires"
        and row["evidence_type"] == "new_hire_count"
        and row["unit"] == "count"
        for row in rows
    )


def test_wipro_attrition_is_not_relabelled_as_firings():
    rows = read_rows()
    attrition_rows = [
        row for row in rows if row["flow_concept"] == "employee_turnover"
    ]
    assert attrition_rows
    assert all(row["flow_concept"] != "firings" for row in attrition_rows)
    assert all(row["screening_status"] == "Secondary" for row in attrition_rows)
