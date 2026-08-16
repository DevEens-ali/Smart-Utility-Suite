from pydantic import BaseModel, Field
from typing import Annotated


class ScientificCalculatorRequest(BaseModel):
    """
    Request model for the Scientific Calculator.
    """

    input_expression: Annotated[
        str,
        Field(..., description="Enter Mathematical Expression")
    ]
  
