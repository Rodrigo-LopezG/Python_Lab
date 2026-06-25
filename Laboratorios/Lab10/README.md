#  Laboratorio de Pruebas y TDD en Python

## Objetivos de Aprendizaje

- Practicar TDD y diseñar pruebas confiables
- Asegurar cobertura suficiente y suite estable
- Aprender a simular dependencias externas
- Generar casos de prueba automáticamente

##  Guía Paso a Paso para Principiantes

### Paso 1: Configuración del Entorno

Si no tienes conocimientos en Python, sigue estos pasos:

1. **Instala Python** (si no lo tienes):
   ```bash
   # Descarga desde https://python.org (versión 3.8 o superior)
   # O usa tu gestor de paquetes preferido
   ```

2. **Instala las dependencias del proyecto**:
   ```bash
   pip install -r requirements.txt
   ```

### Paso 2: Entiende la Estructura del Proyecto

```
Windsurf/
├── src/                    # Código fuente
│   ├── calculadora.py      # Ejemplo 1: Calculadora simple
│   ├── models.py           # Modelos de datos
│   ├── usuario_service.py  # Ejemplo 2: Servicio de usuarios
│   └── validador.py        # Ejemplo 3: Validador de datos
├── tests/                  # Tests
│   ├── test_calculadora.py     # Tests para calculadora
│   ├── test_usuario_service.py # Tests con mocking
│   └── test_validador.py       # Tests con Hypothesis
├── requirements.txt        # Dependencias
├── pytest.ini            # Configuración de pytest
└── run_tests.py          # Script para ejecutar todos los tests
```

### Paso 3: Ejecuta los Tests

```bash
# Opción 1: Ejecutar todos los tests
python run_tests.py

# Opción 2: Ejecutar con pytest directamente
pytest tests/ -v

# Opción 3: Ejecutar con cobertura
pytest tests/ --cov=src --cov-report=html
```

##  Ejemplos Detallados

### Ejemplo 1: Calculadora Simple con TDD 

**Concepto**: TDD (Test-Driven Development) - Escribir tests ANTES del código.

**¿Cómo funciona?**
1. **Escribes un test que falla** (Rojo)
2. **Escribes el código mínimo para que pase** (Verde)  
3. **Refactorizas el código** (Refactorización)

**Archivos**:
- `src/calculadora.py` - La implementación
- `tests/test_calculadora.py` - Los tests

**Ejemplo práctico**:
```python
# 1. Primero escribes el test (esto fallará)
def test_sumar_numeros_positivos(self):
    calc = Calculadora()
    resultado = calc.sumar(2, 3)
    assert resultado == 5

# 2. Luego implementas el método para que pase
def sumar(self, a, b):
    return a + b  # Código mínimo para pasar el test
```

**Conceptos aprendidos**:
- **Fixtures**: Métodos que preparan el entorno (`setup_method`)
- **Parametrización**: Múltiples casos en un solo test (`@pytest.mark.parametrize`)
- **Markers**: Etiquetas para categorizar tests (`@pytest.mark.slow`)

### Ejemplo 2: Sistema de Usuarios con Mocking 


# El test usa el mock en lugar de una DB real
service = UsuarioService(mock_db)
usuario = service.crear_usuario("juan", "juan@email.com")
```

**Conceptos aprendidos**:
- **Mock**: Objeto que simula comportamiento
- **Patch**: Reemplaza temporalmente funciones/módulos
- **Assert**: Verifica que se llamaron los métodos correctos

### Ejemplo 3: Validador con Property-Based Testing 

**Concepto**: Property-based testing - Generar casos de prueba automáticamente.

**¿Qué es Hypothesis?**
- Framework que genera datos de prueba automáticamente
- Verifica propiedades matemáticas de tu código
- Encuentra casos límite que no pensarías

**Archivos**:
- `src/validador.py` - Funciones de validación
- `tests/test_validador.py` - Tests con Hypothesis

**Ejemplo práctico**:
```python
@given(st.integers(min_value=0, max_value=100))
def test_edad_valida_rango(self, edad):
    # Hypothesis genera 100 números aleatorios entre 0 y 100
    assert self.validador.es_edad_valida(edad)
```

**Conceptos aprendidos**:
- **Strategies**: Generadores de datos (`st.integers`, `st.text`, `st.emails`)
- **Properties**: Propiedades matemáticas que deben cumplirse
- **Falsification**: Encontrar casos que rompen las reglas

## Comandos Útiles

### Ejecutar Tests Específicos

```bash
# Ejecutar un archivo específico
pytest tests/test_calculadora.py -v

# Ejecutar una clase específica
pytest tests/test_calculadora.py::TestCalculadora -v

# Ejecutar un test específico
pytest tests/test_calculadora.py::TestCalculadora::test_sumar_numeros_positivos -v
```

### Ejecutar por Categorías

```bash
# Solo tests unitarios
pytest -m unit -v

# Solo tests de integración
pytest -m integration -v

# Excluir tests lentos
pytest -m "not slow" -v
```

### Cobertura de Código

```bash
# Generar reporte en terminal
pytest --cov=src --cov-report=term-missing

# Generar reporte HTML
pytest --cov=src --cov-report=html

# Ver reporte HTML (se abre en htmlcov/index.html)
```

## Métricas de Calidad

### Cobertura de Código
- **Mínimo requerido**: 80%
- **Ideal**: 90%+
- **Reporte**: Se genera en `htmlcov/index.html`


### Tipos de Tests
- **Unit Tests**: Prueban componentes individuales
- **Integration Tests**: Prueban interacción entre componentes
- **Property Tests**: Verifican propiedades matemáticas

## Configuración Avanzada

### pytest.ini
El archivo `pytest.ini` contiene:
- Rutas de búsqueda de tests
- Configuración de cobertura
- Markers personalizados
- Opciones de ejecución

### CI/CD Integration
El workflow `.github/workflows/ci.yml` configura:
- Ejecución automática en GitHub Actions
- Tests en múltiples versiones de Python
- Reportes de cobertura automatizados

## Tareas del Laboratorio

### Tarea 1: Implementar una Nueva Historia con TDD

1. **Define el requisito**: Ejemplo: "Crear una función que calcule el factorial"
2. **Escribe el test primero**:
   ```python
   def test_factorial_de_cinco(self):
       resultado = self.calc.factorial(5)
       assert resultado == 120
   ```
3. **Haz que falle** (ejecuta el test)
4. **Implementa el código mínimo**:
   ```python
   def factorial(self, n):
       if n <= 1:
           return 1
       return n * self.factorial(n - 1)
   ```
5. **Haz que pase** (ejecuta el test)
6. **Refactoriza** (mejora el código)

### Tarea 2: Añadir Tests de Propiedades

1. **Identifica propiedades matemáticas** de tu código
2. **Escribe tests con Hypothesis**:
   ```python
   @given(st.integers(min_value=0))
   def test_factorial_propiedad_creciente(self, n):
       # factorial(n) >= n para n >= 1
       if n >= 1:
           assert self.calc.factorial(n) >= n
   ```
3. **Ejecuta y corrige** los casos que encuentre Hypothesis

### Tarea 3: Generar Reporte de Cobertura

1. **Ejecuta los tests con cobertura**:
   ```bash
   pytest --cov=src --cov-report=html
   ```
2. **Revisa el reporte** en `htmlcov/index.html`
3. **Asegura 80%+ de cobertura**
4. **Identifica código no cubierto** y añade tests

## Errores Comunes y Soluciones

### Error: "ModuleNotFoundError"
**Causa**: Python no encuentra el módulo
**Solución**: Asegúrate de estar en el directorio correcto y ejecutar:
```bash
pip install -r requirements.txt
```

### Error: "Tests fallan"
**Causa**: Los tests esperan comportamiento específico
**Solución**: Revisa los mensajes de error y ajusta el código

### Error: "Cobertura baja"
**Causa**: Hay código sin probar
**Solución**: Añade tests para las ramas no cubiertas

## Recursos Adicionales

### Documentación Oficial
- [pytest Documentation](https://docs.pytest.org/)
- [Hypothesis Documentation](https://hypothesis.works/)
- [unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html)

### Tutoriales Recomendados
- [pytest by Example](https://realpython.com/pytest-python-testing/)
- [Hypothesis for Python](https://hypothesis.works/articles/getting-started-with-hypothesis-and-pytest/)

