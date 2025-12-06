"""Test for fasting subpackage."""

import pytest

from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

test_cases = [
    # Maximum range for each fasting season
    # Format: ["Calendar", "Start Month-Day", "End Month-Day"]
    # Fasting season 11: ["New Calendar", "12-25", "1-6"]
    (
        "1924-12-25",
        "new",
        {
            "fasting_season_index": "11",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Thursday
    (
        "1924-1-5",
        "new",
        {
            "fasting_season_index": "11",
            "fasting_laymen_index": "4",
            "fasting_monks_index": "4",
        },
    ),  # STRICT_FAST, Saturday
    (
        "1924-1-6",
        "new",
        {
            "fasting_season_index": "11",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Sunday
    (
        "2099-12-25",
        "new",
        {
            "fasting_season_index": "11",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Friday
    (
        "2099-1-5",
        "new",
        {
            "fasting_season_index": "11",
            "fasting_laymen_index": "5",
            "fasting_monks_index": "5",
        },
    ),  # STRICT_FAST, Monday
    (
        "2099-1-6",
        "new",
        {
            "fasting_season_index": "11",
            "fasting_laymen_index": "1",
            "fasting_monks_index": "2",
        },
    ),  # Tuesday
]


@pytest.mark.parametrize("current_date, calendar_style, expected", test_cases)
def test_get_fasting(current_date: str, calendar_style: str, expected: str) -> None:
    """Test for get_fasting."""
    assert get_fasting(string_to_date(current_date), calendar_style) == expected
