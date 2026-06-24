# GUÍA COMPLETA DEL LABORATORIO FASTAPI

##  Índice
1. [Introducción](#introducción)
2. [Conceptos Fundamentales](#conceptos-fundamentales)
3. [Paso a Paso del Laboratorio](#paso-a-paso-del-laboratorio)
4. [Ejemplos Prácticos](#ejemplos-prácticos)
5. [Testing y Validación](#testing-y-validación)
6. [Preguntas Frecuentes](#preguntas-frecuentes)

---

## Introducción

Bienvenido al laboratorio de FastAPI. Este proyecto te enseñará a crear una API REST completa utilizando Python y FastAPI, implementando:

- ✅ **CRUD** de Orders (Crear, Leer, Actualizar, Eliminar)
- ✅ **Autenticación JWT** para seguridad
- ✅ **Validación de datos** con Pydantic
- ✅ **Testing automatizado** con pytest
- ✅ **Documentación automática** con OpenAPI

---

##  Conceptos Fundamentales

### 1. ¿Qué es FastAPI?
FastAPI es un framework web moderno y rápido para construir APIs con Python. Es:
- **Rápido**: Alto rendimiento, comparable con NodeJS y Go
- **Rápido de programar**: Incrementa la velocidad de desarrollo 2-3x
- **Menos errores**: Reduce errores humanos y de depuración
- **Intuitivo**: Excelente soporte de editores y autocompletado
- **Fácil**: Diseñado para ser fácil de usar y aprender

### 2. ¿Qué es JWT (JSON Web Token)?
JWT es un estándar abierto para crear tokens de acceso seguros:
- **Sin estado**: No requiere almacenamiento en servidor
- **Seguro**: Firmado digitalmente
- **Compacto**: Pequeño y fácil de transmitir
- **Autocontenido**: Contiene toda la información necesaria

### 3. ¿Qué es Pydantic?
Pydantic es una librería para validación de datos:
- **Validación automática**: Verifica tipos y formatos
- **Serialización**: Convierte datos a/desde Python
- **Documentación**: Genera esquemas automáticamente

### 4. ¿Qué es pytest?
pytest es un framework de testing para Python:
- **Simple**: Fácil de escribir y entender
- **Potente**: Funciones avanzadas de testing
- **Extensible**: Plugin system
- **Popular**: Ampliamente usado en la industria

---

##  Paso a Paso del Laboratorio

### Paso 1: Configuración del Entorno

```bash
# 1. Clonar o descargar el proyecto
# 2. Navegar a la carpeta del proyecto
cd Windsurf

# 3. Ejecutar el script de configuración
python setup.py
```

El script `setup.py` verificará:
-  Versión de Python (requiere 3.7+)
-  Instalación de dependencias
-  Configuración inicial

### Paso 2: Entender la Estructura del Proyecto
def test_create_order_invalid_data():
    invalid_order = {
        "customer_name": "Test",
        "quantity": -1,  # Inválido
        "price": 10.00
    }
    response = requests.post("/orders/", json=invalid_order)
    assert response.status_code == 422  # Unprocessable Entity
```

#### 3. Pruebas de Seguridad
```python
def test_unauthorized_access():
    response = requests.get("/orders/")
    assert response.status_code == 403  # Forbidden
```

### Ejecutar Todas las Pruebas

```bash
# Con pytest (recomendado)
pytest test_orders.py -v

# Pruebas específicas
pytest test_orders.py::TestAuthentication -v

# Con coverage
pytest test_orders.py --cov=. --cov-report=html
```

---

##  Preguntas Frecuentes

### 1. ¿Por qué usar SQLite?
SQLite es ideal para desarrollo y testing porque:
-  No requiere configuración
-  Base de datos en un solo archivo
-  Rápido y ligero
-  Compatible con SQL estándar

### 2. ¿Es seguro usar una clave secreta fija?
**No**, para producción debes:
- Usar variables de entorno
- Rotar claves regularmente
- Usar claves largas y aleatorias
- No incluir claves en el código

### 3. ¿Cómo manejar concurrencia?
FastAPI maneja concurrencia automáticamente:
- Usa `async/await` para operaciones asíncronas
- Cada petición se procesa en paralelo
- SQLite tiene bloqueos a nivel de archivo

### 4. ¿Cómo escalar esta aplicación?
Para producción considera:
- Usar PostgreSQL o MySQL
- Implementar Redis para caché
- Usar Docker para contenerización
- Configurar balanceador de carga

### 5. ¿Cómo agregar más endpoints?
Sigue el patrón establecido:
```python
@app.post("/nuevo-endpoint/")
async def nuevo_endpoint(data: Modelo, user: str = Depends(verify_token)):
    # Tu lógica aquí
    return {"message": "Éxito"}
```

---

## 🎯 Objetivos de Aprendizaje

Al completar este laboratorio, habrás aprendido:

###  Conceptos Técnicos
- **FastAPI**: Creación de APIs REST
- **Pydantic**: Validación de datos
- **JWT**: Autenticación sin estado
- **SQLite**: Base de datos ligera
- **pytest**: Testing automatizado

###  Habilidades Prácticas
- **CRUD**: Operaciones básicas de base de datos
- **Autenticación**: Seguridad en APIs
- **Validación**: Manejo de datos de entrada
- **Testing**: Aseguramiento de calidad
- **Documentación**: API auto-documentada

###  Mejores Prácticas
- **Código limpio**: Estructura organizada
- **Manejo de errores**: Respuestas adecuadas
- **Seguridad**: Protección de endpoints
- **Testing**: Cobertura completa
- **Documentación**: Código autoexplicativo

---

##  Siguientes Pasos

### Para Principiantes
1. **Reproducir los ejemplos**: Ejecuta todos los ejemplos paso a paso
2. **Modificar el código**: Cambia valores y observa resultados
3. **Crear nuevos endpoints**: Agrega funcionalidades adicionales
4. **Escribir pruebas**: Crea pruebas para nuevos endpoints

### Para Intermedios
1. **Mejorar la seguridad**: Implementa refresh tokens
2. **Agregar más validaciones**: Usa validadores personalizados
3. **Implementar logging**: Registra todas las operaciones
4. **Optimizar consultas**: Mejora el rendimiento de la BD

### Para Avanzados
1. **Microservicios**: Divide la aplicación en servicios
2. **Dockerización**: Conteneriza la aplicación
3. **CI/CD**: Automatiza despliegues
4. **Monitoring**: Agrega métricas y alertas

---
