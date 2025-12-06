"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 9: ["New Calendar", "8-1", "8-14"]
    (
        "1924-8-1",
        "new",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Friday
    (
        "1924-8-3",
        "new",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Sunday
    (
        "1924-8-6",
        "new",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Wednesday
    (
        "1924-8-14",
        "new",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Thursday
    (
        "2099-8-1",
        "new",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # Saturday
    (
        "2099-8-3",
        "new",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2099-8-4",
        "new",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Tuesday
    (
        "2099-8-5",
        "new",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "2099-8-6",
        "new",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "3",
            "fasting_monks_index": "3",
        },
    ),  # FISH_ALLOWED, Thursday
    (
        "2099-8-14",
        "new",
        {
            "fasting_season_index": "9",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Friday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
