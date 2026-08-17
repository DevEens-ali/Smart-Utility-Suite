from fastapi import APIRouter
from schemas.weight_converter import WeightConverterRequest
from services.weight_converter_service import WeightConverterService

router = APIRouter(
    prefix="/weight",
    tags=["Weight Converter"]
)


@router.get("/")
def weight_converter():
    return {
        "message": "Weight Converter API"
    }



@router.post("/convert")
def convert_weight(request: WeightConverterRequest):
    return WeightConverterService.convert(
        value=request.value,
        from_unit=request.from_unit,
        to_unit=request.to_unit,
    )