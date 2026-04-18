from datetime import datetime

from app.domain.value_objects.premium_result import PremiumResult


class PremiumCalculator:
    def __init__(self, config):
        self.config = config

    def calculate_car_age(self, car_year: int) -> int:
        current_year = datetime.now().year
        return current_year - car_year

    def calculate_rate(self, car_year: int, car_value: float) -> float:
        car_age = self.calculate_car_age(car_year)
        age_rate = car_age * self.config.rate_per_year
        value_rate = (
            car_value / self.config.value_step
        ) * self.config.rate_per_value_step
        return age_rate + value_rate

    def calculate(
        self, car, deductible_percentage: float, broker_fee: float, rate: float
    ) -> PremiumResult:
        base_premium = car.value * rate
        discount = base_premium * deductible_percentage
        final_premium = base_premium - discount + broker_fee

        base_policy_limit = car.value * self.config.coverage_percentage
        deductible_value = base_policy_limit * deductible_percentage
        final_policy_limit = base_policy_limit - deductible_value

        return PremiumResult(
            car=car,
            applied_rate=rate,
            calculated_premium=final_premium,
            policy_limit=final_policy_limit,
            deductible_value=deductible_value,
        )
