from datetime import date

from pydantic import BaseModel, Field
from typing import Annotated


class AgeCalculatorRequest(BaseModel):
    """
    Request model for Age Calculator.
    """

    date_of_birth: Annotated[
        date,
        Field(
            ...,
            description="Enter your date of birth",
            examples=["2004-08-15"],
        ),
    ]
