from pydantic import BaseModel


class OutputDTO(BaseModel):
    applied_rate: float
    calculated_premium: float
    deductible_value: float
    policy_limit: float
