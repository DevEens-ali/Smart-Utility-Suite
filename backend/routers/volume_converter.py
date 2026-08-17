from fastapi import APIRouter
from schemas.volume_converter import VolumeConverterRequest
from services.volume_converter_service import VolumeConverterService


router = APIRouter(
    prefix="/volume",
    tags=["Volume Converter"]
)


@router.get("/")
def volume_converter():
    return {
        "message": "Volume Converter API"
    }


@router.post("/convert")
def convert_volume(request: VolumeConverterRequest):
    return VolumeConverterService.convert(
        value=request.value,
        from_unit=request.from_unit,
        to_unit=request.to_unit,
        
    )