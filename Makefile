.PHONY: help install install-all lint format typecheck test check clean

help: ## Muestra esta ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Instala el entorno virtual con dependencias de desarrollo
	uv sync --dev

install-all: ## Instala todas las dependencias incluyendo soporte para Jupyter Notebooks
	uv sync --all-groups

lint: ## Ejecuta Ruff linter
	uv run ruff check .

format: ## Formatea el código con Ruff
	uv run ruff check --fix .
	uv run ruff format .

typecheck: ## Ejecuta el chequeo estático de tipos con Mypy
	uv run mypy src/

test: ## Ejecuta pruebas unitarias y reporte de cobertura
	uv run pytest tests/ --cov=src --cov-report=term-missing --cov-report=xml:coverage.xml --junitxml=test-results.xml

check: lint typecheck test ## Ejecuta todas las validaciones de calidad localmente (linter + tipos + tests)

clean: ## Elimina cachés y artefactos temporales
	rm -rf .pytest_cache .ruff_cache .mypy_cache .coverage coverage.xml test-results.xml htmlcov dist build
