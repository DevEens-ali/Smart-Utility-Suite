from pydantic import BaseModel, Field
from typing import Annotated


class TemperatureConverterRequest(BaseModel):
    """
    Request model for Temperature Converter.
    """

    value: Annotated[
        float,
        Field(
            ...,
            description="Enter the temperature value to convert"
        )
    ]

    from_unit: Annotated[
        str,
        Field(
            ...,
            description="Enter the source temperature unit"
        )
    ]

    to_unit: Annotated[
        str,
        Field(
            ...,
            description="Enter the target temperature unit"
        )
    ]