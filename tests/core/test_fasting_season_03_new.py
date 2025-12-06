"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 3: ["New Calendar", "2-15", "3-22"]
    (
        "2010-2-15",
        "new",
        {
            "fasting_season_index": "3",
            "fasting_laymen_index": "6",
            "fasting_monks_index": "6",
        },
    ),  # Monday
    (
        "2010-2-16",
        "new",
        {
            "fasting_season_index": "3",
            "fasting_laymen_index": "6",
            "fasting_monks_index": "6",
        },
    ),  # Tuesday
    (
        "2041-3-4",
        "new",
        {
            "fasting_season_index": "3",
            "fasting_laymen_index": "6",
            "fasting_monks_index": "6",
        },
    ),  # Monday
    (
        "2041-3-5",
        "new",
        {
            "fasting_season_index": "3",
            "fasting_laymen_index": "6",
            "fasting_monks_index": "6",
        },
    ),  # Tuesday
    (
        "2078-3-21",
        "new",
        {
            "fasting_season_index": "3",
            "fasting_laymen_index": "6",
            "fasting_monks_index": "6",
        },
    ),  # Monday
    (
        "2078-3-22",
        "new",
        {
            "fasting_season_index": "3",
            "fasting_laymen_index": "6",
            "fasting_monks_index": "6",
        },
    ),  # Tuesday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
