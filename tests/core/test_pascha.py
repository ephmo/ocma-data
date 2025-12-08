"""Test for pascha subpackage."""

import pytest

from ocma_data.core.pascha.logic import calculate_pascha

test_cases = [
    (1923, "old", "1923-3-26"),
    (1923, "new", "1923-4-8"),
    (1924, "old", "1924-4-14"),
    (1924, "new", "1924-4-27"),
    (2010, "old", "2010-3-22"),
    (2010, "new", "2010-4-4"),
    (2025, "old", "2025-4-7"),
    (2025, "new", "2025-4-20"),
    (2078, "old", "2078-4-25"),
    (2078, "new", "2078-5-8"),
    (2099, "old", "2099-3-30"),
    (2099, "new", "2099-4-12"),
]


@pytest.mark.parametrize("current_year, calendar_style, expected", test_cases)
def test_calculate_pascha(current_year: int, calendar_style: str, expected: str) -> None:
    """Test for calculate_pascha."""
    assert calculate_pascha(current_year, calendar_style) == expected
