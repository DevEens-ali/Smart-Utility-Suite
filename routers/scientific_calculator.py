from fastapi import APIRouter

router = APIRouter(
    prefix = "/scientific",
    tags = ["Scientific calculator"]
)
@router.get("/")
def ScientificCalculator():
    return {
        "message": "Scientific Calculator API"
    }
