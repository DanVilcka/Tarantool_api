from fastapi import FastAPI
from src.routers import auth_router, read_router, write_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(read_router)
app.include_router(write_router)