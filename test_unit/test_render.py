def test_render_template(template_render):
    "Test that render_template returns a rendered template."
    data = {
        "user": "{{ name }}",
        "items": ["{{id}}", "static"],
        "nested": {"key": "{{ value }}"},
    }
    context = {"name": "Alice", "id": 42, "value": "secret"}
    result = template_render.render_data(data, context)
    assert result == {
        "user": "Alice",
        "items": ["42", "static"],
        "nested": {"key": "secret"},
    }
