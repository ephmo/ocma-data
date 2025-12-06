"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 9: ["Old Calendar", "8-1", "8-14"]
    (
        "1924-8-1",
        "old",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Thursday
    (
        "1924-8-6",
        "old",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Tuesday
    (
        "1924-8-10",
        "old",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "1924-8-11",
        "old",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "1924-8-12",
        "old",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "1924-8-13",
        "old",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Tuesday
    (
        "1924-8-14",
        "old",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "2099-8-1",
        "old",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Friday
    (
        "2099-8-6",
        "old",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Wednesday
    (
        "2099-8-14",
        "old",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Thursday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
