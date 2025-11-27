"""Module providing a function to calculate the date of Pascha.

This calculation uses the Jacques Oudin algorithm for the given year.
"""

from datetime import date

from ocma_data.constants import CalendarStyles
from ocma_data.utils.date_utils import date_to_string, modify_date


def calculate_pascha(current_year: int, calendar_style: str) -> str:
    """Calculate the date of Pascha for the given year."""
    golden_number = current_year % 19
    epact = (19 * golden_number + 15) % 30
    century_offset = (current_year + current_year // 4 + epact) % 7
    paschal_full_moon = epact - century_offset
    easter_month = 3 + (paschal_full_moon + 40) // 44
    easter_day = paschal_full_moon + 28 - 31 * (easter_month // 4)

    julian_pascha_date = date(current_year, easter_month, easter_day)

    if calendar_style == CalendarStyles.OLD_CALENDAR.value:
        return date_to_string(julian_pascha_date)

    if calendar_style == CalendarStyles.NEW_CALENDAR.value:
        return date_to_string(modify_date(julian_pascha_date, 13))

    return ""
