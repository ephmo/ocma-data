"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 7: ["New Calendar", "5-23", "7-3"]
    (
        "2010-5-23",
        "new",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2010-5-24",
        "new",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Monday
    (
        "2010-5-25",
        "new",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Tuesday
    (
        "2010-5-30",
        "new",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2041-6-9",
        "new",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2041-6-12",
        "new",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Wednesday
    (
        "2041-6-13",
        "new",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Thursday
    (
        "2041-6-16",
        "new",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2078-6-26",
        "new",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2078-7-1",
        "new",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Friday
    (
        "2078-7-2",
        "new",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Saturday
    (
        "2078-7-3",
        "new",
        {
            "fasting_season_index": "7",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
