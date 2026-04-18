from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/simulate")
def simulate():
    return {
        "applied_rate": 0.1,
        "calculated_premium": 9000,
        "policy_limit": 90000,
        "deductible_value": 10000,
    }