"""Subpackage for Paschal date calculations."""

import argparse

from ocma_data.cli.constants import CLIConstants
from ocma_data.constants import CalendarStyles
from ocma_data.core.pascha.logic import calculate_pascha

YEAR_START = CLIConstants().YEAR_START
YEAR_END = CLIConstants().YEAR_END - 1
OLD = CalendarStyles.OLD_CALENDAR.value
NEW = CalendarStyles.NEW_CALENDAR.value


def valid_year(value: str) -> int:
    """Validate the given year."""
    parsed_year = int(value)
    if not (YEAR_START - 1 <= parsed_year <= YEAR_END):
        raise argparse.ArgumentTypeError(
            f"Year must be between {YEAR_START - 1} and {YEAR_END}."
        )
    return parsed_year


def main():
    """Parse arguments and print the Paschal date for the given year and calendar."""
    parser = argparse.ArgumentParser(description="Calculate the Paschal date.")
    parser.add_argument(
        "-y",
        "--year",
        type=valid_year,
        required=True,
        help=f"Year to calculate Pascha ({YEAR_START - 1} - {YEAR_END})",
    )
    parser.add_argument(
        "-c",
        "--calendar",
        choices=[OLD, NEW],
        required=True,
        help=f"Calendar style: '{OLD}' or '{NEW}'",
    )
    args = parser.parse_args()

    print(calculate_pascha(args.year, args.calendar))


if __name__ == "__main__":
    main()
