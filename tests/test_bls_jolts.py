from pathlib import Path
from hrproject.bls_jolts import parse_flow_file, parse_jolts_directory

def write_fixture(path: Path) -> None:
    path.write_text(
        "series_id\tyear\tperiod\tvalue\tfootnote_codes\n"
        "JTS000000000000000HIL\t2025\tM01\t123.4\t\n"
        "JTS000000000000000HIL\t2025\tM02\t125.0\t\n",
        encoding="utf-8",
    )

def test_parse_flow_preserves_concept(tmp_path):
    path = tmp_path / "jt.data.6.LayoffsDischarges"
    write_fixture(path)
    rows = parse_flow_file(path, "layoffs_and_discharges_bls")
    assert len(rows) == 2
    assert rows[0]["flow_concept"] == "layoffs_and_discharges_bls"
    assert rows[0]["value"] == 123.4
    assert rows[0]["source_id"] == "US_JOLTS"

def test_parser_does_not_create_firings(tmp_path):
    path = tmp_path / "jt.data.6.LayoffsDischarges"
    write_fixture(path)
    rows = parse_flow_file(path, "layoffs_and_discharges_bls")
    assert all(row["flow_concept"] != "firings" for row in rows)

def test_parse_directory_uses_supported_files(tmp_path):
    write_fixture(tmp_path / "jt.data.3.Hires")
    write_fixture(tmp_path / "jt.data.6.LayoffsDischarges")
    rows = parse_jolts_directory(tmp_path)
    concepts = {row["flow_concept"] for row in rows}
    assert concepts == {"hires", "layoffs_and_discharges_bls"}
