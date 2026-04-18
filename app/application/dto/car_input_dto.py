from datetime import datetime

from pydantic import field_validator

from app.application.dto.car_dto import CarDTO


class CarInputDTO(CarDTO):
    @field_validator("year")
    @classmethod
    def validate_year(cls, value: int) -> int:
        current_year = datetime.now().year
        if value > current_year:
            raise ValueError("Car year cannot be in the future")
        return value
