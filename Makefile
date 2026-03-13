check:
	poetry run ruff check . --fix

format:
	poetry run ruff format .

run_server:
	poetry run python src/yatl/server.py

run_yaml:
	poetry run python -m src.yatl.run

test:
	poetry run pytest