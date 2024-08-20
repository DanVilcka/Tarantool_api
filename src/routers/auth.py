from fastapi import APIRouter, Depends, Body
from src.services.auth import AuthService
from src.services.tarantool import TarantoolService, get_db

auth_router = APIRouter()

@auth_router.post("/login")
async def login(username: str = Body(...), password: str = Body(...), db: TarantoolService = Depends(get_db)):
    auth_service = AuthService(db)
    return auth_service.login(username, password)

@auth_router.post("/check-token")
async def check_token(token: str = Body(...), username: str = Body(...), db: TarantoolService = Depends(get_db)):
    auth_service = AuthService(db)
    return {"result": auth_service.check_token(token, username)}