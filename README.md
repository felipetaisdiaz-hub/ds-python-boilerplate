# 🧬 Data Science Python Boilerplate (`ds-python-boilerplate`)

Plantilla base (**boilerplate**) genérica, agnóstica y lista para producción para proyectos de **Data Science y Machine Learning** en Python.

Diseñada con **aislamiento total de entorno mediante [`uv`](https://docs.astral.sh/uv/)**, arquitectura **`src-layout`**, calidad de código automatizada (**Ruff + Mypy + Pre-commit**) e **Integración Continua (GitHub Actions + SonarCloud)**.

---

## 📁 Estructura del Proyecto

```text
ds-python-boilerplate/
├── .github/workflows/
│   └── pr_validation.yml        # CI/CD: Ruff, Mypy, Pytest (cobertura) y SonarCloud
├── config/
│   └── config.yaml              # Parámetros e hiperparámetros del proyecto
├── data/
│   ├── external/                # Datos de fuentes externas de terceros
│   ├── interim/                 # Datos intermedios en transformación
│   ├── processed/               # Datasets limpios listos para modelado
│   └── raw/                     # Datos originales inmutables (nunca se modifican)
├── docs/                        # Documentación técnica y diccionarios de datos
├── models/                      # Modelos entrenados serializados (ignorados en Git)
├── notebooks/                   # Jupyter Notebooks para exploración y prototipado
├── scripts/
│   └── init_project.py          # Script para renombrar la plantilla en proyectos nuevos
├── src/
│   └── ds_python_boilerplate/   # Código fuente empaquetable y modular
│       ├── __init__.py          # Punto de entrada principal
│       ├── logger.py            # Configuración centralizada de logging
│       └── paths.py             # Rutas absolutas del proyecto (independientes del cwd)
├── tests/                       # Pruebas unitarias con pytest
│   └── test_core.py
├── .env.example                 # Plantilla de variables de entorno
├── .gitignore                   # Reglas de exclusión para Python, DS/ML y secretos
├── .pre-commit-config.yaml      # Hooks locales (Ruff, nbstripout, secretos)
├── .python-version              # Versión de Python fijada para uv (3.13)
├── Makefile                     # Atajos para tareas frecuentes
├── pyproject.toml               # Configuración unificada (dependencias, pytest, ruff, mypy)
└── sonar-project.properties     # Configuración de análisis estático para SonarCloud
```

---

## 🚀 Cómo iniciar un nuevo proyecto desde esta plantilla

1. **Crea tu nuevo repositorio** en GitHub usando este repositorio como *Template* (o clónalo).
2. **Renombra automáticamente el paquete y configuraciones** ejecutando:
   ```bash
   uv run python scripts/init_project.py nombre-de-tu-proyecto
   ```
3. **Sincroniza el entorno virtual aislado (`.venv`)**:
   ```bash
   # Solo desarrollo (pytest, ruff, mypy, pre-commit)
   uv sync --dev

   # O incluyendo soporte para Jupyter Notebooks (ipykernel, nbstripout)
   uv sync --all-groups
   ```
4. **Activa los hooks de `pre-commit`** (limpia automáticamente salidas de notebooks y formatea código antes de cada commit):
   ```bash
   uv run pre-commit install
   ```

---

## 🛠️ Comandos de Desarrollo y Calidad de Código

Puedes ejecutar las herramientas directamente con `uv run` o mediante el `Makefile`:

| Tarea | Comando con `uv` | Atajo `Makefile` |
| :--- | :--- | :--- |
| **Instalar dependencias (dev)** | `uv sync --dev` | `make install` |
| **Instalar todo (incl. notebooks)** | `uv sync --all-groups` | `make install-all` |
| **Añadir librería de producción** | `uv add pandas scikit-learn` | — |
| **Ejecutar Linter (Ruff)** | `uv run ruff check .` | `make lint` |
| **Formatear código (Ruff)** | `uv run ruff format .` | `make format` |
| **Verificar tipos (Mypy)** | `uv run mypy src/` | `make typecheck` |
| **Ejecutar Tests + Cobertura** | `uv run pytest --cov=src` | `make test` |
| **Validación completa pre-PR** | `uv run ruff check . && uv run mypy src/ && uv run pytest` | `make check` |

---

## 🔍 Integración Continua (CI/CD) y SonarCloud

El flujo [`.github/workflows/pr_validation.yml`](.github/workflows/pr_validation.yml) se ejecuta en cada `push` y `pull_request` hacia `main`:
1. **`test` Job**: Instala `uv` y Python según `.python-version`, verifica formato y linting con **Ruff**, comprueba tipado estático con **Mypy** y ejecuta **Pytest** generando `coverage.xml` y `test-results.xml`.
2. **`sonar` Job**: Descarga los reportes de cobertura y envía el análisis a **SonarCloud** (requiere configurar el secreto `SONAR_TOKEN` en el repositorio de GitHub).
