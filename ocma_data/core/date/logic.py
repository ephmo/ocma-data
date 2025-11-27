"""Module providing a function that calculate the moon phase for a given date."""

from datetime import date

from ocma_data.constants import CalendarStyles
from ocma_data.utils.date_utils import date_to_string, modify_date


def get_date(current_date: date, calendar_style: str) -> dict[str, str]:
    """Convert a given date to its equivalent in both the Old and New Calendars."""
    if calendar_style == CalendarStyles.OLD_CALENDAR.value:
        return {
            "date_old": f"{date_to_string(current_date)}",
            "date_new": f"{date_to_string(modify_date(current_date, 13))}",
        }

    if calendar_style == CalendarStyles.NEW_CALENDAR.value:
        return {
            "date_old": f"{date_to_string(modify_date(current_date, -13))}",
            "date_new": f"{date_to_string(current_date)}",
        }

    return {"date_old": "", "date_new": ""}
