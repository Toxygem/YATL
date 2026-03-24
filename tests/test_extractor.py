import pytest


def test_get_nested_value(data_extractor):
    data = {
        "id": 1,
        "info": {
            "email": "example.com",
            "age": 32,
        },
    }
    path = "info.age"
    assert data_extractor._get_nested_value(data, path) == 32


def test_get_nested_not_found_value(data_extractor):
    data = {
        "id": 1,
        "info": {
            "email": "example.com",
            "age": 32,
        },
    }
    path = "info.user.age"
    with pytest.raises(ValueError):
        data_extractor._get_nested_value(data, path)
