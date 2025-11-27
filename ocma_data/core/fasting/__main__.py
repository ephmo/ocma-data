"""Subpackage for fasting rules calculations."""

import argparse
from datetime import date

from ocma_data.cli.constants import CLIConstants
from ocma_data.constants import CalendarStyles
from ocma_data.core.fasting.logic import get_fasting
from ocma_data.utils.date_utils import string_to_date

YEAR_START = CLIConstants().YEAR_START
YEAR_END = CLIConstants().YEAR_END - 1
OLD = CalendarStyles.OLD_CALENDAR.value
NEW = CalendarStyles.NEW_CALENDAR.value


def valid_date(value: str) -> date:
    """Validate the given year."""
    try:
        parsed_date = string_to_date(value)

    except ValueError as err:
        raise argparse.ArgumentTypeError(
            f"Invalid date format: '{value}'. Use YYYY-MM-DD."
        ) from err

    if not (YEAR_START <= parsed_date.year <= YEAR_END):
        raise argparse.ArgumentTypeError(
            f"Year must be between {YEAR_START} and {YEAR_END}."
        )
    return parsed_date


def main():
    """Parse arguments and print the fasting rules for the given date and calendar."""
    parser = argparse.ArgumentParser(description="Calculate the fasting rules.")
    parser.add_argument(
        "-d",
        "--date",
        type=valid_date,
        required=True,
        help="Date to calculate the fasting rules",
    )
    parser.add_argument(
        "-c",
        "--calendar",
        choices=[OLD, NEW],
        required=True,
        help=f"Calendar style: '{OLD}' or '{NEW}'",
    )
    args = parser.parse_args()

    print(get_fasting(args.date, args.calendar))


if __name__ == "__main__":
    main()
