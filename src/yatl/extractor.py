from requests import Response
from enum import Enum


class ContentType(Enum):
    JSON = "application/json"
    HTML = "text/html"
    XML = "application/xml"


class DataExtractor:
    def __init__(self):
        pass

    def extract(self, response: Response, extract_spec: dict):
        extracted = {}
        if response.headers.get("content-type") == ContentType.JSON.value:
            resp_json = response.json()

            for key, path in extract_spec.items():
                if path is None:
                    if resp_json and key in resp_json:
                        extracted[key] = resp_json[key]
                    else:
                        raise ValueError(f"Field '{key}' not found in JSON response")
                else:
                    if resp_json and path in resp_json:
                        extracted[key] = resp_json[path]
                    else:
                        raise ValueError(f"Failed to extract '{key}' at path '{path}'")
        elif response.headers.get("content-type") == ContentType.HTML.value:
            pass

        elif response.headers.get("content-type") == ContentType.XML.value:
            pass

        return extracted
