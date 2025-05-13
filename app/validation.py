from pydantic import BaseModel, field_validator
from typing import List

# Define a Pydantic model
class PredictionInput(BaseModel):
   
    data: List[float]

    # Validator to check if the input list contains 4 values
    @field_validator("data")
    @classmethod
    def check_length(cls, v):
        if len(v) != 4:
            raise ValueError("data must contain exactly 4 float values")
        return v

    # Provide an example schema for documentation
    class Config:
        json_schema_extra = {
            "example": {
                "data": [5.1, 3.5, 1.4, 0.2], 
            }
        }