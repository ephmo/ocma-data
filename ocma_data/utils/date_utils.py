"""Utility functions for date manipulation, validation, comparison, and formatting."""

from datetime import date, datetime, timedelta


def date_to_string(current_date: date) -> str:
    """Convert a given date into a string."""
    return current_date.strftime("%Y-%m-%d").replace("-0", "-")


def is_date_before(current_date: date, comparison_date: date) -> bool:
    """Check if the given date comes before another specified date."""
    return current_date < comparison_date


def is_date_in_range(current_date: date, start_date: date, end_date: date) -> bool:
    """Check if the given date is within the specified range."""
    if start_date <= end_date:
        return start_date <= current_date <= end_date
    else:
        return current_date >= start_date or current_date <= end_date


def is_date_in_tuple(month_day: str, comparison_tuple: tuple[str, ...]) -> bool:
    """Check if the given date is in a given tuple."""
    return month_day in comparison_tuple


def is_valid_date(current_year: int, current_month: int, current_day: int) -> bool:
    """Check if the provided date string is a valid date."""
    try:
        date(current_year, current_month, current_day)
    except ValueError:
        return False
    else:
        return True


def modify_date(current_date: date, number_days: int) -> date:
    """Modify a given date by adding or subtracting a number of days."""
    return current_date + timedelta(days=number_days)


def string_to_date(current_date: str) -> date:
    """Convert a given string into a date."""
    return datetime.strptime(current_date, "%Y-%m-%d").date()
