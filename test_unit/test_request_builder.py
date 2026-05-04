from src.yatl.request_builder import build_url, extract_request_params, process_body


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
