"""Module providing a function that calculate the moon phase for a given date."""

from datetime import date

from ocma_data.constants import CalendarStyles
from ocma_data.core.moon_phase.constants import MOON_PHASES
from ocma_data.utils.date_utils import modify_date


def get_moon_phase(current_date: date, calendar_style: str) -> str:
    """Calculate the moon phase for a given date."""

    def find_moon_phase(
        modified_year: int,
        modified_month: int,
        modified_day: int,
    ) -> str:
        """Determine the moon phase for a given date."""
        phase_map = {
            "new_moon": "1",
            "first_quarter": "2",
            "full_moon": "3",
            "last_quarter": "4",
        }
        date_key = f"{modified_month}-{modified_day}"

        for phase, value in phase_map.items():
            if date_key in MOON_PHASES.get(str(modified_year), {}).get(phase, []):
                return value

        return ""

    if calendar_style == CalendarStyles.OLD_CALENDAR.value:
        modified_date = modify_date(current_date, 13)
        return find_moon_phase(
            modified_date.year,
            modified_date.month,
            modified_date.day,
        )

    if calendar_style == CalendarStyles.NEW_CALENDAR.value:
        return find_moon_phase(
            current_date.year,
            current_date.month,
            current_date.day,
        )

    return ""
