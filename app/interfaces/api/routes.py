from fastapi import APIRouter

from app.application.dto.input_dto import InputDTO
from app.application.use_cases.calculate_premium import CalculatePremiumUseCase

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/simulate")
def simulate(data: InputDTO):
    use_case = CalculatePremiumUseCase()
    return use_case.execute(data)
