"""Global constants."""

from enum import IntEnum, StrEnum


class CalendarStyles(StrEnum):
    """Enumeration for Calendar Styles."""

    OLD_CALENDAR = "old"
    NEW_CALENDAR = "new"


class Weekdays(IntEnum):
    """Enumeration for Weekdays."""

    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7
