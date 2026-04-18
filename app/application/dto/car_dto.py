from pydantic import BaseModel, Field


class CarDTO(BaseModel):
    make: str = Field(..., min_length=1, example="Toyota", description="Car brand")
    model: str = Field(..., min_length=1, example="Corolla", description="Car model")
    value: float = Field(..., gt=0, example=100000.0, description="Car value")
    year: int = Field(..., ge=1886, example=2012, description="Year of the car")
