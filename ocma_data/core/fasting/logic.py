"""Module for calculating fasting seasons and levels."""

from datetime import date

from ocma_data.constants import Weekdays
from ocma_data.core.fasting.constants import (
    FISH_ALLOWED,
    STRICT_FAST,
    WINE_AND_OLIVE_OIL_ALLOWED,
    DateFixed,
    DateMovable,
    FastingLevels,
    FastingSeasons,
    PaschaDistanceAfter,
    PaschaDistanceBefore,
)
from ocma_data.core.pascha_distance.logic import pascha_distance
from ocma_data.core.weekday.logic import get_weekday
from ocma_data.utils.date_utils import (
    is_date_before,
    is_date_in_range,
    is_date_in_tuple,
)


def get_fasting(current_date: date, calendar_style: str) -> dict[str, str]:
    """Get the fasting_season_index, fasting_laymen_index and fasting_monks_index."""

    def comparison_date(fasting_season_date: str) -> date:
        """Get the current_date and fasting_season_date."""
        if fasting_season_date == DateFixed.TWELVE_DAY_FAST_FREE_AFTER.value:
            current_year = current_date.year + 1
        current_year = current_date.year
        return date(
            current_year,
            int(fasting_season_date.split("-")[0]),
            int(fasting_season_date.split("-")[1]),
        )

    month_day = f"{current_date.month}-{current_date.day}"
    pascha_distance_int = int(pascha_distance(current_date, calendar_style))
    weekday_int = int(get_weekday(current_date, calendar_style))

    if (
        pascha_distance_int >= PaschaDistanceBefore.FIRST_WEEK_OF_THE_TRIODION.value
        and pascha_distance_int <= PaschaDistanceAfter.FIRST_WEEK_OF_THE_TRIODION.value
    ):
        return {
            "fasting_season_index": f"{FastingSeasons.FIRST_WEEK_OF_THE_TRIODION.value}",
            "fasting_laymen_index": f"{FastingLevels.NO_FASTING.value}",
            "fasting_monks_index": f"{FastingLevels.DAIRY_PRODUCTS_ALLOWED.value}",
        }

    if (
        pascha_distance_int >= PaschaDistanceBefore.CHEESEFARE_WEEK.value
        and pascha_distance_int <= PaschaDistanceAfter.CHEESEFARE_WEEK.value
    ):
        return {
            "fasting_season_index": f"{FastingSeasons.CHEESEFARE_WEEK.value}",
            "fasting_laymen_index": f"{FastingLevels.DAIRY_PRODUCTS_ALLOWED.value}",
            "fasting_monks_index": f"{FastingLevels.DAIRY_PRODUCTS_ALLOWED.value}",
        }

    if (
        pascha_distance_int >= PaschaDistanceBefore.THREE_DAY_FAST.value
        and pascha_distance_int <= PaschaDistanceAfter.THREE_DAY_FAST.value
    ):
        if is_date_in_tuple(month_day, FISH_ALLOWED):
            return {
                "fasting_season_index": f"{FastingSeasons.THREE_DAY_FAST.value}",
                "fasting_laymen_index": f"{FastingLevels.STRICT_FAST.value}",
                "fasting_monks_index": f"{FastingLevels.STRICT_FAST.value}",
            }
        return {
            "fasting_season_index": f"{FastingSeasons.THREE_DAY_FAST.value}",
            "fasting_laymen_index": f"{FastingLevels.ABSOLUTE_FAST.value}",
            "fasting_monks_index": f"{FastingLevels.ABSOLUTE_FAST.value}",
        }

    if (
        pascha_distance_int >= PaschaDistanceBefore.GREAT_LENT.value
        and pascha_distance_int <= PaschaDistanceAfter.GREAT_LENT.value
    ):
        if (
            is_date_in_tuple(month_day, FISH_ALLOWED)
            or pascha_distance_int == DateMovable.PALM_SUNDAY.value
        ):
            return {
                "fasting_season_index": f"{FastingSeasons.GREAT_LENT.value}",
                "fasting_laymen_index": f"{FastingLevels.FISH_ALLOWED.value}",
                "fasting_monks_index": f"{FastingLevels.FISH_ALLOWED.value}",
            }

        if (
            is_date_in_tuple(month_day, WINE_AND_OLIVE_OIL_ALLOWED)
            or weekday_int == Weekdays.SAT.value
            or weekday_int == Weekdays.SUN.value
        ):
            return {
                "fasting_season_index": f"{FastingSeasons.GREAT_LENT.value}",
                "fasting_laymen_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                "fasting_monks_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
            }
        return {
            "fasting_season_index": f"{FastingSeasons.GREAT_LENT.value}",
            "fasting_laymen_index": f"{FastingLevels.STRICT_FAST.value}",
            "fasting_monks_index": f"{FastingLevels.STRICT_FAST.value}",
        }

    if (
        pascha_distance_int >= PaschaDistanceBefore.HOLY_WEEK.value
        and pascha_distance_int <= PaschaDistanceAfter.HOLY_WEEK.value
    ):
        if weekday_int == Weekdays.SAT.value:
            return {
                "fasting_season_index": f"{FastingSeasons.HOLY_WEEK.value}",
                "fasting_laymen_index": f"{FastingLevels.STRICT_FAST.value}",
                "fasting_monks_index": f"{FastingLevels.STRICT_FAST.value}",
            }
        if is_date_in_tuple(month_day, FISH_ALLOWED):
            if weekday_int == Weekdays.FRI.value:
                return {
                    "fasting_season_index": f"{FastingSeasons.HOLY_WEEK.value}",
                    "fasting_laymen_index": f"{FastingLevels.STRICT_FAST.value}",
                    "fasting_monks_index": f"{FastingLevels.STRICT_FAST.value}",
                }
            return {
                "fasting_season_index": f"{FastingSeasons.HOLY_WEEK.value}",
                "fasting_laymen_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                "fasting_monks_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
            }
        if weekday_int == Weekdays.FRI.value:
            return {
                "fasting_season_index": f"{FastingSeasons.HOLY_WEEK.value}",
                "fasting_laymen_index": f"{FastingLevels.ABSOLUTE_FAST.value}",
                "fasting_monks_index": f"{FastingLevels.ABSOLUTE_FAST.value}",
            }
        return {
            "fasting_season_index": f"{FastingSeasons.HOLY_WEEK.value}",
            "fasting_laymen_index": f"{FastingLevels.STRICT_FAST.value}",
            "fasting_monks_index": f"{FastingLevels.STRICT_FAST.value}",
        }

    if (
        pascha_distance_int >= PaschaDistanceBefore.BRIGHT_WEEK.value
        and pascha_distance_int <= PaschaDistanceAfter.BRIGHT_WEEK.value
    ):
        return {
            "fasting_season_index": f"{FastingSeasons.BRIGHT_WEEK.value}",
            "fasting_laymen_index": f"{FastingLevels.NO_FASTING.value}",
            "fasting_monks_index": f"{FastingLevels.DAIRY_PRODUCTS_ALLOWED.value}",
        }

    if (
        pascha_distance_int >= PaschaDistanceBefore.WEEK_OF_THE_HOLY_SPIRIT.value
        and pascha_distance_int <= PaschaDistanceAfter.WEEK_OF_THE_HOLY_SPIRIT.value
    ):
        return {
            "fasting_season_index": f"{FastingSeasons.WEEK_OF_THE_HOLY_SPIRIT.value}",
            "fasting_laymen_index": f"{FastingLevels.NO_FASTING.value}",
            "fasting_monks_index": f"{FastingLevels.DAIRY_PRODUCTS_ALLOWED.value}",
        }

    if (
        pascha_distance_int >= PaschaDistanceBefore.APOSTLES_FAST.value
        and is_date_before(current_date, comparison_date(DateFixed.APOSTLES_FAST.value))
    ):
        if is_date_in_tuple(month_day, FISH_ALLOWED):
            return {
                "fasting_season_index": f"{FastingSeasons.APOSTLES_FAST.value}",
                "fasting_laymen_index": f"{FastingLevels.FISH_ALLOWED.value}",
                "fasting_monks_index": f"{FastingLevels.FISH_ALLOWED.value}",
            }

        if weekday_int == Weekdays.SAT.value or weekday_int == Weekdays.SUN.value:
            if is_date_before(
                current_date, comparison_date(DateFixed.NATIVITY_OF_THE_BAPTIST.value)
            ):
                return {
                    "fasting_season_index": f"{FastingSeasons.APOSTLES_FAST.value}",
                    "fasting_laymen_index": f"{FastingLevels.FISH_ALLOWED.value}",
                    "fasting_monks_index": f"{FastingLevels.FISH_ALLOWED.value}",
                }
            return {
                "fasting_season_index": f"{FastingSeasons.APOSTLES_FAST.value}",
                "fasting_laymen_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                "fasting_monks_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
            }
        if (
            weekday_int == Weekdays.MON.value
            or weekday_int == Weekdays.WED.value
            or weekday_int == Weekdays.FRI.value
        ):
            if is_date_in_tuple(month_day, WINE_AND_OLIVE_OIL_ALLOWED):
                return {
                    "fasting_season_index": f"{FastingSeasons.APOSTLES_FAST.value}",
                    "fasting_laymen_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                    "fasting_monks_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                }
            return {
                "fasting_season_index": f"{FastingSeasons.APOSTLES_FAST.value}",
                "fasting_laymen_index": f"{FastingLevels.STRICT_FAST.value}",
                "fasting_monks_index": f"{FastingLevels.STRICT_FAST.value}",
            }
        return {
            "fasting_season_index": f"{FastingSeasons.APOSTLES_FAST.value}",
            "fasting_laymen_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
            "fasting_monks_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
        }

    if is_date_in_range(
        current_date,
        comparison_date(DateFixed.DORMITION_FAST_BEFORE.value),
        comparison_date(DateFixed.DORMITION_FAST_AFTER.value),
    ):
        if is_date_in_tuple(month_day, FISH_ALLOWED):
            return {
                "fasting_season_index": f"{FastingSeasons.DORMITION_FAST.value}",
                "fasting_laymen_index": f"{FastingLevels.FISH_ALLOWED.value}",
                "fasting_monks_index": f"{FastingLevels.FISH_ALLOWED.value}",
            }
        if weekday_int == Weekdays.SAT.value or weekday_int == Weekdays.SUN.value:
            return {
                "fasting_season_index": f"{FastingSeasons.DORMITION_FAST.value}",
                "fasting_laymen_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                "fasting_monks_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
            }
        return {
            "fasting_season_index": f"{FastingSeasons.DORMITION_FAST.value}",
            "fasting_laymen_index": f"{FastingLevels.STRICT_FAST.value}",
            "fasting_monks_index": f"{FastingLevels.STRICT_FAST.value}",
        }

    if is_date_in_range(
        current_date,
        comparison_date(DateFixed.NATIVITY_FAST_BEFORE.value),
        comparison_date(DateFixed.NATIVITY_FAST_AFTER.value),
    ):
        if is_date_in_tuple(month_day, STRICT_FAST):
            if weekday_int == Weekdays.SAT.value or weekday_int == Weekdays.SUN.value:
                return {
                    "fasting_season_index": f"{FastingSeasons.NATIVITY_FAST.value}",
                    "fasting_laymen_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                    "fasting_monks_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                }
            return {
                "fasting_season_index": f"{FastingSeasons.NATIVITY_FAST.value}",
                "fasting_laymen_index": f"{FastingLevels.STRICT_FAST.value}",
                "fasting_monks_index": f"{FastingLevels.STRICT_FAST.value}",
            }
        if is_date_in_tuple(month_day, FISH_ALLOWED):
            return {
                "fasting_season_index": f"{FastingSeasons.NATIVITY_FAST.value}",
                "fasting_laymen_index": f"{FastingLevels.FISH_ALLOWED.value}",
                "fasting_monks_index": f"{FastingLevels.FISH_ALLOWED.value}",
            }
        if weekday_int == Weekdays.SAT.value or weekday_int == Weekdays.SUN.value:
            if is_date_in_range(
                current_date,
                comparison_date(DateFixed.THE_ENTRANCE_OF_THE_THEOTOKOS.value),
                comparison_date(DateFixed.SAINT_SPYRIDON.value),
            ):
                return {
                    "fasting_season_index": f"{FastingSeasons.NATIVITY_FAST.value}",
                    "fasting_laymen_index": f"{FastingLevels.FISH_ALLOWED.value}",
                    "fasting_monks_index": f"{FastingLevels.FISH_ALLOWED.value}",
                }
            return {
                "fasting_season_index": f"{FastingSeasons.NATIVITY_FAST.value}",
                "fasting_laymen_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                "fasting_monks_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
            }
        if (
            weekday_int == Weekdays.MON.value
            or weekday_int == Weekdays.WED.value
            or weekday_int == Weekdays.FRI.value
        ):
            if is_date_in_tuple(month_day, WINE_AND_OLIVE_OIL_ALLOWED):
                return {
                    "fasting_season_index": f"{FastingSeasons.NATIVITY_FAST.value}",
                    "fasting_laymen_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                    "fasting_monks_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                }
            return {
                "fasting_season_index": f"{FastingSeasons.NATIVITY_FAST.value}",
                "fasting_laymen_index": f"{FastingLevels.STRICT_FAST.value}",
                "fasting_monks_index": f"{FastingLevels.STRICT_FAST.value}",
            }
        return {
            "fasting_season_index": f"{FastingSeasons.NATIVITY_FAST.value}",
            "fasting_laymen_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
            "fasting_monks_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
        }

    if is_date_in_range(
        current_date,
        comparison_date(DateFixed.TWELVE_DAY_FAST_FREE_BEFORE.value),
        comparison_date(DateFixed.TWELVE_DAY_FAST_FREE_AFTER.value),
    ):
        if is_date_in_tuple(month_day, STRICT_FAST):
            if weekday_int == Weekdays.SAT.value or weekday_int == Weekdays.SUN.value:
                return {
                    "fasting_season_index": f"{FastingSeasons.TWELVE_DAY_FAST_FREE.value}",
                    "fasting_laymen_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                    "fasting_monks_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                }
            return {
                "fasting_season_index": f"{FastingSeasons.TWELVE_DAY_FAST_FREE.value}",
                "fasting_laymen_index": f"{FastingLevels.STRICT_FAST.value}",
                "fasting_monks_index": f"{FastingLevels.STRICT_FAST.value}",
            }
        return {
            "fasting_season_index": f"{FastingSeasons.TWELVE_DAY_FAST_FREE.value}",
            "fasting_laymen_index": f"{FastingLevels.NO_FASTING.value}",
            "fasting_monks_index": f"{FastingLevels.DAIRY_PRODUCTS_ALLOWED.value}",
        }

    if is_date_in_tuple(month_day, STRICT_FAST):
        if weekday_int == Weekdays.SAT.value or weekday_int == Weekdays.SUN.value:
            return {
                "fasting_season_index": f"{FastingSeasons.REGULAR_SEASON.value}",
                "fasting_laymen_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                "fasting_monks_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
            }
        return {
            "fasting_season_index": f"{FastingSeasons.REGULAR_SEASON.value}",
            "fasting_laymen_index": f"{FastingLevels.STRICT_FAST.value}",
            "fasting_monks_index": f"{FastingLevels.STRICT_FAST.value}",
        }
    if (
        weekday_int == Weekdays.MON.value
        or weekday_int == Weekdays.WED.value
        or weekday_int == Weekdays.FRI.value
    ):
        if (
            is_date_in_tuple(month_day, FISH_ALLOWED)
            or pascha_distance_int == DateMovable.MIDFEAST_OF_PENTECOST.value
            or pascha_distance_int == DateMovable.LEAVETAKING_OF_PASCHA.value
        ) and weekday_int != Weekdays.MON.value:
            return {
                "fasting_season_index": f"{FastingSeasons.REGULAR_SEASON.value}",
                "fasting_laymen_index": f"{FastingLevels.FISH_ALLOWED.value}",
                "fasting_monks_index": f"{FastingLevels.FISH_ALLOWED.value}",
            }
        if (
            is_date_in_tuple(month_day, WINE_AND_OLIVE_OIL_ALLOWED)
            and weekday_int != Weekdays.MON.value
        ):
            return {
                "fasting_season_index": f"{FastingSeasons.REGULAR_SEASON.value}",
                "fasting_laymen_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
                "fasting_monks_index": f"{FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value}",
            }
        if weekday_int == Weekdays.MON.value:
            return {
                "fasting_season_index": f"{FastingSeasons.REGULAR_SEASON.value}",
                "fasting_laymen_index": f"{FastingLevels.NO_FASTING.value}",
                "fasting_monks_index": f"{FastingLevels.STRICT_FAST.value}",
            }
        return {
            "fasting_season_index": f"{FastingSeasons.REGULAR_SEASON.value}",
            "fasting_laymen_index": f"{FastingLevels.STRICT_FAST.value}",
            "fasting_monks_index": f"{FastingLevels.STRICT_FAST.value}",
        }
    return {
        "fasting_season_index": f"{FastingSeasons.REGULAR_SEASON.value}",
        "fasting_laymen_index": f"{FastingLevels.NO_FASTING.value}",
        "fasting_monks_index": f"{FastingLevels.DAIRY_PRODUCTS_ALLOWED.value}",
    }
