from fastapi import APIRouter
from schemas.length_converter import LengthConverterRequest
from services.length_converter_service import LengthConverterService


router = APIRouter(
    prefix="/length",
    tags=["Length Converter"]
)


@router.get("/")
def length_converter():
    return {
        "message": "Length Converter API"
    }


@router.post("/convert")
def convert_length(request: LengthConverterRequest):

    return LengthConverterService.convert(
        value=request.value,
        from_unit=request.from_unit,
        to_unit=request.to_unit,
    )