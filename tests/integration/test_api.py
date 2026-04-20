from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_simulate_endpoint():
    payload = {
        "car": {"make": "Toyota", "model": "Corolla", "year": 2015, "value": 100000},
        "deductible_percentage": 0.1,
        "broker_fee": 50,
    }

    response = client.post("/api/v1/simulate", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["applied_rate"] > 0
    assert data["calculated_premium"] > 0
    assert data["policy_limit"] > 0
    assert data["deductible_value"] > 0


def test_simulate_expected_values():
    payload = {
        "car": {
            "make": "Toyota",
            "model": "Corolla",
            "year": 2015,
            "value": 100000,
        },
        "deductible_percentage": 0.1,
        "broker_fee": 50,
    }

    response = client.post("/api/v1/simulate", json=payload)
    data = response.json()

    assert round(data["calculated_premium"], 2) > 0


def test_simulate_expected_values_registration_location():
    payload = {
        "car": {
            "make": "Toyota",
            "model": "Corolla",
            "year": 2015,
            "value": 100000,
        },
        "deductible_percentage": 0.1,
        "broker_fee": 50,
        "registration_location": "São Paulo, Brazil",
    }

    response = client.post("/api/v1/simulate", json=payload)
    data = response.json()

    assert round(data["calculated_premium"], 2) > 0


def test_simulate_invalid_input():
    payload = {
        "car": {
            "make": "Toyota",
            "model": "Corolla",
            "year": 2050,
            "value": 100000,
        },
        "deductible_percentage": 0.1,
        "broker_fee": 50,
    }

    response = client.post("/api/v1/simulate", json=payload)

    assert response.status_code == 422


def test_simulate_missing_field():
    payload = {
        "car": {
            "make": "Toyota",
            "model": "Corolla",
            "value": 100000,
        },
        "deductible_percentage": 0.1,
        "broker_fee": 50,
    }

    response = client.post("/api/v1/simulate", json=payload)

    assert response.status_code == 422
