"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 2: ["New Calendar", "2-8", "3-20"]
    (
        "2010-2-8",
        "new",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Monday
    (
        "2010-2-9",
        "new",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Tuesday
    (
        "2010-2-14",
        "new",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2041-2-25",
        "new",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Monday
    (
        "2041-2-27",
        "new",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Wednesday
    (
        "2041-2-28",
        "new",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Thursday
    (
        "2041-3-3",
        "new",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2078-3-14",
        "new",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Monday
    (
        "2078-3-18",
        "new",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Friday
    (
        "2078-3-19",
        "new",
        {
            "fasting_season_index": "2",
            "fasting_laymen_index": "2",
            "fasting_monks_index": "2",
        },
    ),  # Saturday
    (
        "2078-3-20",
        "new",
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
