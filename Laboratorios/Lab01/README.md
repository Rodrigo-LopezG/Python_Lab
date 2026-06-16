# Laboratorio 01: Entorno y Herramientas

## Objetivo del Laboratorio

1) Crear proyecto con Poetry, activar venv, instalar black/isort/ruff
2) Configurar pre-commit; corregir infracciones PEP 8 iniciales

## Estructura del Proyecto

Lab01/
├── pyproject.toml          # Configuración de Poetry y herramientas
├── .pre-commit-config.yaml # Configuración de hooks pre-commit
├── README.md              # Este archivo
└── src/
    ├── __init__.py        # Inicialización del paquete
    ├── ejemplo_con_errores.py    # Código con infracciones PEP 8
    └── ejemplo_corregido.py      # Código corregido siguiendo PEP 8


### 1. Instalación de Poetry

Instalación recomendada (instalador oficial)
Windows (PowerShell):

(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

Tras la instalación, añade Poetry a tu PATH. El instalador imprime la ruta exacta — normalmente $HOME/.local/bin en Linux/macOS o %APPDATA%\Python\Scripts en Windows.

Verifica la instalación:
poetry --versión

Poetry (version 2.4.1)


### 2. Configuración del Entorno Virtual

# Navegar al directorio del proyecto
cd Lab01

# Crear y activar entorno virtual
poetry install

# Activar el entorno virtual
poetry shell

### 3. Instalación de Dependencias

`pyproject.toml`:

# Instalar dependencias de desarrollo
poetry install --with dev

### 4. Configuración de Pre-commit Hooks

# Instalar hooks pre-commit
poetry run pre-commit install

# Ejecutar hooks en todos los archivos
poetry run pre-commit run --all-files

### 5. Corrección de Infracciones PEP 8

# black (Fromateo)
poetry run black src/ejemplo_con_errores.py

# isort (Organizar imports)
poetry run isort src/ejemplo_con_errores.py

# ruff (Analisis)
poetry run ruff check src/ejemplo_con_errores.py

# Corregir automáticamente con ruff
poetry run ruff check --fix src/ejemplo_con_errores.py


## Verificación Final

1. **Ejecutar todos los hooks**:

   poetry run pre-commit run --all-files

2. **Verificar que no hay errores de linting**:

   poetry run ruff check src/

3. **Confirmar que el código está formateado**:

   poetry run black --check src/

4. **Probar que los imports están ordenados**:

   poetry run isort --check-only src/

	
