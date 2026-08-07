from pydantic import BaseModel, Field
from typing import Literal


class BasicCalculatorRequest(BaseModel):
    """
    Request model for Basic Calculator.
    """

    num1: float = Field(
        ...,
        description="First Number"
    )

    num2: float = Field(
        ...,
        description="Second Number"
    )

    operation: Literal["+", "-", "*", "/"] = Field(
        ...,
        description="Mathematical Operation"
    )
