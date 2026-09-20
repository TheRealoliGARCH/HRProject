from pathlib import Path
from hrproject.bls_metadata import load_jolts_metadata, normalize_series_metadata

def write_metadata_fixture(directory: Path) -> None:
    (directory / "jt.series").write_text(
        "series_id\tseasonal\tindustry_code\tseries_title\tfootnote_codes\n"
        "JTS000000000000000HIL\tS\t000000\tHires Level\t\n", encoding="utf-8")
    (directory / "jt.industry").write_text(
        "industry_code\tindustry_text\n000000\tTotal nonfarm\n", encoding="utf-8")
    (directory / "jt.period").write_text(
        "period\tperiod_abbr\tperiod_name\nM01\tJan\tJanuary\n", encoding="utf-8")
    (directory / "jt.seasonal").write_text(
        "seasonal_code\tseasonal_text\nS\tSeasonally Adjusted\n", encoding="utf-8")

def test_load_metadata_reads_available_files(tmp_path):
    write_metadata_fixture(tmp_path)
    assert set(load_jolts_metadata(tmp_path)) == {"series", "industry", "period", "seasonal"}

def test_normalize_series_metadata_joins_source_metadata(tmp_path):
    write_metadata_fixture(tmp_path)
    rows = normalize_series_metadata(tmp_path)
    assert rows[0]["industry_industry_text"] == "Total nonfarm"
    assert rows[0]["seasonal_seasonal_text"] == "Seasonally Adjusted"
    assert rows[0]["series_title"] == "Hires Level"

def test_normalize_series_metadata_does_not_invent_missing_metadata(tmp_path):
    (tmp_path / "jt.series").write_text(
        "series_id\tseasonal\tindustry_code\tseries_title\nX\tS\t999999\tExample\n",
        encoding="utf-8")
    rows = normalize_series_metadata(tmp_path)
    assert "industry_industry_text" not in rows[0]
