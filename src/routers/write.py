from fastapi import APIRouter, Depends, Body
from src.services.tarantool import TarantoolService

write_router = APIRouter()

@write_router.post("/write")
async def write(data: dict = Body(...), tarantool_service: TarantoolService = Depends()):
    return tarantool_service.write("data", data, "")