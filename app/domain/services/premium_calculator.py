from datetime import datetime

from app.domain.value_objects.premium_result import PremiumResult


class PremiumCalculator:
    def __init__(self, config):
        self.config = config

    def __calculate_car_age(self, car_year: int) -> int:
        current_year = datetime.now().year
        return current_year - car_year

    def calculate_rate(self, car_year: int, car_value: float) -> float:
        car_age = self.__calculate_car_age(car_year)
        age_rate = car_age * self.config.rate_per_year
        value_rate = (
            car_value / self.config.value_step
        ) * self.config.rate_per_value_step
        return age_rate + value_rate

    def __premium_calculation(
        self, car, deductible_percentage: float, broker_fee: float, rate: float
    ):
        base_premium = car.value * rate
        discount = base_premium * deductible_percentage
        return base_premium - discount + broker_fee

    def calculate(
        self, car, deductible_percentage: float, broker_fee: float, rate: float
    ) -> PremiumResult:

        base_policy_limit = car.value * self.config.coverage_percentage
        deductible_value = base_policy_limit * deductible_percentage
        final_policy_limit = base_policy_limit - deductible_value
        final_premium = self.__premium_calculation(
            car, deductible_percentage, broker_fee, rate
        )

        return PremiumResult(
            applied_rate=rate,
            car=car,
            calculated_premium=final_premium,
            deductible_value=deductible_value,
            policy_limit=final_policy_limit,
        )
