from pydantic import BaseModel, Field


class CarDTO(BaseModel):
    make: str = Field(
        ...,
        min_length=1,
        description="Car brand",
        json_schema_extra={"example": "Toyota"},
    )
    model: str = Field(
        ...,
        min_length=1,
        description="Car model",
        json_schema_extra={"example": "Corolla"},
    )
    value: float = Field(
        ..., gt=0, description="Car value", json_schema_extra={"example": 100000}
    )
    year: int = Field(
        ..., ge=1886, description="Year of the car", json_schema_extra={"example": 2012}
    )
