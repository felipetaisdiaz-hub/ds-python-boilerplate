"""Paquete principal del proyecto Data Science."""

from ds_python_boilerplate.logger import get_logger
from ds_python_boilerplate.paths import ROOT_DIR

__all__ = ["ROOT_DIR", "get_logger", "main"]


def main() -> None:
    """Punto de entrada principal del proyecto."""
    logger = get_logger()
    logger.info(f"Proyecto inicializado desde: {ROOT_DIR}")
