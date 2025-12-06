"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 10: ["Old Calendar", "11-15", "12-24"]
    (
        "1924-11-15",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Friday
    (
        "1924-11-16",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Saturday
    (
        "1924-11-17",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "1924-11-18",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "1924-11-19",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Tuesday
    (
        "1924-11-20",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "1924-11-21",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Thursday
    (
        "1924-11-23",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Saturday
    (
        "1924-11-24",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Sunday
    (
        "1924-11-25",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Monday
    (
        "1924-11-30",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Saturday
    (
        "1924-12-4",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Wednesday
    (
        "1924-12-5",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Thursday
    (
        "1924-12-6",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Friday
    (
        "1924-12-7",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Saturday
    (
        "1924-12-8",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Sunday
    (
        "1924-12-9",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Monday
    (
        "1924-12-12",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Thursday
    (
        "1924-12-14",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "1924-12-15",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Sunday
    (
        "1924-12-17",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Tuesday
    (
        "1924-12-20",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Friday
    (
        "1924-12-21",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "1924-12-22",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "1924-12-24",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # STRICT_FAST, Tuesday
    (
        "2099-11-15",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "2099-11-16",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Sunday
    (
        "2099-11-20",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Thursday
    (
        "2099-11-21",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Friday
    (
        "2099-11-22",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Saturday
    (
        "2099-11-23",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Sunday
    (
        "2099-11-25",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Tuesday
    (
        "2099-11-30",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Sunday
    (
        "2099-12-4",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Thursday
    (
        "2099-12-5",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Friday
    (
        "2099-12-6",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Saturday
    (
        "2099-12-7",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Sunday
    (
        "2099-12-9",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Tuesday
    (
        "2099-12-12",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Friday
    (
        "2099-12-13",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "2099-12-14",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "2099-12-15",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Monday
    (
        "2099-12-17",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Wednesday
    (
        "2099-12-20",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Saturday
    (
        "2099-12-21",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "2024-12-24",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # STRICT_FAST, Monday
    (
        "2099-12-24",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # STRICT_FAST, Wednesday
    (
        "2027-12-24",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # STRICT_FAST, Thursday
    (
        "2033-12-24",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # STRICT_FAST, Friday
    (
        "2028-12-24",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # STRICT_FAST, Saturday
    (
        "2029-12-24",
        "old",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # STRICT_FAST, Sunday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
