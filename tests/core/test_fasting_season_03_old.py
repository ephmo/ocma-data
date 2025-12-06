"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 3: ["Old Calendar", "2-2", "3-9"]
    (
        "2010-2-2",
        "old",
        {
            "fasting_season_index": "3",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # FISH_ALLOWED, Monday
    (
        "2010-2-3",
        "old",
        {
            "fasting_season_index": "3",
            "fasting_laymen_index": "6",
            "fasting_monks_index": "6",
        },
    ),  # Tuesday
    (
        "2041-2-19",
        "old",
        {
            "fasting_season_index": "3",
            "fasting_laymen_index": "6",
            "fasting_monks_index": "6",
        },
    ),  # Monday
    (
        "2041-2-20",
        "old",
        {
            "fasting_season_index": "3",
            "fasting_laymen_index": "6",
            "fasting_monks_index": "6",
        },
    ),  # Tuesday
    (
        "2078-3-8",
        "old",
        {
            "fasting_season_index": "3",
            "fasting_laymen_index": "6",
            "fasting_monks_index": "6",
        },
    ),  # Monday
    (
        "2078-3-9",
        "old",
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
