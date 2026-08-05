from fastapi import APIRouter
from schemas.bmi_calculator import BMICalculatorRequest
from services.bmi_service import BMICalculatorService

router = APIRouter(
    prefix="/bmi",
    tags=["BMI Calculator"]
)


@router.get("/")
def get_bmi_info():
    return {
        "message": "Welcome! Check your BMI to track your health."
    }


@router.post("/calculate")
def calculatebmi(request: BMICalculatorRequest):
    return BMICalculatorService.calculate(
        request.height,
        request.weight,
    )
