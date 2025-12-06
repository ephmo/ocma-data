"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 8: ["New Calendar", "5-31", "6-28"]
    (
        "2010-5-31",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2010-6-5",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Saturday
    (
        "2010-6-6",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Sunday
    (
        "2010-6-8",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Tuesday
    (
        "2010-6-11",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # WINE_AND_OLIVE_OIL_ALLOWED, Friday
    (
        "2010-6-19",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Saturday
    (
        "2010-6-20",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Sunday
    (
        "2010-6-24",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Thursday
    (
        "2010-6-26",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "2010-6-27",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "2010-6-28",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2041-6-17",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2041-6-18",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Tuesday
    (
        "2041-6-19",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "2041-6-20",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Thursday
    (
        "2041-6-22",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Saturday
    (
        "2041-6-23",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # Sunday
    (
        "2041-6-24",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Monday
    (
        "2041-6-28",
        "new",
        {
            "fasting_season_index": "8",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Friday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
