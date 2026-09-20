from pathlib import Path

from hrproject.bls_benchmark import build_benchmark_rows, write_benchmark_csv


def write_fixture(directory: Path) -> None:
    directory.mkdir()
    content = (
        "series_id\tyear\tperiod\tvalue\tfootnote_codes\n"
        "JTS000000000000000H\t2025\tM01\t100\t\n"
    )
    (directory / "jt.data.3.Hires").write_text(content, encoding="utf-8")
    content = (
        "series_id\tyear\tperiod\tvalue\tfootnote_codes\n"
        "JTS000000000000000Q\t2025\tM01\t40\tP\n"
    )
    (directory / "jt.data.5.Quits").write_text(content, encoding="utf-8")
    content = (
        "series_id\tyear\tperiod\tvalue\tfootnote_codes\n"
        "JTS000000000000000LD\t2025\tM01\t20\t\n"
    )
    (directory / "jt.data.6.LayoffsDischarges").write_text(content, encoding="utf-8")


def test_benchmark_preserves_bls_concepts(tmp_path):
    raw = tmp_path / "raw"
    write_fixture(raw)

    rows = build_benchmark_rows(raw)

    concepts = {row["flow_concept"] for row in rows}
    assert concepts == {"hires", "quits", "layoffs_and_discharges_bls"}
    assert not any(row["flow_concept"] == "firings" for row in rows)
    assert next(row for row in rows if row["flow_concept"] == "quits")["footnote_codes"] == "P"
    assert all(row["measurement_status"] == "observed" for row in rows)


def test_benchmark_csv_writer(tmp_path):
    raw = tmp_path / "raw"
    write_fixture(raw)
    rows = build_benchmark_rows(raw)
    output = tmp_path / "analysis" / "bls_jolts_flows.csv"

    write_benchmark_csv(rows, output)

    text = output.read_text(encoding="utf-8")
    assert "layoffs_and_discharges_bls" in text
    assert "firings" not in text.splitlines()[0]
