"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 10: ["New Calendar", "11-15", "12-24"]
    (
        "1924-11-15",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "1924-11-16",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Sunday
    (
        "1924-11-17",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "1924-11-18",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Tuesday
    (
        "1924-11-19",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "1924-11-20",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Thursday
    (
        "1924-11-21",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Friday
    (
        "1924-11-22",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Saturday
    (
        "1924-11-23",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Sunday
    (
        "1924-11-25",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Tuesday
    (
        "1924-11-30",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Sunday
    (
        "1924-12-4",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Thursday
    (
        "1924-12-5",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Friday
    (
        "1924-12-6",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Saturday
    (
        "1924-12-7",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Sunday
    (
        "1924-12-9",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Tuesday
    (
        "1924-12-12",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Friday
    (
        "1924-12-13",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "1924-12-14",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "1924-12-15",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Monday
    (
        "1924-12-17",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Wednesday
    (
        "1924-12-20",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Saturday
    (
        "1924-12-21",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "1924-12-24",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # STRICT_FAST, Wednesday
    (
        "2099-11-15",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "2099-11-16",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Monday
    (
        "2099-11-21",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Saturday
    (
        "2099-11-22",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Sunday
    (
        "2099-11-25",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Wednesday
    (
        "2099-11-30",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Monday
    (
        "2099-12-4",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Friday
    (
        "2099-12-5",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Saturday
    (
        "2099-12-6",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Sunday
    (
        "2099-12-9",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Wednesday
    (
        "2099-12-11",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Friday
    (
        "2099-12-12",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Saturday
    (
        "2099-12-13",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "2099-12-15",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Tuesday
    (
        "2099-12-17",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Thursday
    (
        "2099-12-19",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "2099-12-20",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Sunday
    (
        "2018-12-24",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # STRICT_FAST, Monday
    (
        "2019-12-24",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # STRICT_FAST, Tuesday
    (
        "2099-12-24",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # STRICT_FAST, Thursday
    (
        "2021-12-24",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # STRICT_FAST, Friday
    (
        "2022-12-24",
        "new",
        {
            "fasting_season_index": "10",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # STRICT_FAST, Saturday
    (
        "2023-12-24",
        "new",
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
