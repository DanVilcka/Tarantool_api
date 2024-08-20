from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Data(BaseModel):
    key: str
    value: str

class ReadRequest(BaseModel):
    keys: list[str]

class WriteRequest(BaseModel):
    key: str
    value: str