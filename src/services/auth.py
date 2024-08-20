from typing import Optional
from src.utils import hash_password, verify_password
from src.services.tarantool import TarantoolService

class AuthService:
    def __init__(self, tarantool_service: TarantoolService):
        self.tarantool_service = tarantool_service

    def login(self, username: str, password: str) -> dict:
        stored_password = self.tarantool_service.read("tokens", username, "")
        stored_password = stored_password["data"].get(username)
        if not stored_password:
            return {"error": "Пользователь не существует"}
        elif not verify_password(password, stored_password):
            return {"error": "Неправильный пароль"}
        import uuid
        token = str(uuid.uuid4())
        self.tarantool_service.add_token(username, token)
        return {"token": token}

    def register(self, username: str, password: str) -> dict:
        stored_password = self.tarantool_service.read("tokens", username, "")
        if stored_password["data"].get(username):
            return {"error": "Пользователь уже существует"}
        hashed_password = hash_password(password)
        self.tarantool_service.write("tokens", {username: hashed_password}, "")
        import uuid
        token = str(uuid.uuid4())
        self.tarantool_service.add_token(username, token)
        return {"token": token}

    def check_token(self, token: str, username: str) -> bool:
        stored_token = self.tarantool_service.get_token(username)
        return stored_token == token