"""Module providing a function generating JSON data for Calendar."""

import json
from datetime import date
from pathlib import Path

from ocma_data.cli.constants import CLIConstants, JsonKeys
from ocma_data.constants import CalendarStyles
from ocma_data.core.date.logic import get_date
from ocma_data.core.moon_phase.logic import get_moon_phase
from ocma_data.core.pascha.logic import calculate_pascha
from ocma_data.core.pascha_distance.logic import pascha_distance
from ocma_data.core.weekday.logic import get_weekday
from ocma_data.utils.date_utils import is_valid_date, string_to_date


def main() -> None:
    """Generate JSON data for the Calendar."""
    Path(CLIConstants().BUILD_FOLDER).mkdir(parents=True, exist_ok=True)
    Path(f"{CLIConstants().BUILD_FOLDER}/{CLIConstants().PASCHALION}").mkdir(
        parents=True, exist_ok=True
    )

    for calendar_style in CalendarStyles:
        Path(f"{CLIConstants().BUILD_FOLDER}/{calendar_style.value}").mkdir(
            parents=True, exist_ok=True
        )
        paschalion_data = {}
        paschalion_data[JsonKeys.PASCHA_DATE.value] = {}

        for current_year in range(CLIConstants().YEAR_START, CLIConstants().YEAR_END):
            paschalion_data[JsonKeys.PASCHA_DATE.value][current_year] = (
                calculate_pascha(current_year, calendar_style.value)
            )

            with Path(
                f"{CLIConstants().BUILD_FOLDER}/{CLIConstants().PASCHALION}/{calendar_style.value}.json",
            ).open("w", encoding="utf-8") as json_file:
                json.dump(paschalion_data, json_file, indent=4)

            calendar_data = {}
            calendar_data[str(current_year)] = {}

            for current_month in range(1, 13):
                calendar_data[str(current_year)][str(current_month)] = {}

                for current_day in range(1, 32):
                    if is_valid_date(current_year, current_month, current_day):
                        current_date = date(current_year, current_month, current_day)
                        date_old_new = get_date(current_date, calendar_style.value)

                        calendar_data[str(current_year)][str(current_month)][
                            str(current_day)
                        ] = {}
                        calendar_data[str(current_year)][str(current_month)][
                            str(current_day)
                        ][JsonKeys.DATE_OLD.value] = date_old_new[
                            JsonKeys.DATE_OLD.value
                        ]
                        calendar_data[str(current_year)][str(current_month)][
                            str(current_day)
                        ][JsonKeys.DATE_NEW.value] = date_old_new[
                            JsonKeys.DATE_NEW.value
                        ]
                        calendar_data[str(current_year)][str(current_month)][
                            str(current_day)
                        ][JsonKeys.WEEKDAY_INDEX.value] = get_weekday(
                            current_date, calendar_style.value
                        )
                        calendar_data[str(current_year)][str(current_month)][
                            str(current_day)
                        ][JsonKeys.MOON_PHASE_INDEX.value] = get_moon_phase(
                            string_to_date(
                                f"{current_year}-{current_month}-{current_day}"
                            ),
                            calendar_style.value,
                        )
                        calendar_data[str(current_year)][str(current_month)][
                            str(current_day)
                        ][JsonKeys.PASCHA_DISTANCE.value] = pascha_distance(
                            current_date, calendar_style.value
                        )
                        calendar_data[str(current_year)][str(current_month)][
                            str(current_day)
                        ][JsonKeys.FASTING_SEASON_INDEX.value] = ""
                        calendar_data[str(current_year)][str(current_month)][
                            str(current_day)
                        ][JsonKeys.FASTING_LAYMEN_INDEX.value] = ""
                        calendar_data[str(current_year)][str(current_month)][
                            str(current_day)
                        ][JsonKeys.FASTING_MONKS_INDEX.value] = ""
                        calendar_data[str(current_year)][str(current_month)][
                            str(current_day)
                        ][JsonKeys.SUNDAY_DESCRIPTION_GR_INDEX.value] = ""
                        calendar_data[str(current_year)][str(current_month)][
                            str(current_day)
                        ][JsonKeys.SUNDAY_DESCRIPTION_RO_INDEX.value] = ""
                        calendar_data[str(current_year)][str(current_month)][
                            str(current_day)
                        ][JsonKeys.SUNDAY_DESCRIPTION_RU_INDEX.value] = ""
                        calendar_data[str(current_year)][str(current_month)][
                            str(current_day)
                        ][JsonKeys.SUNDAY_LECTIONARY_INDEX.value] = ""

            with Path(
                f"{CLIConstants().BUILD_FOLDER}/{calendar_style.value}/{current_year}.json",
            ).open("w", encoding="utf-8") as json_file:
                json.dump(calendar_data, json_file, indent=4)


if __name__ == "__main__":
    main()
