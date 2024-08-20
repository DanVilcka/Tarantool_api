import pytest
from src.services.auth import AuthService

def test_login():
    auth_service = AuthService()
    assert auth_service.login("admin", "presale") == "token"
    assert auth_service.login("admin", "wrong_password") is None