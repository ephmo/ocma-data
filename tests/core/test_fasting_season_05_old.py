"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 5: ["Old Calendar", "3-16", "4-24"]
    (
        "2031-3-25",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # FISH_ALLOWED, Monday
    (
        "2015-3-25",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # FISH_ALLOWED, Tuesday
    (
        "2004-3-25",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # FISH_ALLOWED, Wednesday
    (
        "2061-3-25",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # FISH_ALLOWED, Thursday
    (
        "2034-3-25",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # FISH_ALLOWED, Friday
    (
        "2018-3-25",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # FISH_ALLOWED, Saturday
    (
        "2010-3-16",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2010-3-17",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Tuesday
    (
        "2010-3-18",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "2010-3-19",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Thursday
    (
        "2010-3-20",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "6",
            "fasting_monks_index": "6",
        },
    ),  # Friday
    (
        "2010-3-21",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Saturday
    (
        "2041-4-2",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2041-4-7",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Saturday
    (
        "2078-4-19",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2078-4-24",
        "old",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Saturday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
