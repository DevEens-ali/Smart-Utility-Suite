class TemperatureConverterService:
    """
    Business logic for Temperature Converter.
    """

    @staticmethod
    def convert(value: float, from_unit: str, to_unit: str):

        # ==========================================
        # Convert units to lowercase
        # ==========================================

        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # ==========================================
        # Validate units
        # ==========================================

        valid_units = {
            "celsius",
            "fahrenheit",
            "kelvin"
        }

        if from_unit not in valid_units:
            return {
                "error": f"Invalid source unit: {from_unit}"
            }

        if to_unit not in valid_units:
            return {
                "error": f"Invalid target unit: {to_unit}"
            }

        # ==========================================
        # Celsius → Fahrenheit
        # ==========================================

        if from_unit == "celsius" and to_unit == "fahrenheit":

            result = (value * 9 / 5) + 32

        # ==========================================
        # Fahrenheit → Celsius
        # ==========================================

        elif from_unit == "fahrenheit" and to_unit == "celsius":

            result = (value - 32) * 5 / 9

        # ==========================================
        # Celsius → Kelvin
        # ==========================================

        elif from_unit == "celsius" and to_unit == "kelvin":

            result = value + 273.15

        # ==========================================
        # Kelvin → Celsius
        # ==========================================

        elif from_unit == "kelvin" and to_unit == "celsius":

            result = value - 273.15

        # ==========================================
        # Fahrenheit → Kelvin
        # ==========================================

        elif from_unit == "fahrenheit" and to_unit == "kelvin":

            result = (value - 32) * 5 / 9 + 273.15

        # ==========================================
        # Kelvin → Fahrenheit
        # ==========================================

        elif from_unit == "kelvin" and to_unit == "fahrenheit":

            result = (value - 273.15) * 9 / 5 + 32

        # ==========================================
        # Same unit
        # ==========================================

        else:

            result = value

        # ==========================================
        # Return response
        # ==========================================

        return {
            "value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "result": round(result, 2)
        }