.PHONY: help clean test lint format type-check docs install dev-install

help:
	@echo "Available commands:"
	@echo "  make install      Install the package"
	@echo "  make dev-install  Install with dev dependencies"
	@echo "  make test        Run tests"
	@echo "  make lint        Run linters"
	@echo "  make format      Format code"
	@echo "  make type-check  Run type checking"
	@echo "  make docs        Build documentation"
	@echo "  make clean       Clean build artifacts"

install:
	pip install -e .

dev-install:
	pip install -e ".[dev,docs]"
	pre-commit install

test:
	pytest

lint:
	flake8 src tests
	isort --check-only src tests
	black --check src tests

format:
	isort src tests
	black src tests

type-check:
	mypy src

docs:
	cd docs && make html

clean:
	rm -rf build dist *.egg-info
	rm -rf .pytest_cache .coverage htmlcov
	rm -rf docs/_build
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
