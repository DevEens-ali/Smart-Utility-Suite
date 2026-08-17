from pydantic import BaseModel, Field
from typing import Annotated


class AreaConverterRequest(BaseModel):
    """
    Request model for Area Converter.
    """

    value: Annotated[
        float,
        Field(
            ...,
            description="Enter the area value to convert"
        )
    ]

    from_unit: Annotated[
        str,
        Field(
            ...,
            description="Enter the source area unit"
        )
    ]

    to_unit: Annotated[
        str,
        Field(
            ...,
            description="Enter the target area unit"
        )
    ]