class AreaConverterService:
    """
    Business logic for Area Converter.
    """

    @staticmethod
    def convert(value: float, from_unit: str, to_unit: str):

        # ==========================================
        # Conversion factors
        # Base unit = square meter
        # ==========================================

        conversion_factors = {
            "square_meter": 1,
            "square_kilometer": 1_000_000,
            "square_centimeter": 0.0001,
            "square_mile": 2_589_988.110336,
            "square_yard": 0.83612736,
            "square_foot": 0.09290304,
            "square_inch": 0.00064516,
            "acre": 4046.8564224,
            "hectare": 10_000,
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
        # Convert source value to square meters
        # ==========================================

        value_in_square_meters = (
            value * conversion_factors[from_unit]
        )

        # ==========================================
        # Convert square meters to target unit
        # ==========================================

        result = (
            value_in_square_meters
            / conversion_factors[to_unit]
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