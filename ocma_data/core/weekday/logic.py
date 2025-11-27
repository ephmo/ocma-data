"""Module providing a function that calculate the moon phase for a given date."""

from datetime import date

from ocma_data.constants import CalendarStyles
from ocma_data.utils.date_utils import modify_date


def get_weekday(current_date: date, calendar_style: str) -> str:
    """Get the weekday (1-based index) for a given date."""
    if calendar_style == CalendarStyles.OLD_CALENDAR.value:
        return str(modify_date(current_date, 13).isoweekday())

    if calendar_style == CalendarStyles.NEW_CALENDAR.value:
        return str(current_date.isoweekday())

    return ""
