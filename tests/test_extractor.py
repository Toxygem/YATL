import pytest
from src.yatl.utils import get_nested_value


def test_get_nested_value():
    data = {
        "id": 1,
        "info": {
            "email": "example.com",
            "age": 32,
        },
    }
    path = "info.age"
    assert get_nested_value(data, path) == 32


def test_get_nested_not_found_value():
    data = {
        "id": 1,
        "info": {
            "email": "example.com",
            "age": 32,
        },
    }
    path = "info.user.age"
    with pytest.raises(ValueError):
        get_nested_value(data, path)
