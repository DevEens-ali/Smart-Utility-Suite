class WeightConverterService:
    """
    Business logic for Weight Converter.
    """

    @staticmethod
    def convert(value: float, from_unit: str, to_unit: str):

        # ==========================================
        # Conversion factors
        # Base unit = kilogram
        # ==========================================

        conversion_factors = {
            "kilogram": 1,
            "gram": 0.001,
            "milligram": 0.000001,
            "metric_ton": 1000,
            "pound": 0.45359237,
            "ounce": 0.028349523125,
        }

        # ==========================================
        # Convert unit names to lowercase
        # ==========================================

        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # ==========================================
        # Check source unit
        # ==========================================

        if from_unit not in conversion_factors:
            return {
                "error": f"Invalid source unit: {from_unit}"
            }

        # ==========================================
        # Check target unit
        # ==========================================

        if to_unit not in conversion_factors:
            return {
                "error": f"Invalid target unit: {to_unit}"
            }

        # ==========================================
        # Convert source value to kilograms
        # ==========================================

        value_in_kilograms = (
            value * conversion_factors[from_unit]
        )

        # ==========================================
        # Convert kilograms to target unit
        # ==========================================

        result = (
            value_in_kilograms / conversion_factors[to_unit]
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