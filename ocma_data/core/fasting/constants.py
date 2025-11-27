"""Constants related to Orthodox fasting rules."""

from enum import IntEnum, StrEnum


class FastingLevels(IntEnum):
    """Enumeration for fasting levels."""

    NO_FASTING = 1
    DAIRY_PRODUCTS_ALLOWED = 2
    FISH_ALLOWED = 3
    WINE_AND_OLIVE_OIL_ALLOWED = 4
    STRICT_FAST = 5
    ABSOLUTE_FAST = 6


class FastingSeasons(IntEnum):
    """Enumeration for fasting seasons."""

    FIRST_WEEK_OF_THE_TRIODION = 1
    CHEESEFARE_WEEK = 2
    THREE_DAY_FAST = 3
    GREAT_LENT = 4
    HOLY_WEEK = 5
    BRIGHT_WEEK = 6
    WEEK_OF_THE_HOLY_SPIRIT = 7
    APOSTLES_FAST = 8
    DORMITION_FAST = 9
    NATIVITY_FAST = 10
    TWELVE_DAY_FAST_FREE = 11
    REGULAR_SEASON = 12


class PaschaDistanceBefore(IntEnum):
    """Enumeration for PaschaDistanceBefore."""

    FIRST_WEEK_OF_THE_TRIODION = -70
    CHEESEFARE_WEEK = -55
    THREE_DAY_FAST = -48
    GREAT_LENT = -46
    HOLY_WEEK = -6
    BRIGHT_WEEK = 0
    WEEK_OF_THE_HOLY_SPIRIT = 49
    APOSTLES_FAST = 57


class PaschaDistanceAfter(IntEnum):
    """Enumeration for PaschaDistanceAfter."""

    FIRST_WEEK_OF_THE_TRIODION = -63
    CHEESEFARE_WEEK = -49
    THREE_DAY_FAST = -47
    GREAT_LENT = -7
    HOLY_WEEK = -1
    BRIGHT_WEEK = 7
    WEEK_OF_THE_HOLY_SPIRIT = 56


class DateMovable(IntEnum):
    """Enumeration for DateMovable."""

    PALM_SUNDAY = -7
    MIDFEAST_OF_PENTECOST = 24
    LEAVETAKING_OF_PASCHA = 38


class DateFixed(StrEnum):
    """Enumeration for DateFixed."""

    TWELVE_DAY_FAST_FREE_AFTER = "1-6"
    NATIVITY_OF_THE_BAPTIST = "6-24"
    APOSTLES_FAST = "6-29"
    DORMITION_FAST_BEFORE = "8-1"
    DORMITION_FAST_AFTER = "8-14"
    NATIVITY_FAST_BEFORE = "11-15"
    THE_ENTRANCE_OF_THE_THEOTOKOS = "11-21"
    SAINT_SPYRIDON = "12-12"
    NATIVITY_FAST_AFTER = "12-24"
    TWELVE_DAY_FAST_FREE_BEFORE = "12-25"


STRICT_FAST = ("1-5", "8-29", "9-14", "12-24")
WINE_AND_OLIVE_OIL_ALLOWED = (
    "1-11",
    "1-16",
    "1-17",
    "1-18",
    "1-20",
    "1-22",
    "1-25",
    "1-27",
    "1-30",
    "2-8",
    "2-10",
    "2-11",
    "2-17",
    "2-24",
    "3-9",
    "4-23",
    "4-25",
    "4-30",
    "5-2",
    "5-8",
    "5-15",
    "5-21",
    "5-25",
    "6-8",
    "6-11",
    "6-30",
    "7-1",
    "7-2",
    "7-17",
    "7-20",
    "7-22",
    "7-25",
    "7-26",
    "7-27",
    "8-31",
    "9-1",
    "9-9",
    "9-13",
    "9-20",
    "9-23",
    "9-26",
    "10-6",
    "10-18",
    "10-23",
    "10-26",
    "11-1",
    "11-8",
    "11-12",
    "11-13",
    "11-16",
    "11-25",
    "11-30",
    "12-4",
    "12-5",
    "12-6",
    "12-9",
    "12-12",
    "12-15",
    "12-17",
    "12-20",
)
FISH_ALLOWED = (
    "1-7",
    "2-2",
    "3-25",
    "6-24",
    "6-29",
    "8-6",
    "8-15",
    "9-8",
    "11-14",
    "11-21",
)
