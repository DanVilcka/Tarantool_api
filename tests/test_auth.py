import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_login():
    response = client.post("/api/login", json={"username": "test", "password": "test"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_invalid_login():
    response = client.post("/api/login", json={"username": "test", "password": "wrong"})
    assert response.status_code == 401