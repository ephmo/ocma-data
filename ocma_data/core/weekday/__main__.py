"""Subpackage for calculating the weekday of a given date."""

import argparse
from datetime import date

from ocma_data.constants import CalendarStyles
from ocma_data.core.weekday.logic import get_weekday
from ocma_data.utils.date_utils import string_to_date

OLD = CalendarStyles.OLD_CALENDAR.value
NEW = CalendarStyles.NEW_CALENDAR.value


def valid_date(value: str) -> date:
    """Validate the given year."""
    try:
        parsed_date = string_to_date(value)

    except ValueError as err:
        raise argparse.ArgumentTypeError(f"Invalid date format: '{value}'. Use YYYY-MM-DD.") from err
    return parsed_date


def main():
    """Parse arguments and print the weekday for the given date and calendar."""
    parser = argparse.ArgumentParser(description="Calculate the weekday.")
    parser.add_argument(
        "-d",
        "--date",
        type=valid_date,
        required=True,
        help="The date for which to calculate the weekday",
    )
    parser.add_argument(
        "-c",
        "--calendar",
        choices=[OLD, NEW],
        required=True,
        help=f"Calendar style: '{OLD}' or '{NEW}'",
    )
    args = parser.parse_args()

    print(get_weekday(args.date, args.calendar))


if __name__ == "__main__":
    main()
