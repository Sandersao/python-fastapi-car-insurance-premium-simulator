import pytest
from pydantic import ValidationError

from app.application.dto.car_input_dto import CarInputDTO
from app.application.dto.input_dto import InputDTO


def test_invalid_deductible():
    with pytest.raises(ValidationError) as exc_info:
        InputDTO(
            car=CarInputDTO(make="Toyota", model="Corolla", year=2015, value=100000),
            deductible_percentage=2,
            broker_fee=50,
        )
    assert "deductible_percentage" in str(exc_info.value)


def test_invalid_deductible_too_high():
    with pytest.raises(ValueError) as exc_info:
        InputDTO(
            car=CarInputDTO(make="Toyota", model="Corolla", year=2015, value=100000),
            deductible_percentage=2.0,
            broker_fee=50,
        )

    errors = exc_info.value.errors()

    assert any(err["loc"] == ("deductible_percentage",) for err in errors)


def test_invalid_deductible_negative():
    with pytest.raises(ValidationError):
        InputDTO(
            car=CarInputDTO(make="Toyota", model="Corolla", year=2015, value=100000),
            deductible_percentage=-0.1,
            broker_fee=50,
        )


def test_valid_deductible():
    dto = InputDTO(
        car=CarInputDTO(make="Toyota", model="Corolla", year=2015, value=100000),
        deductible_percentage=0.1,
        broker_fee=50,
    )

    assert dto.deductible_percentage == pytest.approx(0.1)


def test_input_dto_contract():
    dto = InputDTO(
        car=CarInputDTO(make="Toyota", model="Corolla", year=2015, value=100000),
        deductible_percentage=0.1,
        broker_fee=50,
        registration_location="SP",
    )

    assert dto.car.make == "Toyota"
    assert dto.deductible_percentage == pytest.approx(0.1)
    assert dto.broker_fee == 50
