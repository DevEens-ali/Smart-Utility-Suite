from datetime import date
import calendar

from dateutil.relativedelta import relativedelta


class AgeCalculatorService:
    """
    Business logic for Age Calculator.
    """

    # ==========================================
    # Check Leap Year
    # ==========================================

    @staticmethod
    def leap_year(birth_year: int):

        if birth_year % 4 == 0:

            if birth_year % 100 == 0:
                return birth_year % 400 == 0

            return True

        return False

    # ==========================================
    # Days Until Next Birthday
    # ==========================================

    @staticmethod
    def days_until_birthday(birth_month: int, birth_day: int):

        today = date.today()

        try:
            next_birthday = date(
                today.year,
                birth_month,
                birth_day,
            )

        except ValueError:
            # Handle 29 Feb
            next_birthday = date(
                today.year,
                3,
                1,
            )

        if next_birthday < today:

            try:
                next_birthday = date(
                    today.year + 1,
                    birth_month,
                    birth_day,
                )

            except ValueError:
                next_birthday = date(
                    today.year + 1,
                    3,
                    1,
                )

        remaining_days = (next_birthday - today).days

        return remaining_days

    # ==========================================
    # Zodiac Sign
    # ==========================================

    @staticmethod
    def get_zodiac_sign(month: int, day: int):

        if month == 3:
            return "Aries" if day >= 21 else "Pisces"

        elif month == 4:
            return "Taurus" if day >= 20 else "Aries"

        elif month == 5:
            return "Gemini" if day >= 21 else "Taurus"

        elif month == 6:
            return "Cancer" if day >= 21 else "Gemini"

        elif month == 7:
            return "Leo" if day >= 23 else "Cancer"

        elif month == 8:
            return "Virgo" if day >= 23 else "Leo"

        elif month == 9:
            return "Libra" if day >= 23 else "Virgo"

        elif month == 10:
            return "Scorpio" if day >= 23 else "Libra"

        elif month == 11:
            return "Sagittarius" if day >= 22 else "Scorpio"

        elif month == 12:
            return "Capricorn" if day >= 22 else "Sagittarius"

        elif month == 1:
            return "Aquarius" if day >= 20 else "Capricorn"

        elif month == 2:
            return "Pisces" if day >= 19 else "Aquarius"

        return "Unknown"

    # ==========================================
    # Generation
    # ==========================================

    @staticmethod
    def get_generation(birth_year: int):

        if 1997 <= birth_year <= 2012:
            return "Gen Z"

        elif 1981 <= birth_year <= 1996:
            return "Millennial"

        elif 1965 <= birth_year <= 1980:
            return "Generation X"

        elif 1946 <= birth_year <= 1964:
            return "Baby Boomer"

        return "Silent Generation"

    # ==========================================
    # Main Calculation
    # ==========================================

    @staticmethod
    def calculate(date_of_birth):

        # Current Date
        today = date.today()

        # Current Age
        age = relativedelta(today, date_of_birth)

        years = age.years
        months = age.months
        days = age.days

        # Total Age
        total_days = (today - date_of_birth).days
        total_weeks = total_days // 7
        total_hours = total_days * 24
        total_minutes = total_hours * 60
        total_months = (years * 12) + months

        # Birth Details
        day_of_birth = calendar.day_name[
            date_of_birth.weekday()
        ]

        born_in_leap_year = AgeCalculatorService.leap_year(
            date_of_birth.year
        )

        zodiac_sign = AgeCalculatorService.get_zodiac_sign(
            date_of_birth.month,
            date_of_birth.day,
        )

        generation = AgeCalculatorService.get_generation(
            date_of_birth.year
        )

        next_birthday = AgeCalculatorService.days_until_birthday(
            date_of_birth.month,
            date_of_birth.day,
        )

        # Response
        return {
            "current_age": {
                "years": years,
                "months": months,
                "days": days,
            },

            "total_age": {
                "months": total_months,
                "weeks": total_weeks,
                "days": total_days,
                "hours": total_hours,
                "minutes": total_minutes,
            },

            "birth_details": {
                "day_of_birth": day_of_birth,
                "born_in_leap_year": born_in_leap_year,
                "zodiac_sign": zodiac_sign,
                "generation": generation,
            },

            "next_birthday": {
                "days_remaining": next_birthday,
            },
        }
