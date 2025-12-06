"""Module for calculating fasting seasons and levels."""

from datetime import date
from typing import TypedDict

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


class FastingResult(TypedDict):
    """Type for fasting result."""

    fasting_season_index: str
    fasting_laymen_index: str
    fasting_monks_index: str


class FastingContext:
    """Context object for fasting calculations."""

    def __init__(self, current_date: date, calendar_style: str):
        """Initialize fasting context with date and calendar style."""
        self.current_date = current_date
        self.calendar_style = calendar_style
        self.month_day = f"{current_date.month}-{current_date.day}"
        self.pascha_distance = int(pascha_distance(current_date, calendar_style))
        self.weekday = int(get_weekday(current_date, calendar_style))

    def comparison_date(self, fasting_season_date: str) -> date:
        """Get the comparison date for fixed date ranges."""
        current_year = self.current_date.year
        if fasting_season_date == DateFixed.TWELVE_DAY_FAST_FREE_AFTER.value:
            current_year += 1

        parts = fasting_season_date.split("-")
        return date(current_year, int(parts[0]), int(parts[1]))

    def is_weekend(self) -> bool:
        """Check if current day is weekend."""
        return self.weekday in (Weekdays.SAT.value, Weekdays.SUN.value)

    def is_mon_wed_fri(self) -> bool:
        """Check if current day is Monday, Wednesday or Friday."""
        return self.weekday in (Weekdays.MON.value, Weekdays.WED.value, Weekdays.FRI.value)

    def create_result(self, season: int, laymen: int, monks: int) -> FastingResult:
        """Create a fasting result dictionary."""
        return {
            "fasting_season_index": str(season),
            "fasting_laymen_index": str(laymen),
            "fasting_monks_index": str(monks),
        }


# Strategy functions for each fasting period

def check_first_week_triodion(ctx: FastingContext) -> FastingResult | None:
    """Check if date is in First Week of Triodion."""
    if (PaschaDistanceBefore.FIRST_WEEK_OF_THE_TRIODION.value <= ctx.pascha_distance
            <= PaschaDistanceAfter.FIRST_WEEK_OF_THE_TRIODION.value):
        return ctx.create_result(
            FastingSeasons.FIRST_WEEK_OF_THE_TRIODION.value,
            FastingLevels.NO_FASTING.value,
            FastingLevels.DAIRY_PRODUCTS_ALLOWED.value
        )
    return None


def check_cheesefare_week(ctx: FastingContext) -> FastingResult | None:
    """Check if date is in Cheesefare Week."""
    if (PaschaDistanceBefore.CHEESEFARE_WEEK.value <= ctx.pascha_distance
            <= PaschaDistanceAfter.CHEESEFARE_WEEK.value):
        return ctx.create_result(
            FastingSeasons.CHEESEFARE_WEEK.value,
            FastingLevels.DAIRY_PRODUCTS_ALLOWED.value,
            FastingLevels.DAIRY_PRODUCTS_ALLOWED.value
        )
    return None


def check_three_day_fast(ctx: FastingContext) -> FastingResult | None:
    """Check if date is in Three-Day Fast."""
    if (PaschaDistanceBefore.THREE_DAY_FAST.value <= ctx.pascha_distance
            <= PaschaDistanceAfter.THREE_DAY_FAST.value):
        level = (FastingLevels.STRICT_FAST.value
                if is_date_in_tuple(ctx.month_day, FISH_ALLOWED)
                else FastingLevels.ABSOLUTE_FAST.value)
        return ctx.create_result(FastingSeasons.THREE_DAY_FAST.value, level, level)
    return None


def check_great_lent(ctx: FastingContext) -> FastingResult | None:
    """Check if date is in Great Lent."""
    if not (PaschaDistanceBefore.GREAT_LENT.value <= ctx.pascha_distance
            <= PaschaDistanceAfter.GREAT_LENT.value):
        return None

    # Fish allowed days
    if (is_date_in_tuple(ctx.month_day, FISH_ALLOWED)
            or ctx.pascha_distance == DateMovable.PALM_SUNDAY.value):
        level = FastingLevels.FISH_ALLOWED.value
    # Wine and oil allowed days
    elif (is_date_in_tuple(ctx.month_day, WINE_AND_OLIVE_OIL_ALLOWED)
            or ctx.is_weekend()):
        level = FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value
    # Strict fast days
    else:
        level = FastingLevels.STRICT_FAST.value

    return ctx.create_result(FastingSeasons.GREAT_LENT.value, level, level)


def check_holy_week(ctx: FastingContext) -> FastingResult | None:
    """Check if date is in Holy Week."""
    if not (PaschaDistanceBefore.HOLY_WEEK.value <= ctx.pascha_distance
            <= PaschaDistanceAfter.HOLY_WEEK.value):
        return None

    is_saturday = ctx.weekday == Weekdays.SAT.value
    is_friday = ctx.weekday == Weekdays.FRI.value
    fish_allowed = is_date_in_tuple(ctx.month_day, FISH_ALLOWED)

    # Saturday - strict fast
    if is_saturday:
        level = FastingLevels.STRICT_FAST.value
    # Friday - absolute or strict fast
    elif is_friday:
        level = (FastingLevels.STRICT_FAST.value if fish_allowed
                else FastingLevels.ABSOLUTE_FAST.value)
    # Other days with fish allowed
    elif fish_allowed:
        level = FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value
    # Other days
    else:
        level = FastingLevels.STRICT_FAST.value

    return ctx.create_result(FastingSeasons.HOLY_WEEK.value, level, level)


def check_bright_week(ctx: FastingContext) -> FastingResult | None:
    """Check if date is in Bright Week."""
    if (PaschaDistanceBefore.BRIGHT_WEEK.value <= ctx.pascha_distance
            <= PaschaDistanceAfter.BRIGHT_WEEK.value):
        return ctx.create_result(
            FastingSeasons.BRIGHT_WEEK.value,
            FastingLevels.NO_FASTING.value,
            FastingLevels.DAIRY_PRODUCTS_ALLOWED.value
        )
    return None


def check_week_holy_spirit(ctx: FastingContext) -> FastingResult | None:
    """Check if date is in Week of the Holy Spirit."""
    if (PaschaDistanceBefore.WEEK_OF_THE_HOLY_SPIRIT.value <= ctx.pascha_distance
            <= PaschaDistanceAfter.WEEK_OF_THE_HOLY_SPIRIT.value):
        return ctx.create_result(
            FastingSeasons.WEEK_OF_THE_HOLY_SPIRIT.value,
            FastingLevels.NO_FASTING.value,
            FastingLevels.DAIRY_PRODUCTS_ALLOWED.value
        )
    return None


def check_apostles_fast(ctx: FastingContext) -> FastingResult | None:
    """Check if date is in Apostles' Fast."""
    if not (ctx.pascha_distance >= PaschaDistanceBefore.APOSTLES_FAST.value
            and is_date_before(ctx.current_date, ctx.comparison_date(DateFixed.APOSTLES_FAST.value))):
        return None

    # Fish allowed days
    if is_date_in_tuple(ctx.month_day, FISH_ALLOWED):
        level = FastingLevels.FISH_ALLOWED.value
    # Weekend
    elif ctx.is_weekend():
        before_baptist = is_date_before(
            ctx.current_date,
            ctx.comparison_date(DateFixed.NATIVITY_OF_THE_BAPTIST.value)
        )
        level = (FastingLevels.FISH_ALLOWED.value if before_baptist
                else FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value)
    # Monday, Wednesday, Friday
    elif ctx.is_mon_wed_fri():
        level = (FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value
                if is_date_in_tuple(ctx.month_day, WINE_AND_OLIVE_OIL_ALLOWED)
                else FastingLevels.STRICT_FAST.value)
    # Other days
    else:
        level = FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value

    return ctx.create_result(FastingSeasons.APOSTLES_FAST.value, level, level)


def check_dormition_fast(ctx: FastingContext) -> FastingResult | None:
    """Check if date is in Dormition Fast."""
    if not is_date_in_range(
        ctx.current_date,
        ctx.comparison_date(DateFixed.DORMITION_FAST_BEFORE.value),
        ctx.comparison_date(DateFixed.DORMITION_FAST_AFTER.value)
    ):
        return None

    # Fish allowed days
    if is_date_in_tuple(ctx.month_day, FISH_ALLOWED):
        level = FastingLevels.FISH_ALLOWED.value
    # Weekend
    elif ctx.is_weekend():
        level = FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value
    # Other days
    else:
        level = FastingLevels.STRICT_FAST.value

    return ctx.create_result(FastingSeasons.DORMITION_FAST.value, level, level)


def check_nativity_fast(ctx: FastingContext) -> FastingResult | None:
    """Check if date is in Nativity Fast."""
    if not is_date_in_range(
        ctx.current_date,
        ctx.comparison_date(DateFixed.NATIVITY_FAST_BEFORE.value),
        ctx.comparison_date(DateFixed.NATIVITY_FAST_AFTER.value)
    ):
        return None

    is_strict_day = is_date_in_tuple(ctx.month_day, STRICT_FAST)

    # Strict fast days
    if is_strict_day:
        level = (FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value if ctx.is_weekend()
                else FastingLevels.STRICT_FAST.value)
    # Fish allowed days
    elif is_date_in_tuple(ctx.month_day, FISH_ALLOWED):
        level = FastingLevels.FISH_ALLOWED.value
    # Weekend
    elif ctx.is_weekend():
        in_theotokos_range = is_date_in_range(
            ctx.current_date,
            ctx.comparison_date(DateFixed.THE_ENTRANCE_OF_THE_THEOTOKOS.value),
            ctx.comparison_date(DateFixed.SAINT_SPYRIDON.value)
        )
        level = (FastingLevels.FISH_ALLOWED.value if in_theotokos_range
                else FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value)
    # Monday, Wednesday, Friday
    elif ctx.is_mon_wed_fri():
        level = (FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value
                if is_date_in_tuple(ctx.month_day, WINE_AND_OLIVE_OIL_ALLOWED)
                else FastingLevels.STRICT_FAST.value)
    # Other days
    else:
        level = FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value

    return ctx.create_result(FastingSeasons.NATIVITY_FAST.value, level, level)


def check_twelve_day_fast_free(ctx: FastingContext) -> FastingResult | None:
    """Check if date is in Twelve-Day Fast-Free period."""
    if not is_date_in_range(
        ctx.current_date,
        ctx.comparison_date(DateFixed.TWELVE_DAY_FAST_FREE_BEFORE.value),
        ctx.comparison_date(DateFixed.TWELVE_DAY_FAST_FREE_AFTER.value)
    ):
        return None

    if is_date_in_tuple(ctx.month_day, STRICT_FAST):
        level = (FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value if ctx.is_weekend()
                else FastingLevels.STRICT_FAST.value)
        return ctx.create_result(FastingSeasons.TWELVE_DAY_FAST_FREE.value, level, level)

    return ctx.create_result(
        FastingSeasons.TWELVE_DAY_FAST_FREE.value,
        FastingLevels.NO_FASTING.value,
        FastingLevels.DAIRY_PRODUCTS_ALLOWED.value
    )


def check_regular_season(ctx: FastingContext) -> FastingResult:
    """Check regular season fasting rules."""
    # Strict fast days
    if is_date_in_tuple(ctx.month_day, STRICT_FAST):
        level = (FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value if ctx.is_weekend()
                else FastingLevels.STRICT_FAST.value)
        return ctx.create_result(FastingSeasons.REGULAR_SEASON.value, level, level)

    # Monday, Wednesday, Friday
    if ctx.is_mon_wed_fri():
        # Special movable feasts (not on Monday)
        if (ctx.weekday != Weekdays.MON.value and
                (is_date_in_tuple(ctx.month_day, FISH_ALLOWED)
                 or ctx.pascha_distance == DateMovable.MIDFEAST_OF_PENTECOST.value
                 or ctx.pascha_distance == DateMovable.LEAVETAKING_OF_PASCHA.value)):
            level_lay = level_monk = FastingLevels.FISH_ALLOWED.value
        # Wine and oil allowed (not on Monday)
        elif (ctx.weekday != Weekdays.MON.value
                and is_date_in_tuple(ctx.month_day, WINE_AND_OLIVE_OIL_ALLOWED)):
            level_lay = level_monk = FastingLevels.WINE_AND_OLIVE_OIL_ALLOWED.value
        # Monday
        elif ctx.weekday == Weekdays.MON.value:
            level_lay = FastingLevels.NO_FASTING.value
            level_monk = FastingLevels.STRICT_FAST.value
        # Wednesday and Friday
        else:
            level_lay = level_monk = FastingLevels.STRICT_FAST.value

        return ctx.create_result(FastingSeasons.REGULAR_SEASON.value, level_lay, level_monk)

    # Other days - no fasting for laypeople
    return ctx.create_result(
        FastingSeasons.REGULAR_SEASON.value,
        FastingLevels.NO_FASTING.value,
        FastingLevels.DAIRY_PRODUCTS_ALLOWED.value
    )


# Main function with strategy pattern

FASTING_STRATEGIES = [
    check_first_week_triodion,
    check_cheesefare_week,
    check_three_day_fast,
    check_great_lent,
    check_holy_week,
    check_bright_week,
    check_week_holy_spirit,
    check_apostles_fast,
    check_dormition_fast,
    check_nativity_fast,
    check_twelve_day_fast_free,
]


def get_fasting(current_date: date, calendar_style: str) -> dict[str, str]:
    """Get the fasting_season_index, fasting_laymen_index and fasting_monks_index.

    This function uses a strategy pattern to check each fasting period in order.
    The first matching period determines the fasting rules.
    """
    ctx = FastingContext(current_date, calendar_style)

    # Check special fasting periods in order
    for strategy in FASTING_STRATEGIES:
        result = strategy(ctx)
        if result is not None:
            return result

    # Default to regular season
    return check_regular_season(ctx)
