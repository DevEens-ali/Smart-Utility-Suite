from fastapi import FastAPI

from routers.basic_calculator import router as basic_router
from routers.cgpa_calculator import router as cgpa_router
from routers.gpa_calculator import router as gpa_router
from routers.bmi_calculator import router as bmi_router
from routers.age_calculator import router as age_router
from routers.scientific_calculator import router as scientific_router
from routers.length_converter import router as length_converter_router
from routers.weight_converter import router as weight_converter_router
from routers.temperature_converter import router as temperature_converter_router
from routers.volume_converter import router as volume_converter_router
from routers.area_converter import router as area_converter_router

app = FastAPI()

@app.get("/health")
def health():
    return {
        "status": "Backend is running"
    }

app.include_router(basic_router)
app.include_router(cgpa_router)
app.include_router(gpa_router)
app.include_router(bmi_router)
app.include_router(age_router)
app.include_router(scientific_router)
app.include_router(length_converter_router)
app.include_router(weight_converter_router)
app.include_router(temperature_converter_router)
app.include_router(volume_converter_router)
app.include_router(area_converter_router)

