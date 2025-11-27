"""Module providing a function that calculate the moon phase for a given date."""

from datetime import date

from ocma_data.core.pascha.logic import calculate_pascha
from ocma_data.utils.date_utils import string_to_date


def pascha_distance(current_date: date, calendar_style: str) -> str:
    """Calculate the number of days between a given date and Pascha."""
    pascha_date = string_to_date(calculate_pascha(current_date.year, calendar_style))
    delta_date = current_date - pascha_date

    return str(delta_date.days)
