import re
import sys
import os
import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import only the pure functions we can test without Streamlit runtime / secrets
from app import (
    sanitize_input,
    generate_tracking_id,
    parse_department_and_letter,
    MAX_INPUT_CHARS,
)


def test_sanitize_input_strips_control_chars():
    dirty = "Hello\x00World\x0b Test"
    result = sanitize_input(dirty)
    assert "\x00" not in result
    assert "\x0b" not in result
    assert "Hello" in result and "World" in result


def test_sanitize_input_enforces_max_length():
    long_text = "a" * (MAX_INPUT_CHARS + 500)
    result = sanitize_input(long_text)
    assert len(result) == MAX_INPUT_CHARS


def test_sanitize_input_handles_none():
    assert sanitize_input(None) == ""


def test_sanitize_input_strips_whitespace():
    assert sanitize_input("   hello world   ") == "hello world"


def test_generate_tracking_id_format():
    tid = generate_tracking_id()
    pattern = r"^NGR-\d{8}-\d{5}$"
    assert re.match(pattern, tid), f"Tracking ID '{tid}' does not match expected format"


def test_generate_tracking_id_contains_todays_date():
    tid = generate_tracking_id()
    today_str = datetime.datetime.now().strftime("%Y%m%d")
    assert today_str in tid


def test_generate_tracking_id_uniqueness():
    ids = {generate_tracking_id() for _ in range(50)}
    # Extremely unlikely to collide across 50 generations; sanity check randomness
    assert len(ids) > 1


def test_parse_department_and_letter_standard_format():
    raw_output = "DEPARTMENT: Roads & Infrastructure (PWD)\n\nDear Sir/Madam,\nThis is a formal complaint."
    department, letter = parse_department_and_letter(raw_output)
    assert department == "Roads & Infrastructure (PWD)"
    assert "Dear Sir/Madam" in letter


def test_parse_department_and_letter_fallback_format():
    raw_output = "Department: Water Supply\nDear Sir,\nComplaint body here."
    department, letter = parse_department_and_letter(raw_output)
    assert "Water Supply" in department
    assert "Complaint body here" in letter


def test_parse_department_and_letter_no_department_marker():
    raw_output = "Just a plain letter with no department marker at all."
    department, letter = parse_department_and_letter(raw_output)
    assert department == "General Civic Department"
    assert letter == raw_output


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-v"]))
