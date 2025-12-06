"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 5: ["New Calendar", "3-29", "5-7"]
    (
        "2010-3-29",
        "new",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2010-3-30",
        "new",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Tuesday
    (
        "2010-3-31",
        "new",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Wednesday
    (
        "2010-4-1",
        "new",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Thursday
    (
        "2010-4-2",
        "new",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "6",
            "fasting_monks_index": "6",
        },
    ),  # Friday
    (
        "2010-4-3",
        "new",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Saturday
    (
        "2041-4-15",
        "new",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2041-4-20",
        "new",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Saturday
    (
        "2078-5-2",
        "new",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Monday
    (
        "2078-5-7",
        "new",
        {
            "fasting_season_index": "5",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # Saturday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
