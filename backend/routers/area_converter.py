from fastapi import APIRouter
from schemas.area_converter import AreaConverterRequest
from services.area_converter_service import AreaConverterService


router = APIRouter(
    prefix="/area",
    tags=["Area Converter"]
)


@router.get("/")
def area_converter():
    return {
        "message": "Area Converter API"
    }


@router.post("/convert")
def convert_area(request:AreaConverterRequest):
    return AreaConverterService.convert(
        value=request.value,
        from_unit=request.from_unit,
        to_unit=request.to_unit,
        
        
    )
    
