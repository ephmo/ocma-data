"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 2: ["Old Calendar", "1-26", "3-7"]
    (
        "2010-1-26",
        "old",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Monday
    (
        "2010-1-27",
        "old",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Tuesday
    (
        "2010-2-1",
        "old",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2041-2-12",
        "old",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Monday
    (
        "2041-2-14",
        "old",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Wednesday
    (
        "2041-2-15",
        "old",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Thursday
    (
        "2041-2-18",
        "old",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2078-3-1",
        "old",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Monday
    (
        "2078-3-5",
        "old",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Friday
    (
        "2078-3-6",
        "old",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Saturday
    (
        "2078-3-7",
        "old",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
