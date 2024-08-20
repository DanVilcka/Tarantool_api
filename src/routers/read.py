from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.services import auth as auth_service
from src.services import tarantool as tarantool_service

from jose import JWTError

router = APIRouter()

@router.post("/api/read")
async def read(keys: list, token: str = Depends(OAuth2PasswordBearer())):
    try:
        await auth_service.validate_token(token)
    except JWTError:
        raise HTTPException(status_code=401, detail="Неправильный токен")
    data = await tarantool_service.read(keys)
    return {"data": data}