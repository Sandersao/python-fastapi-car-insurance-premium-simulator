from typing import Optional

from pydantic import BaseModel, Field, field_validator

from app.application.dto.car_input_dto import CarInputDTO


class InputDTO(BaseModel):
    broker_fee: float = Field(..., ge=0, json_schema_extra={"example": 50.0})
    car: CarInputDTO
    deductible_percentage: float = Field(
        ..., ge=0, le=1, json_schema_extra={"example": 0.10}
    )
    registration_location: Optional[str] = Field(
        None, json_schema_extra={"example": "São Paulo, Brazil"}
    )

    @field_validator("deductible_percentage")
    @classmethod
    def validate_deductible(cls, value: float) -> float:
        if value > 1:
            raise ValueError("Deductible percentage must be between 0 and 1")
        return value
