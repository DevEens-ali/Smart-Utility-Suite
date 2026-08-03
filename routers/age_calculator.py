from fastapi import APIRouter

router = APIRouter(
    prefix = "/age",
    tags = ["Age calculator"]
)
@router.get("/")
def AgeCalculator():
    return {
        "message": "Age Calculator API"
    }
