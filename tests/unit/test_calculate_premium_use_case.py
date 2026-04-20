from datetime import datetime

import pytest

from app.application.dto.car_input_dto import CarInputDTO
from app.application.dto.input_dto import InputDTO
from app.application.use_cases.calculate_premium import CalculatePremiumUseCase


class FakeDate(datetime):
    @classmethod
    def now(cls):
        return cls(2025, 1, 1)


class FakeGIS:
    def __init__(self):
        self.called = False

    def get_risk_adjustment(self, location):
        self.called = True
        return 0.02


def test_use_case_with_gis():
    use_case = CalculatePremiumUseCase(gis_service=FakeGIS())

    input_dto = InputDTO(
        car=CarInputDTO(make="Toyota", model="Corolla", year=2015, value=100000),
        deductible_percentage=0.1,
        broker_fee=50,
        registration_location="São Paulo",
    )

    result = use_case.execute(input_dto)

    current_year = datetime.now().year
    age = current_year - 2015

    expected_rate = age * 0.005 + (100000 / 10000) * 0.005 + 0.02

    assert round(result.applied_rate, 5) == round(expected_rate, 5)


def test_use_case_applies_gis_adjustment():
    fake = FakeGIS()
    use_case = CalculatePremiumUseCase(gis_service=fake)

    input_dto = InputDTO(
        car=CarInputDTO(make="Toyota", model="Corolla", year=2015, value=100000),
        deductible_percentage=0.1,
        broker_fee=50,
        registration_location="São Paulo",
    )

    use_case.execute(input_dto)

    assert fake.called is True


def test_premium_is_consistent():
    use_case = CalculatePremiumUseCase()

    input_dto = InputDTO(
        car=CarInputDTO(make="Toyota", model="Corolla", year=2015, value=100000),
        deductible_percentage=0.1,
        broker_fee=50,
    )

    result = use_case.execute(input_dto)

    assert result.calculated_premium >= 0
    assert result.policy_limit > 0
    assert result.deductible_value > 0


def test_use_case_exact_with_gis(monkeypatch):
    monkeypatch.setattr("app.domain.services.premium_calculator.datetime", FakeDate)

    use_case = CalculatePremiumUseCase(gis_service=FakeGIS())

    input_dto = InputDTO(
        car=CarInputDTO(make="Toyota", model="Corolla", year=2015, value=100000),
        deductible_percentage=0.1,
        broker_fee=50,
        registration_location="São Paulo, Brazil",
    )

    result = use_case.execute(input_dto)

    assert result.car.make == "Toyota"
    assert result.car.model == "Corolla"
    assert result.car.value == 100000
    assert result.car.year == 2015

    assert result.applied_rate == pytest.approx(0.12)
    assert result.calculated_premium == pytest.approx(10850)
    assert result.deductible_value == pytest.approx(10000)
    assert result.policy_limit == pytest.approx(90000)
