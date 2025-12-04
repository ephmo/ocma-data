"""Constants used in the CLI."""

from dataclasses import dataclass
from enum import StrEnum


@dataclass(frozen=True)
class CLIConstants:
    """Immutable constants for CLI."""

    BUILD_FOLDER: str = "public/data"
    PASCHALION: str = "paschalion"
    YEAR_END: int = 2100
    YEAR_START: int = 1924


class JsonKeys(StrEnum):
    """Immutable JsonKeys constants."""

    DATE_OLD = "date_old"
    DATE_NEW = "date_new"
    WEEKDAY_INDEX = "weekday_index"
    MOON_PHASE_INDEX = "moon_phase_index"
    PASCHA_DATE = "pascha_date"
    PASCHA_DISTANCE = "pascha_distance"
    FASTING_SEASON_INDEX = "fasting_season_index"
    FASTING_LAYMEN_INDEX = "fasting_laymen_index"
    FASTING_MONKS_INDEX = "fasting_monks_index"
    SUNDAY_DESCRIPTION_GR_INDEX = "sunday_description_gr_index"
    SUNDAY_DESCRIPTION_RO_INDEX = "sunday_description_ro_index"
    SUNDAY_DESCRIPTION_RU_INDEX = "sunday_description_ru_index"
    SUNDAY_LECTIONARY_INDEX = "sunday_lectionary_index"
