from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt

from src.services import auth as auth_service

router = APIRouter()

@router.post("/api/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Неправильный логин или пароль")
    access_token = jwt.encode({"sub": user.username}, secret_key="secret_key", algorithm="HS256")
    return {"access_token": access_token, "token_type": "bearer"}