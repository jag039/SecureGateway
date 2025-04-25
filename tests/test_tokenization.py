from fastapi.testclient import TestClient
from app.main import app
from app.services.auth import encode_jwt
from datetime import timedelta


client = TestClient(app)


def test_tokenize_success():
    payload = {"sub": "test-user-123", "role": "processor"}
    token = encode_jwt(payload, expires_delta=timedelta(hours=0.001))

    headers = {"Authorization": f"Bearer {token}"}
    payload = {"card_number": "4111111111111111", "cvv": "123", "expiry": "04/26"}
    response = client.post("/tokenize", json=payload, headers=headers)
    assert response.status_code == 200
    assert "token" in response.json()


def test_invalid_token():
    token = "invlaid token"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"card_number": "4111111111111111", "cvv": "123", "expiry": "04/26"}
    response = client.post("/tokenize", json=payload, headers=headers)
    assert response.status_code == 401


def test_tokenize_forbidden_role():
    payload = {"sub": "hacker-001", "role": "attacker"}
    token = encode_jwt(payload, expires_delta=timedelta(hours=0.001))
    headers = {"Authorization": f"Bearer {token}"}

    body = {"card_number": "4111111111111111", "cvv": "123", "expiry": "04/26"}

    response = client.post("/tokenize", json=body, headers=headers)

    assert response.status_code == 403
    assert response.json()["detail"] == "Not authorized"
