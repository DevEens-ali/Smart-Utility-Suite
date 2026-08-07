from pydantic import BaseModel, Field
from typing import Annotated


class BMICalculatorRequest(BaseModel):
    """
    Request model for BMI Calculator.
    """

    height: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="Enter height in meters",
            examples=[1.72],
        ),
    ]

    weight: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="Enter weight in kilograms",
            examples=[70.5],
        ),
    ]
