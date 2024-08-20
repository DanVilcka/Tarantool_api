import pytest
from src.services.tarantool import TarantoolService

def test_read():
    tarantool_service = TarantoolService()
    tarantool_service.write({"key1": "value1", "key2": "value2"})
    assert tarantool_service.read(["key1", "key2"]) == {"key1": "value1", "key2": "value2"}