from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_flow():

    response = client.get("/api/v1/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"


def test_full_simulation_flow():
    payload = {
        "car": {"make": "Toyota", "model": "Corolla", "year": 2015, "value": 100000},
        "deductible_percentage": 0.1,
        "broker_fee": 50,
    }

    response = client.post("/api/v1/simulate", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["calculated_premium"] > 0
    assert data["policy_limit"] > 0
