from typing import Optional

from pydantic import BaseModel, Field

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
