from dataclasses import dataclass

from app.domain.value_objects.car import Car


@dataclass(frozen=True)
class PremiumResult:
    car: Car
    applied_rate: float
    calculated_premium: float
    deductible_value: float
    policy_limit: float
