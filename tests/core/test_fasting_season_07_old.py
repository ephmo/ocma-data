"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 7: ["Old Calendar", "5-10", "6-20"]
    (
        "2010-5-10",
        "old",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2010-5-11",
        "old",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Monday
    (
        "2010-5-12",
        "old",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Tuesday
    (
        "2010-5-17",
        "old",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2041-5-27",
        "old",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2041-5-30",
        "old",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Wednesday
    (
        "2041-5-31",
        "old",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Thursday
    (
        "2041-6-3",
        "old",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2078-6-13",
        "old",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2078-6-18",
        "old",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Friday
    (
        "2078-6-19",
        "old",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Saturday
    (
        "2078-6-20",
        "old",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
