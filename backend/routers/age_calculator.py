from fastapi import APIRouter
from schemas.age_calculator import AgeCalculatorRequest
from services.age_service import AgeCalculatorService

router = APIRouter(
    prefix="/age",
    tags=["Age Calculator"]
)

@router.get("/")
def get_age_info():
    return {
        "message": "Welcome! Calculate your age from your date of birth."
    }

@router.post("/calculate")
def calculate_age(request: AgeCalculatorRequest):

    return AgeCalculatorService.calculate(
        request.date_of_birth,
    )
