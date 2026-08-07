class BasicCalculatorService:
    """
    Business logic for Basic Calculator.
    """

    @staticmethod
    def calculate(num1: float, num2: float, operation: str):

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":

            if num2 == 0:
                return {
                    "error": "Cannot divide by zero. Please provide a number"
                }

            result = num1 / num2

        return {
            "result": result
        }
