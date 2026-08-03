from fastapi import APIRouter

router = APIRouter(
    prefix = "/cgpa",
    tags = ["CGPA calculator"]
)
@router.get("/")
def CGPACalculator():
    return {
        "message": "CGPA Calculator API"
    }
