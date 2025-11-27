"""Test for pascha_distance subpackage."""

import pytest

from ocma_data.core.pascha_distance.logic import pascha_distance
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    ("1923-01-01", "old", "-84"),
    ("1923-01-01", "new", "-97"),
    ("1923-12-31", "old", "280"),
    ("1923-12-31", "new", "267"),
    ("1924-01-01", "old", "-104"),
    ("1924-01-01", "new", "-117"),
    ("1924-12-31", "old", "261"),
    ("1924-12-31", "new", "248"),
    ("2025-04-21", "new", "1"),
    ("2025-04-04", "old", "-3"),
    ("2025-04-24", "new", "4"),
    ("2025-04-05", "old", "-2"),
    ("2025-04-25", "new", "5"),
    ("2025-04-06", "old", "-1"),
    ("2025-04-26", "new", "6"),
    ("2025-04-07", "old", "0"),
    ("2025-04-27", "new", "7"),
    ("2099-01-01", "old", "-88"),
    ("2099-01-01", "new", "-101"),
    ("2099-12-31", "old", "276"),
    ("2099-12-31", "new", "263"),
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_pascha_distance(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for pascha_distance."""
    assert pascha_distance(string_to_date(current_date), calendar_style) == expected
