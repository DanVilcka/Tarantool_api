import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read():
    response = client.post("/api/login", json={"username": "test", "password": "test"})
    token = response.json()["access_token"]
    response = client.post("/api/read", json={"keys": ["test"]}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert "data" in response.json()

def test_invalid_token():
    response = client.post("/api/read", json={"keys": ["test"]}, headers={"Authorization": "Bearer wrong"})
    assert response.status_code == 401