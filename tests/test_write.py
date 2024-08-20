import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_write():
    response = client.post("/api/login", json={"username": "test", "password": "test"})
    token = response.json()["access_token"]
    response = client.post("/api/write", json={"key": "test", "value": "test"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert "status" in response.json()

def test_invalid_token():
    response = client.post("/api/write", json={"key": "test", "value": "test"}, headers={"Authorization": "Bearer wrong"})
    assert response.status_code == 401