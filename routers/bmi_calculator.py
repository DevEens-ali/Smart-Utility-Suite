from fastapi import APIRouter

router = APIRouter(
    prefix = "/bmi",
    tags = ["BMI calculator"]
)
@router.get("/")
def BMICalculator():
    return {
        "message": "BMI Calculator API"
    }
