.PHONY: install lint format test run pre-commit

install:
	poetry install

lint:
	poetry run black domain infrastructure tests
	poetry run isort domain infrastructure tests
	poetry run mypy domain infrastructure tests
	poetry run flake8 domain infrastructure tests

format:
	make lint

test:
	poetry run python -m pytest

run:
	poetry run python main.py

pre-commit:
	poetry run pre-commit run --all-files
