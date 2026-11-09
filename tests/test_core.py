"""Pruebas unitarias base para validar la infraestructura del proyecto y CI/CD."""

import logging

from ds_python_boilerplate import ROOT_DIR, get_logger, main
from ds_python_boilerplate.paths import (
    CONFIG_DIR,
    DATA_DIR,
    DOCS_DIR,
    EXTERNAL_DATA_DIR,
    INTERIM_DATA_DIR,
    MODELS_DIR,
    NOTEBOOKS_DIR,
    PROCESSED_DATA_DIR,
    RAW_DATA_DIR,
)


def test_project_paths() -> None:
    """Verifica que las rutas principales del proyecto estén bien estructuradas."""
    assert ROOT_DIR.exists()
    assert CONFIG_DIR == ROOT_DIR / "config"
    assert DATA_DIR == ROOT_DIR / "data"
    assert RAW_DATA_DIR == DATA_DIR / "raw"
    assert INTERIM_DATA_DIR == DATA_DIR / "interim"
    assert PROCESSED_DATA_DIR == DATA_DIR / "processed"
    assert EXTERNAL_DATA_DIR == DATA_DIR / "external"
    assert MODELS_DIR == ROOT_DIR / "models"
    assert NOTEBOOKS_DIR == ROOT_DIR / "notebooks"
    assert DOCS_DIR == ROOT_DIR / "docs"


def test_get_logger() -> None:
    """Verifica que el logger se configure adecuadamente sin duplicar handlers."""
    logger = get_logger("test_logger", level=logging.DEBUG)
    assert logger.name == "test_logger"
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) == 1

    # Segunda llamada no debe duplicar handlers
    logger_again = get_logger("test_logger", level=logging.INFO)
    assert len(logger_again.handlers) == 1
    assert logger_again.level == logging.INFO


def test_main_runs(capfd) -> None:  # type: ignore[no-untyped-def]
    """Verifica que el punto de entrada main() se ejecute y emita log."""
    main()
    captured = capfd.readouterr()
    assert "Proyecto inicializado desde:" in captured.out
