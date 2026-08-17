from pydantic import BaseModel, Field
from typing import Annotated


class VolumeConverterRequest(BaseModel):
    """
    Request model for Volume Converter.
    """

    value: Annotated[
        float,
        Field(
            ...,
            description="Enter the volume value to convert"
        )
    ]

    from_unit: Annotated[
        str,
        Field(
            ...,
            description="Enter the source volume unit"
        )
    ]

    to_unit: Annotated[
        str,
        Field(
            ...,
            description="Enter the target volume unit"
        )
    ]
    