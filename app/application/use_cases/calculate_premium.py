from datetime import datetime

from app.application.dto.input_dto import InputDTO
from app.application.dto.output_dto import OutputDTO
from app.domain.services.premium_calculator import PremiumCalculator
from app.infrastructure.config.settings import Settings
from app.infrastructure.gis.gis_service import GISService


class CalculatePremiumUseCase:
    def __init__(
        self,
        calculator: PremiumCalculator | None = None,
        config: Settings | None = None,
        gis_service: GISService | None = None,
    ):
        self.config = config or Settings()
        self.calculator = calculator or PremiumCalculator(self.config)
        self.gis_service = gis_service or GISService()

    def execute(self, input_dto: InputDTO) -> OutputDTO:
        car = input_dto.car
        current_year = datetime.now().year
        car_age = current_year - car.year

        rate = self.calculator.calculate_rate(
            car_age=car_age,
            car_value=car.value,
        )

        if input_dto.registration_location:
            adjustment = self.gis_service.get_risk_adjustment(
                input_dto.registration_location
            )
            rate += adjustment

        result = self.calculator.calculate(
            car=car,
            deductible_percentage=input_dto.deductible_percentage,
            broker_fee=input_dto.broker_fee,
            rate=rate,
        )

        return OutputDTO(
            applied_rate=result["applied_rate"],
            calculated_premium=result["calculated_premium"],
            deductible_value=result["deductible_value"],
            policy_limit=result["policy_limit"],
        )
