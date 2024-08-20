from tarantool import Connection

class TarantoolService:
    def __init__(self, host, port):
        self.conn = Connection(host, port)

    async def write(self, data):
        # реализация записи данных в Tarantool
        self.conn.insert("test", data)

    async def read(self, keys):
        # реализация чтения данных из Tarantool
        result = []
        for key in keys:
            data = self.conn.select("test", index="primary", limit=1, offset=0, equal=[key])
            if data:
                result.append(data[0])
        return result