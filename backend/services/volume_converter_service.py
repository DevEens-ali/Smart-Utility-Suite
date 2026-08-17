class VolumeConverterService:
    """
    Business logic for Volume Converter.
    """

    @staticmethod
    def convert(value: float, from_unit: str, to_unit: str):

        # ==========================================
        # Conversion factors
        # Base unit = liter
        # ==========================================

        conversion_factors = {
            "liter": 1,
            "milliliter": 0.001,
            "cubic_meter": 1000,
            "cubic_centimeter": 0.001,
            "gallon": 3.785411784,
            "quart": 0.946352946,
            "pint": 0.473176473,
            "cup": 0.2365882365,
        }

        # ==========================================
        # Convert unit names to lowercase
        # ==========================================

        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # ==========================================
        # Validate source unit
        # ==========================================

        if from_unit not in conversion_factors:
            return {
                "error": f"Invalid source unit: {from_unit}"
            }

        # ==========================================
        # Validate target unit
        # ==========================================

        if to_unit not in conversion_factors:
            return {
                "error": f"Invalid target unit: {to_unit}"
            }

        # ==========================================
        # Convert source value to liters
        # ==========================================

        value_in_liters = (
            value * conversion_factors[from_unit]
        )

        # ==========================================
        # Convert liters to target unit
        # ==========================================

        result = (
            value_in_liters / conversion_factors[to_unit]
        )

        # ==========================================
        # Return response
        # ==========================================

        return {
            "value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "result": round(result, 6),
        }