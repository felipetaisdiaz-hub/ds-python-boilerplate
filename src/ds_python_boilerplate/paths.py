"""Módulo centralizado de rutas del proyecto para evitar rutas relativas frágiles."""

from pathlib import Path

# Raíz del repositorio (src/ds_python_boilerplate/paths.py -> parents[2])
ROOT_DIR: Path = Path(__file__).resolve().parents[2]

# Directorios principales
CONFIG_DIR: Path = ROOT_DIR / "config"
DATA_DIR: Path = ROOT_DIR / "data"
RAW_DATA_DIR: Path = DATA_DIR / "raw"
INTERIM_DATA_DIR: Path = DATA_DIR / "interim"
PROCESSED_DATA_DIR: Path = DATA_DIR / "processed"
EXTERNAL_DATA_DIR: Path = DATA_DIR / "external"
MODELS_DIR: Path = ROOT_DIR / "models"
NOTEBOOKS_DIR: Path = ROOT_DIR / "notebooks"
DOCS_DIR: Path = ROOT_DIR / "docs"
