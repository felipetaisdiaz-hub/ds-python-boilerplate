"""Script para renombrar el boilerplate al iniciar un nuevo proyecto de Data Science.

Uso:
    uv run python scripts/init_project.py mi-nuevo-proyecto
"""

import re
import sys
from pathlib import Path

OLD_HYPHEN = "ds-python-boilerplate"
OLD_UNDERSCORE = "ds_python_boilerplate"


def init_project(new_name: str) -> None:
    """Renombra referencias y carpeta del paquete principal al nuevo nombre."""
    clean_hyphen = new_name.strip().lower().replace("_", "-")
    clean_underscore = clean_hyphen.replace("-", "_")

    if not re.match(r"^[a-z][a-z0-9-]*$", clean_hyphen):
        print(f"Error: '{new_name}' no es un nombre de paquete Python válido.")
        sys.exit(1)

    root_dir = Path(__file__).resolve().parents[1]
    files_to_update = [
        root_dir / "AGENTS.md",
        root_dir / "pyproject.toml",
        root_dir / "sonar-project.properties",
        root_dir / "config" / "config.yaml",
        root_dir / "README.md",
        root_dir / "src" / OLD_UNDERSCORE / "__init__.py",
        root_dir / "src" / OLD_UNDERSCORE / "logger.py",
        root_dir / "src" / OLD_UNDERSCORE / "paths.py",
        root_dir / "tests" / "test_core.py",
    ]

    for file_path in files_to_update:
        if file_path.exists():
            content = file_path.read_text(encoding="utf-8")
            updated = content.replace(OLD_HYPHEN, clean_hyphen).replace(
                OLD_UNDERSCORE, clean_underscore
            )
            file_path.write_text(updated, encoding="utf-8")

    old_pkg_dir = root_dir / "src" / OLD_UNDERSCORE
    new_pkg_dir = root_dir / "src" / clean_underscore
    if old_pkg_dir.exists() and old_pkg_dir != new_pkg_dir:
        old_pkg_dir.rename(new_pkg_dir)

    print(f"Proyecto renombrado exitosamente a '{clean_hyphen}' (paquete: '{clean_underscore}').")
    print("Ejecuta 'uv sync --dev' para actualizar el entorno y el lockfile.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: uv run python scripts/init_project.py <nombre-del-proyecto>")
        sys.exit(1)
    init_project(sys.argv[1])
