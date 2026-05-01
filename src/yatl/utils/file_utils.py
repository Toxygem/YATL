import os
from typing import Any

import yaml


class LoadError(Exception):
    "Base class for load errors."

    pass


class InvalidYamlError(LoadError):
    "Invalid YAML error."

    pass


class TestStructureError(LoadError):
    "Test structure error."

    pass


def load_test_yaml(file_path: str) -> dict[str, str | int | list[Any]] | bool:
    """Loads and parses a YAML test file.

    Args:
        file_path: Path to the .test.yaml or .test.yml file.

    Returns:
        The parsed YAML as a dictionary, or False if the file is not found."
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            test_specification = yaml.safe_load(f)
            if not test_specification:
                test_specification = {}
            return test_specification
    except FileExistsError:
        raise FileExistsError(f"Not a file: {file_path}")
    except yaml.YAMLError as e:
        raise InvalidYamlError(f"Invalid YAML in {file_path}: {e}")
    except UnicodeDecodeError as e:
        raise InvalidYamlError(f"Encoding error in {file_path}: {e}")


def search_files(base_path: str) -> list[str]:
    """Recursively searches for test files with a .yatl.yaml/.yatl.yml suffix.

    Args:
        base_path: Base directory for the search.

    Returns:
        List of found file paths.
    """
    files = []

    def _search(current_path: str):
        try:
            os.listdir(current_path)
        except FileNotFoundError:
            return
        for item in os.listdir(current_path):
            full_path = os.path.join(current_path, item)
            if os.path.isfile(full_path) and (
                item.endswith(".yatl.yaml") or item.endswith(".yatl.yml")
            ):
                files.append(full_path)
            elif os.path.isdir(full_path):
                _search(full_path)

    _search(base_path)
    return files
