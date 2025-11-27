"""Test for weekday subpackage."""

import pytest

from ocma_data.core.weekday.logic import get_weekday
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    ("1924-01-01", "old", "1"),
    ("1924-01-01", "new", "2"),
    ("1924-12-31", "old", "2"),
    ("1924-12-31", "new", "3"),
    ("2025-04-21", "new", "1"),
    ("2025-04-04", "old", "4"),
    ("2025-04-24", "new", "4"),
    ("2025-04-05", "old", "5"),
    ("2025-04-25", "new", "5"),
    ("2025-04-06", "old", "6"),
    ("2025-04-26", "new", "6"),
    ("2025-04-07", "old", "7"),
    ("2025-04-27", "new", "7"),
    ("2099-01-01", "old", "3"),
    ("2099-01-01", "new", "4"),
    ("2099-12-31", "old", "3"),
    ("2099-12-31", "new", "4"),
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_weekday(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_weekday."""
    assert get_weekday(string_to_date(current_date), calendar_style) == expected
