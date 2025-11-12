import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_activity():
    # Usando una actividad existente: 'Basketball Club'
    email = "testuser@mergington.edu"
    response = client.post("/activities/Basketball Club/signup?email=" + email)
    assert response.status_code in (200, 400)  # Puede ser 400 si ya está inscrito o no hay cupo
    data = response.json()
    assert "message" in data or "detail" in data

def test_unregister_activity():
    email = "testuser@mergington.edu"
    response = client.post("/activities/Basketball Club/unregister?email=" + email)
    assert response.status_code in (200, 400)
    data = response.json()
    assert "message" in data or "detail" in data
