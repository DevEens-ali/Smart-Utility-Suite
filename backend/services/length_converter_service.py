class LengthConverterService:
    """
    Business logic for Length Converter.
    """

    @staticmethod
    def convert(value: float, from_unit: str, to_unit: str):

        # ==========================================
        # Conversion factors
        # Base unit = meter
        # ==========================================

        conversion_factors = {
            "meter": 1,
            "kilometer": 1000,
            "centimeter": 0.01,
            "millimeter": 0.001,
            "mile": 1609.344,
            "yard": 0.9144,
            "foot": 0.3048,
            "inch": 0.0254,
        }

        # ==========================================
        # Convert unit names to lowercase
        # ==========================================

        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # ==========================================
        # Check units
        # ==========================================

        if from_unit not in conversion_factors:
            return {
                "error": f"Invalid source unit: {from_unit}"
            }

        if to_unit not in conversion_factors:
            return {
                "error": f"Invalid target unit: {to_unit}"
            }

        # ==========================================
        # Convert source value to meters
        # ==========================================

        value_in_meters = value * conversion_factors[from_unit]

        # ==========================================
        # Convert meters to target unit
        # ==========================================

        result = value_in_meters / conversion_factors[to_unit]

        # ==========================================
        # Return response
        # ==========================================

        return {
            "value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "result": round(result, 6),
        }