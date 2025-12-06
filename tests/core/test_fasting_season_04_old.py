"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 4: ["Old Calendar", "2-4", "4-18"]
    (
        "2024-3-25",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Sunday
    (
        "2059-3-25",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Monday
    (
        "2043-3-25",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Tuesday
    (
        "2021-3-25",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Wednesday
    (
        "2005-3-25",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Thursday
    (
        "2000-3-25",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Friday
    (
        "2035-3-25",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Saturday
    (
        "2010-2-4",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "2010-2-7",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "2010-2-8",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Sunday
    (
        "2010-3-9",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Monday
    (
        "2010-3-15",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # PALM_SUNDAY, Sunday
    (
        "2041-2-21",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "2041-2-24",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Saturday
    (
        "2041-2-25",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "2041-2-26",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2041-2-27",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Tuesday
    (
        "2041-3-1",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Thursday
    (
        "2041-3-2",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Friday
    (
        "2041-4-1",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # PALM_SUNDAY, Sunday
    (
        "2078-3-10",
        "old",
        {
            "fasting_season_index": "4",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "2078-4-18",
        "old",
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
