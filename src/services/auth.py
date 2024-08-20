from jose import jwt, JWTError

async def authenticate_user(username: str, password: str):
    # реализация аутентификации пользователя
    pass

async def validate_token(token: str):
    try:
        jwt.decode(token, secret_key="secret_key", algorithms=["HS256"])
    except JWTError:
        raise JWTError