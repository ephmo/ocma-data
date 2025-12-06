"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 1: ["New Calendar", "1-24", "3-6"]
    (
        "2010-1-24",
        "new",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2010-1-25",
        "new",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Monday
    (
        "2010-1-26",
        "new",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Tuesday
    (
        "2010-1-31",
        "new",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2041-2-10",
        "new",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2041-2-13",
        "new",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Wednesday
    (
        "2041-2-14",
        "new",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Thursday
    (
        "2041-2-17",
        "new",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2078-2-27",
        "new",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2078-3-4",
        "new",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Friday
    (
        "2078-3-5",
        "new",
        {
            "fasting_season_index": "1",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Saturday
    (
        "2078-3-6",
        "new",
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
