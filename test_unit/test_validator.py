import json

import pytest
from requests import Response

from src.yatl.validator import BodyFormat, validate_json_body


def test_from_content_type_json():
    "Test JSON content type."
    assert BodyFormat.from_content_type("application/json") == BodyFormat.JSON


def test_from_content_type_xml():
    "Test XML content type."
    assert BodyFormat.from_content_type("application/xml") == BodyFormat.XML


def test_from_content_type_text():
    """Test text/plain content type."""
    assert BodyFormat.from_content_type("text/plain") == BodyFormat.TEXT


class MockResponse(Response):
    """Mock response with configurable JSON content."""

    def __init__(self, json_data, status_code=200):
        super().__init__()
        self._json_data = json_data
        self.status_code = status_code
        self.headers["Content-Type"] = "application/json"

    def json(self):
        return self._json_data


def test_validate_json_body_simple():
    """Test simple flat JSON validation."""
    response = MockResponse({"name": "Alice", "age": 30})
    validate_json_body(response, {"name": "Alice", "age": 30})


def test_validate_json_body_nested():
    """Test nested object validation."""
    response = MockResponse(
        {
            "user": {"name": "Bob", "address": {"city": "Moscow", "zip": "123456"}},
            "active": True,
        }
    )
    validate_json_body(
        response,
        {
            "user": {"name": "Bob", "address": {"city": "Moscow", "zip": "123456"}},
            "active": True,
        },
    )


def test_validate_json_body_dot_notation():
    """Test dot-notation for deeply nested fields."""
    response = MockResponse({"a": {"b": {"c": 42}}, "items": [{"id": 1}, {"id": 2}]})
    validate_json_body(response, {"a.b.c": 42, "items.0.id": 1})


def test_validate_json_body_different_types():
    """Test validation of various data types."""
    response = MockResponse(
        {
            "string": "hello",
            "number": 123,
            "float": 45.67,
            "boolean": True,
            "null": None,
            "array": [1, 2, 3],
            "empty_object": {},
        }
    )
    validate_json_body(
        response,
        {
            "string": "hello",
            "number": 123,
            "float": 45.67,
            "boolean": True,
            "null": None,
            "array": [1, 2, 3],
            "empty_object": {},
        },
    )


def test_validate_json_body_empty():
    """Test empty object validation."""
    response = MockResponse({})
    validate_json_body(response, {})


def test_validate_json_body_invalid_json():
    """Test when response is not valid JSON."""

    class InvalidJSONResponse(Response):
        def __init__(self):
            super().__init__()
            self.headers["Content-Type"] = "application/json"

        def json(self):
            raise json.JSONDecodeError("Expecting value", "", 0)

    response = InvalidJSONResponse()
    with pytest.raises(AssertionError, match="Response is not valid JSON"):
        validate_json_body(response, {})


def test_validate_json_body_missing_key():
    """Test missing key in response."""
    response = MockResponse({"name": "Alice"})
    with pytest.raises(AssertionError, match="Key 'age' is missing in response"):
        validate_json_body(response, {"name": "Alice", "age": 30})


def test_validate_json_body_value_mismatch():
    """Test value mismatch."""
    response = MockResponse({"name": "Alice", "age": 30})
    with pytest.raises(AssertionError, match="For key 'age' expected '31', got '30'"):
        validate_json_body(response, {"name": "Alice", "age": 31})


def test_validate_json_body_nested_mismatch():
    """Test mismatch in nested object."""
    response = MockResponse(
        {"user": {"name": "Bob", "address": {"city": "Moscow", "zip": "123456"}}}
    )
    with pytest.raises(
        AssertionError, match="For key 'city' expected 'SPb', got 'Moscow'"
    ):
        validate_json_body(
            response,
            {"user": {"name": "Bob", "address": {"city": "SPb", "zip": "123456"}}},
        )


def test_validate_json_body_dot_notation_not_found():
    """Test when dot-notation path is not found."""
    response = MockResponse({"a": {"b": {"c": 42}}})
    with pytest.raises(AssertionError, match="Path 'a.b.d' not found in response"):
        validate_json_body(response, {"a.b.d": 42})


def test_validate_json_body_dot_notation_mismatch():
    """Test dot-notation value mismatch."""
    response = MockResponse({"a": {"b": {"c": 42}}})
    with pytest.raises(
        AssertionError, match="For path 'a.b.c' expected '43', got '42'"
    ):
        validate_json_body(response, {"a.b.c": 43})


def test_validate_json_body_type_mismatch():
    """Test type mismatch (string vs number)."""
    response = MockResponse({"count": "123"})
    with pytest.raises(
        AssertionError, match="For key 'count' expected '123', got '123'"
    ):
        validate_json_body(response, {"count": 123})
