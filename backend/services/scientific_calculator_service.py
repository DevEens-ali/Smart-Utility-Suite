import math


class ScientificCalculatorService:
    """
    Business logic for Scientific Calculator.
    """

    @staticmethod
    def calculate(input_expression: str):

        try:
            result = eval(
                input_expression,
                {
                    "__builtins__": {},
                    "math": math,
                }
            )

            return {
                "expression": input_expression,
                "result": result,
            }

        except ZeroDivisionError:
            return {
                "error": "Cannot divide by zero."
            }

        except (ValueError, TypeError):
            return {
                "error": "Invalid mathematical expression."
            }

        except Exception:
            return {
                "error": "Unable to calculate the given expression."
            }