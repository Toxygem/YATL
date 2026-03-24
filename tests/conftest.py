import pytest


@pytest.fixture
def data_extractor():
    from src.yatl.extractor import DataExtractor

    return DataExtractor()


@pytest.fixture
def template_render():
    from src.yatl.render import TemplateRenderer

    return TemplateRenderer()


@pytest.fixture
def runner(template_render, data_extractor):
    from src.yatl.run import Runner

    return Runner(data_extractor, template_render)


@pytest.fixture
def data():
    return {
        "base_url": "https://yandex.ru",
        "name": "ping",
        "steps": [
            {
                "expect": {"status": 200},
                "name": "ok_test",
                "request": {"method": "GET"},
            },
            {
                "expect": {"status": 404},
                "name": "not_found_test",
                "request": {"method": "GET", "url": "/not_found"},
            },
        ],
    }
