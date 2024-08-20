from fastapi import APIRouter, Depends, Body
from src.services.tarantool import TarantoolService

read_router = APIRouter()

@read_router.post("/read")
async def read(key: str = Body(...), tarantool_service: TarantoolService = Depends()):
    return tarantool_service.read("data", key, "")