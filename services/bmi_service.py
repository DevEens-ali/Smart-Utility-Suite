class BMICalculatorService:
    """
    Business logic for BMI Calculator.
    """

    @staticmethod
    def calculate(height: float, weight: float):

        # Calculate BMI
        bmi = round(weight / (height * height), 2)

        # Decide Category & Message
        if bmi < 18.5:
            category = "Underweight"
            message = "You are below the healthy BMI range."
            advice = (
                        "Your BMI indicates that you are underweight. "
                        "Try to increase your calorie intake with nutritious foods such as milk, eggs, nuts, rice, potatoes, chicken, and healthy fats. "
                        "Include strength training exercises and consult a healthcare professional if you continue losing weight."
                    )

        elif 18.5 <= bmi < 25:
            category = "Normal Weight"
            message = "You are in the healthy BMI range."
            advice = (
                        "Great job! Your BMI is within the healthy range. "
                        "Maintain a balanced diet, stay physically active for at least 30 minutes a day, drink enough water, and continue your healthy lifestyle."
                    )

        elif 25 <= bmi < 30:
            category = "Overweight"
            message = "You are above the healthy BMI range."
            advice = (
                        "Your BMI indicates that you are slightly above the healthy range. "
                        "Reduce sugary drinks and junk food, increase fruits and vegetables, exercise regularly, and aim for gradual weight loss through healthy habits."
                    )

        elif 30 <= bmi < 35:
            category = "Obesity Class I"
            message = "Your BMI indicates Class I obesity."
            advice = (
                        "Your BMI falls into Obesity Class I. "
                        "It is recommended to start a structured weight management plan, reduce processed foods, exercise consistently, and seek guidance from a healthcare professional if needed."
                    )

        elif 35 <= bmi < 40:
            category = "Obesity Class II"
            message = "Your BMI indicates Class II obesity."
            advice = (
                        "Your BMI indicates Obesity Class II. "
                        "This level increases the risk of several health conditions. Consult a healthcare provider for a personalized diet and exercise plan."
                    )

        else:
            category = "Obesity Class III"
            message = "Your BMI indicates severe obesity."
            advice = (
                        "Your BMI falls into Obesity Class III. "
                        "This is considered severe obesity and requires professional medical advice. Please consult your doctor or a nutrition specialist for a comprehensive treatment plan."
                    )

        # Return Response
        
        return {
            "bmi": bmi,
            "category": category,
            "message": message,
            "advice": advice,
        }
