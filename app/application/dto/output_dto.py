from pydantic import BaseModel

from app.application.dto.car_output_dto import CarOutputDTO


class OutputDTO(BaseModel):
    car: CarOutputDTO
    applied_rate: float
    calculated_premium: float
    deductible_value: float
    policy_limit: float
