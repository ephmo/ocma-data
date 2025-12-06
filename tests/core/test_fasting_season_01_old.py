"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 1: ["Old Calendar", "1-11", "2-21"]
    (
        "2010-1-11",
        "old",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2010-1-12",
        "old",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Monday
    (
        "2010-1-13",
        "old",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Tuesday
    (
        "2010-1-18",
        "old",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2041-1-28",
        "old",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2041-1-31",
        "old",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Wednesday
    (
        "2041-2-1",
        "old",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Thursday
    (
        "2041-2-4",
        "old",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2078-2-14",
        "old",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2078-2-19",
        "old",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Friday
    (
        "2078-2-20",
        "old",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Saturday
    (
        "2078-2-21",
        "old",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
