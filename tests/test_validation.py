from hrproject.validation import validate_row


def test_valid_observation():
    row = {
        "employment_begin": 100,
        "employment_end": 110,
        "hires": 20,
        "firings": 10,
        "measurement_status": "reported",
        "firing_quality": "directly_reported",
    }
    assert validate_row(row) == []


def test_negative_firing_is_rejected():
    row = {
        "employment_begin": 100,
        "employment_end": 110,
        "hires": 20,
        "firings": -1,
        "measurement_status": "reported",
        "firing_quality": "directly_reported",
    }
    errors = validate_row(row)
    assert any("firings" in error for error in errors)


def test_missing_firing_is_not_zero():
    row = {
        "employment_begin": 100,
        "employment_end": 110,
        "hires": 20,
        "firings": None,
        "measurement_status": "missing",
        "firing_quality": "missing",
    }
    assert validate_row(row) == []


def test_unreported_firing_cannot_be_silently_zero():
    row = {
        "employment_begin": 100,
        "employment_end": 110,
        "hires": 20,
        "firings": None,
        "measurement_status": "reported",
        "firing_quality": "directly_reported",
    }
    errors = validate_row(row)
    assert any("missing firing count" in error for error in errors)


def test_invalid_quality_is_rejected():
    row = {
        "employment_begin": 100,
        "employment_end": 110,
        "hires": 20,
        "firings": 10,
        "measurement_status": "reported",
        "firing_quality": "invented",
    }
    errors = validate_row(row)
    assert any("firing_quality" in error for error in errors)


def test_jolts_aggregate_is_not_a_firing_measure():
    row = {
        "source_id": "US_JOLTS",
        "flow_concept": "firings",
        "layoffs_and_discharges_bls": 25,
        "firings": None,
        "measurement_status": "reported",
        "firing_quality": "missing",
    }
    errors = validate_row(row)
    assert any("cannot be relabeled as firings" in error for error in errors)


def test_jolts_aggregate_is_valid_as_its_own_concept():
    row = {
        "source_id": "US_JOLTS",
        "flow_concept": "layoffs_and_discharges_bls",
        "layoffs_and_discharges_bls": 25,
        "firings": None,
        "measurement_status": "reported",
        "firing_quality": "missing",
    }
    assert validate_row(row) == []
