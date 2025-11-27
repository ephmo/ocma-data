"""Test for date subpackage."""

import pytest

from ocma_data.core.date.logic import get_date
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    ("1924-01-01", "old", {"date_old": "1924-1-1", "date_new": "1924-1-14"}),
    ("1924-01-01", "new", {"date_old": "1923-12-19", "date_new": "1924-1-1"}),
    ("1924-12-31", "old", {"date_old": "1924-12-31", "date_new": "1925-1-13"}),
    ("1924-12-31", "new", {"date_old": "1924-12-18", "date_new": "1924-12-31"}),
    ("2025-04-29", "old", {"date_old": "2025-4-29", "date_new": "2025-5-12"}),
    ("2025-04-29", "new", {"date_old": "2025-4-16", "date_new": "2025-4-29"}),
    ("2099-01-01", "old", {"date_old": "2099-1-1", "date_new": "2099-1-14"}),
    ("2099-01-01", "new", {"date_old": "2098-12-19", "date_new": "2099-1-1"}),
    ("2099-12-31", "old", {"date_old": "2099-12-31", "date_new": "2100-1-13"}),
    ("2099-12-31", "new", {"date_old": "2099-12-18", "date_new": "2099-12-31"}),
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_date(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_date."""
    assert get_date(string_to_date(current_date), calendar_style) == expected
