"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 4: ["New Calendar", "2-17", "5-1"]
    (
        "2040-3-25",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Sunday
    (
        "2013-3-25",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Monday
    (
        "2070-3-25",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Tuesday
    (
        "2054-3-25",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Wednesday
    (
        "2027-3-25",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Thursday
    (
        "2016-3-25",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Friday
    (
        "2062-3-25",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Saturday
    (
        "2010-2-17",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Wednesday
    (
        "2010-3-9",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Tuesday
    (
        "2010-3-28",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # PALM_SUNDAY, Sunday
    (
        "2041-3-6",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "2041-3-9",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Saturday
    (
        "2041-3-10",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "2041-3-11",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2041-3-12",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Tuesday
    (
        "2041-3-13",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "2041-3-14",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Thursday
    (
        "2041-3-15",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Friday
    (
        "2041-3-16",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "2041-4-14",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # PALM_SUNDAY, Sunday
    (
        "2078-3-23",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "2078-4-23",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Saturday
    (
        "2078-4-30",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Saturday
    (
        "2078-5-1",
        "new",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # PALM_SUNDAY, Sunday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
