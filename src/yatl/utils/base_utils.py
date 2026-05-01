from typing import Any

from requests import Response


def is_skipped(item: dict[str, bool]) -> bool:
    """Checks if an item is skipped based on the "skip" flag.

    Args:
        item: The parsed YAML dictionary.

    Returns:
        True if the item is skipped, False otherwise.
    """
    return item.get("skip", False)


def get_content_type(response: Response) -> str:
    """Extracts the media type from the response's Content-Type header.

    Returns:
        The media type without parameters, lowercased.
        If the header is missing, returns an empty string.
    """
    ct = response.headers.get("content-type", "")
    return ct.split(";")[0].strip().lower()


def get_nested_value(data: Any, path: str) -> Any:
    """Retrieve a value from a nested dict using dot notation.

    Args:
        data: A dictionary (or list) containing the data.
        path: A dot-separated string representing the path (e.g., "user.email").

    Returns:
        The value at the given path.

    Raises:
        ValueError: If any component of the path does not exist.
    """
    keys = path.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list) and key.isdigit() and int(key) < len(current):
            current = current[int(key)]
        elif isinstance(current, list):
            raise ValueError(f"Path component '{key}' is not an index in {current}")
        else:
            raise ValueError(f"Path component '{key}' not found in {current}")
    return current
