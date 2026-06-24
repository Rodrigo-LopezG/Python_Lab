# Laboratorio 05: Tipado estático y Calidad de Código

## 🎯 Objetivos


## Estructura del laboratorio

```
Lab_05/
├── src/
│   ├── __init__.py
│   ├── models.py          # Modelos de datos con TypedDict
│   ├── services.py        # Lógica de negocio con Protocol
│   └── utils.py           # Utilidades con Union y Literal
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_services.py
│   └── test_utils.py
├── .pre-commit-config.yaml
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Comandos Útiles

```bash
# Instalar dependencias
pip install -r requirements-dev.txt

# Instalar pre-commit hooks
pre-commit install

# Ejecutar verificación de tipos
mypy src/

# Formatear código
black src/ tests/
ruff check src/ tests/
isort src/ tests/

# Ejecutar todos los checks
pre-commit run --all-files
```

## Conceptos Clave

### Type Hints Básicos
```python
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"
```

### Union Types
```python
from typing import Union

def procesar_id(id: Union[int, str]) -> str:
    return str(id)
```

### Literal Types
```python
from typing import Literal

def set_estado(estado: Literal["activo", "inactivo", "pendiente"]) -> None:
    pass
```

### TypedDict
```python
from typing import TypedDict

class Usuario(TypedDict):
    id: int
    nombre: str
    email: str
```

### Protocol
```python
from typing import Protocol

class Procesable(Protocol):
    def procesar(self) -> str: ...
```
