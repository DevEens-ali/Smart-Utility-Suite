from fastapi import APIRouter

router = APIRouter(
    prefix = "/gpa",
    tags = ["GPA calculator"]
)
@router.get("/")
def GPACalculator():
    return {
        "message": "GPA Calculator API"
    }
