from pydantic import BaseModel, Field
from typing import Annotated


class LengthConverterRequest(BaseModel):
    """
    Request model for Length Converter.
    """

    value: Annotated[
        float,
        Field(
            ...,
            description="Enter the value to convert"
        )
    ]

    from_unit: Annotated[
        str,
        Field(
            ...,
            description="Enter the unit to convert from"
        )
    ]

    to_unit: Annotated[
        str,
        Field(
            ...,
            description="Enter the unit to convert to"
        )
    ]