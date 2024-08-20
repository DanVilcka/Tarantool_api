import tarantool
import os
from typing import Optional

TARANTOOL_HOST = os.environ.get('TARANTOOL_HOST', '127.0.0.1')
TARANTOOL_PORT = os.environ.get('TARANTOOL_PORT', 3301)

class TarantoolService:
    def __init__(self):
        self.conn = tarantool.connect(TARANTOOL_HOST, TARANTOOL_PORT)

    def write(self, table_name: str, data: dict[str, str], token: str) -> dict:
        batch_data = []
        for key, value in data.items():
            batch_data.append([key, value])
        self.conn.space[table_name].insert(batch_data)
        return {"status": "success"}

    def read(self, table_name: str, key: str, token: str) -> dict:
        response = self.conn.space[table_name].select([key])
        if response:
            return {"data": {response[0][1]: response[0][2]}}
        else:
            return {"data": {}}

    def add_token(self, username: str, token: str) -> dict:
        self.conn.space.tokens.insert([token, username, token])
        return {"status": "success"}

    def get_token(self, username: str) -> Optional[str]:
        response = self.conn.space.tokens.select([username])
        if response:
            return response[0][0]
        else:
            return None

def get_db():
    db = TarantoolService()
    try:
        yield db
    finally:
        pass