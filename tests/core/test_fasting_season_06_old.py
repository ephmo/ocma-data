"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 6: ["Old Calendar", "3-22", "5-2"]
    (
        "2010-3-22",
        "old",
        {
            "fasting_season_index": "6",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2010-3-23",
        "old",
        {
            "fasting_season_index": "6",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Monday
    (
        "2010-3-24",
        "old",
        {
            "fasting_season_index": "6",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Tuesday
    (
        "2010-3-29",
        "old",
        {
            "fasting_season_index": "6",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2041-4-8",
        "old",
        {
            "fasting_season_index": "6",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2041-4-11",
        "old",
        {
            "fasting_season_index": "6",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Wednesday
    (
        "2041-4-12",
        "old",
        {
            "fasting_season_index": "6",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Thursday
    (
        "2041-4-15",
        "old",
        {
            "fasting_season_index": "6",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2078-4-25",
        "old",
        {
            "fasting_season_index": "6",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2078-4-30",
        "old",
        {
            "fasting_season_index": "6",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Friday
    (
        "2078-5-1",
        "old",
        {
            "fasting_season_index": "6",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Saturday
    (
        "2078-5-2",
        "old",
        {
            "fasting_season_index": "6",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
