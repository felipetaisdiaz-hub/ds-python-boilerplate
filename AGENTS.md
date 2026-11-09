# 🧠 Memoria y Reglas del Proyecto (`AGENTS.md`)

Este documento define las reglas obligatorias de arquitectura, herramientas y flujo de trabajo para cualquier agente de IA que opere en este repositorio (`ds-python-boilerplate`). **Léelo y cúmplelo antes de ejecutar comandos o modificar archivos.**

---

## 1. Idioma y Comunicación
- **Idioma por defecto:** Responde siempre al usuario en **español**.
- **Documentación y comentarios:** Escribe los *docstrings*, comentarios en el código y el `README.md` en español (salvo nombres de variables/funciones que pueden seguir convenciones estándar en inglés o español consistente con el módulo).
- **Control de versiones:** No ejecutes `git commit` ni `git push` sin confirmación explícita del usuario.

---

## 2. Gestión de Entorno y Dependencias (`uv` estricto)
- **Gestor único:** Este proyecto usa exclusivamente **[`uv`](https://docs.astral.sh/uv/)** con entorno virtual local en `.venv/`.
- **Prohibido `pip` / `conda` / `poetry`:**
  - ❌ **NUNCA** ejecutes `pip install`, `python -m pip` ni modifiques paquetes globales.
  - ✅ Para añadir dependencias de producción: `uv add <paquete>`
  - ✅ Para añadir dependencias de desarrollo: `uv add --group dev <paquete>`
  - ✅ Para añadir dependencias de notebooks: `uv add --group notebooks <paquete>`
  - ✅ Para sincronizar el entorno: `uv sync --dev` (o `uv sync --all-groups`)
  - ✅ Para ejecutar cualquier comando o script: `uv run <comando>` (ej. `uv run pytest`, `uv run python ...`).

---

## 3. Arquitectura de Carpetas y Rutas (Data Science Standard)
Respeta estrictamente la separación de responsabilidades del proyecto:
- **`src/ds_python_boilerplate/`**: Único lugar para el código Python modular, reutilizable y de producción (`.py`).
  - **Rutas:** ❌ **NUNCA** uses rutas relativas frágiles (`"../data/..."`). ✅ Importa siempre las constantes desde [`src/ds_python_boilerplate/paths.py`](src/ds_python_boilerplate/paths.py) (`ROOT_DIR`, `RAW_DATA_DIR`, `INTERIM_DATA_DIR`, `PROCESSED_DATA_DIR`, `EXTERNAL_DATA_DIR`, `MODELS_DIR`, `CONFIG_DIR`).
  - **Logging:** ❌ Evita `print()` en el código de `src/`. ✅ Usa `get_logger()` desde [`src/ds_python_boilerplate/logger.py`](src/ds_python_boilerplate/logger.py).
- **`data/`**: Exclusivamente para datasets (ignorados en Git salvo `.gitkeep`).
  - `data/raw/`: Datos originales **inmutables**. **NUNCA** modifiques ni sobrescribas archivos en `data/raw/`.
  - `data/interim/`: Datos intermedios en transformación.
  - `data/processed/`: Datasets limpios y con *features* finales listos para modelado.
  - `data/external/`: Datos de fuentes externas de terceros.
- **`notebooks/`**: Exclusivamente para Jupyter Notebooks (`.ipynb`) de exploración (EDA), visualización y prototipado (nombrados con prefijo numérico, ej. `01_eda.ipynb`). En cuanto una función o transformación sea estable, refactorízala dentro de `src/ds_python_boilerplate/`.
- **`models/`**: Artefactos de modelos entrenados serializados (`.pkl`, `.joblib`, `.pt`, `.onnx`).
- **`config/`**: Archivos `.yaml`/`.toml` con hiperparámetros y configuración de negocio ([`config/config.yaml`](config/config.yaml)). Evita valores mágicos (*hardcodeados*) en el código.
- **`tests/`**: Pruebas unitarias con `pytest`. Todo módulo nuevo en `src/` debe tener su correspondiente test en `tests/`.

---

## 4. Estándares de Calidad de Código (Pre-vuelo obligatorio)
Antes de dar por finalizada cualquier modificación de código en `src/` o `tests/`, verifica que pasen las 3 barreras de calidad que exige el pipeline de CI/CD y SonarCloud:

1. **Linter y Formato (`Ruff`):**
   ```bash
   uv run ruff check --fix .
   uv run ruff format .
   ```
   *(Límite de línea: 100 caracteres, reglas `E, W, F, I, B, UP, SIM`).*

2. **Tipado Estático (`Mypy`):**
   ```bash
   uv run mypy src/
   ```
   *(Todas las funciones en `src/` deben incluir anotaciones de tipos en argumentos y retorno: `disallow_untyped_defs = true`).*

3. **Tests Unitarios y Cobertura (`Pytest`):**
   ```bash
   uv run pytest tests/ --cov=src --cov-report=term-missing
   ```
   *(Asegura que los tests pasen y mantengan alta cobertura para no bloquear el Quality Gate de SonarCloud).*
