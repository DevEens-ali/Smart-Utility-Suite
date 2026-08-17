from fastapi import APIRouter
from schemas.temperature_converter import TemperatureConverterRequest
from services.temperature_converter_service import TemperatureConverterService

router = APIRouter(
    prefix="/temperature",
    tags=["Temperature Converter"]
)


@router.get("/")
def temperature_converter():
    return {
        "message": "Temperature Converter API"
    }


@router.post("/convert")
def convert_temperature(request: TemperatureConverterRequest):
    return TemperatureConverterService.convert(
        value=request.value,
        from_unit=request.from_unit,
        to_unit=request.to_unit,
    )