from src.yatl.request_builder import build_url, extract_request_params, process_body

from unittest.mock import patch

import pytest
import requests

from yatl.exceptions import YATLRequestError
from src.yatl.request_builder import send_request

def test_build_url():
    assert build_url("google.com", "") == "https://google.com/"


def test_build_url_with_path():
    assert build_url("google.com", "search") == "https://google.com/search"


def test_build_url_with_http_prefix():
    assert build_url("google.com", "https://api/v1") == "https://api/v1"


def test_extract_request_params():
    assert extract_request_params({"method": "GET", "url": "https://google.com"}) == (
        "GET",
        "https://google.com",
        None,
        {},
        {},
        {},
        None,
    )


def test_process_body_preserves_existing_content_type():
    body = {"json": {"name": "John"}}
    headers = {"Content-Type": "application/json"}
    kwargs = {}
    process_body(body, headers, kwargs)
    assert headers == {"Content-Type": "application/json"}
    assert kwargs == {"json": {"name": "John"}}


def test_process_body_string():
    body = "plain text"
    headers = {}
    kwargs = {}
    process_body(body, headers, kwargs)
    assert kwargs == {"data": "plain text"}
    assert headers == {"Content-Type": "text/plain"}


def test_process_body_xml():
    body = {"xml": "<user><name>John</name></user>"}
    headers = {}
    kwargs = {}
    process_body(body, headers, kwargs)
    assert kwargs == {"data": "<user><name>John</name></user>"}
    assert headers == {"Content-Type": "application/xml"}



CONTEXT = {"base_url": "https://api.example.com"}

RESOLVED_STEP = {
    "request": {
        "method": "GET",
        "url": "/users",
    }
}

def test_send_request_raises_yatl_request_error_on_timeout_without_value():
    "Test that send_request raises YATLRequestError on timeout with no timeout set."
    with patch("src.yatl.request_builder.request") as mock_request:
        mock_request.side_effect = requests.exceptions.Timeout()

        with pytest.raises(YATLRequestError, match="Request timed out \\(no explicit timeout set\\): GET"):
            send_request(CONTEXT, RESOLVED_STEP)


def test_send_request_raises_yatl_request_error_on_timeout_with_value():
    "Test that send_request raises YATLRequestError on timeout with timeout value."
    resolved_step_with_timeout = {
        "request": {
            "method": "GET",
            "url": "/users",
            "timeout": 30,
        }
    }
    with patch("src.yatl.request_builder.request") as mock_request:
        mock_request.side_effect = requests.exceptions.Timeout()

        with pytest.raises(YATLRequestError, match="Request timed out after 30s: GET"):
            send_request(CONTEXT, resolved_step_with_timeout)


def test_send_request_raises_yatl_request_error_on_connection_error():
    "Test that send_request raises YATLRequestError on connection error."
    with patch("src.yatl.request_builder.request") as mock_request:
        mock_request.side_effect = requests.exceptions.ConnectionError()

        with pytest.raises(YATLRequestError, match="Connection failed: GET"):
            send_request(CONTEXT, RESOLVED_STEP)


def test_send_request_returns_response_on_success():
    "Test that send_request returns the response object on success."
    with patch("src.yatl.request_builder.request") as mock_request:
        mock_request.return_value = "mock_response"

        result = send_request(CONTEXT, RESOLVED_STEP)

        assert result == "mock_response"