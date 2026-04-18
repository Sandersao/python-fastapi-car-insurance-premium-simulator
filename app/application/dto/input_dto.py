from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class CarDTO(BaseModel):
    make: str = Field(..., min_length=1, example="Toyota", description="Car branch")
    model: str = Field(..., min_length=1, example="Corolla", description="Car model")
    value: float = Field(..., gt=0, example=100000.0, description="Car value")
    year: int = Field(..., ge=1886, example=2012, description="Year of the car")

    @field_validator("year")
    @classmethod
    def validate_year(cls, value: int) -> int:
        current_year = datetime.now().year
        if value > current_year:
            raise ValueError("Car year cannot be in the future")
        return value


class InputDTO(BaseModel):
    broker_fee: float = Field(..., ge=0, example=50.0)
    car: CarDTO
    deductible_percentage: float = Field(..., ge=0, le=1, example=0.10)
    registration_location: Optional[str] = Field(None, example="São Paulo, Brazil")

    @field_validator("deductible_percentage")
    @classmethod
    def validate_deductible(cls, value: float) -> float:
        if value > 1:
            raise ValueError("Deductible percentage must be between 0 and 1")
        return value
