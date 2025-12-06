"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 8: ["Old Calendar", "5-18", "6-28"]
    (
        "2010-5-18",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2010-5-19",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Tuesday
    (
        "2010-5-20",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "2010-5-21",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Thursday
    (
        "2010-5-22",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Friday
    (
        "2010-5-23",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Saturday
    (
        "2010-5-24",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Sunday
    (
        "2010-5-25",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Monday
    (
        "2010-6-8",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Monday
    (
        "2010-6-11",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Thursday
    (
        "2010-6-20",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Saturday
    (
        "2010-6-21",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Sunday
    (
        "2010-6-24",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Wednesday
    (
        "2010-6-27",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "2010-6-28",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "2041-6-4",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2041-6-8",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Friday
    (
        "2041-6-9",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Saturday
    (
        "2041-6-10",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Sunday
    (
        "2041-6-11",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Monday
    (
        "2041-6-23",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Saturday
    (
        "2041-6-24",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Sunday
    (
        "2041-6-28",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Thursday
    (
        "2078-6-21",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2078-6-24",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Thursday
    (
        "2078-6-26",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "2078-6-27",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "2078-6-28",
        "old",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
