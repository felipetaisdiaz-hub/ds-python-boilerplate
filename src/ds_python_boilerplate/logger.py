"""Configuración estandarizada de logging para scripts y pipelines."""

import logging
import sys


def get_logger(name: str = "ds_python_boilerplate", level: int = logging.INFO) -> logging.Logger:
    """Crea o recupera un logger configurado con salida estándar."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger
