"""Test for moon_phase subpackage."""

import pytest

from ocma_data.core.moon_phase.logic import get_moon_phase
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    ("1924-01-09", "old", "3"),
    ("1924-12-28", "old", "3"),
    ("2024-12-24", "old", "2"),
    ("2025-11-28", "old", "4"),
    ("2099-01-08", "old", "1"),
    ("2099-12-14", "old", "3"),
    ("2099-12-21", "old", "4"),
    ("2099-12-28", "old", "1"),
    ("1924-01-06", "new", "1"),
    ("1924-12-26", "new", "1"),
    ("2025-01-06", "new", "2"),
    ("2025-12-11", "new", "4"),
    ("2099-01-07", "new", "3"),
    ("2099-12-27", "new", "3"),
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_moon_phase(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_moon_phase."""
    assert get_moon_phase(string_to_date(current_date), calendar_style) == expected
