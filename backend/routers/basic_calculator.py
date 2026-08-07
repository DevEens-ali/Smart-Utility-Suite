# """
# Basic Calculator Router

# Purpose:
# ------------
# Is file ka sirf ek kaam hai:

# Basic Calculator ke tamam API Endpoints
# isi file me honge.

# Yahan calculation nahi hogi.

# Yahan sirf:

# Receive Request
# ↓

# Service Call

# ↓

# Return Response
# """

from fastapi import APIRouter
from schemas.basic_calculator import BasicCalculatorRequest
from services.basic_calculator_service import BasicCalculatorService

router = APIRouter(
    prefix="/calculator",
    tags=["Basic Calculator"]
)

@router.get("/")
def basic_calculator():
    return {
        "message": "Basic Calculator API"
    }

@router.post("/calculate")
def calculate(request: BasicCalculatorRequest):

    return BasicCalculatorService.calculate(
        request.num1,
        request.num2,
        request.operation,
    )
