# Laboratorio 02: Fundamentos de lenguaje

## Objetivo del laboratorio

- Manejar estructuras de datos y control de flujo
- Implementar manejo de errores robusto
- Usar pattern matching en casos adecuados y expresiones regulares

## Archivos del Laboratorio

### Sistema de Ventas
- **Archivo**: `Sistema_ventas.py`
- **Datos**: `ventas.json`
- **Funcionalidad**: Analiza datos de ventas, filtra por categorías y genera reportes

## Laboratorio 02

### 1. Estructura del Código

Los ejemplos siguen la misma estructura:

1. **Lectura de JSON**: Función que lee archivos JSON con manejo de errores
2. **Procesamiento**: Funciones que filtran y transforman datos
3. **Análisis**: Funciones que calculan estadísticas y agregados
4. **Salida**: Muestra resultados y opcionalmente guarda archivos

#### Sistema_ventas:
```bash
# Análisis general
python Sistema_ventas.py ventas.json

# Filtrar por categoría específica
python Sistema_ventas.py ventas.json Electrónicos
```

## Conceptos Clave Explicados

### 1. Manejo de Excepciones


try:
    # Código que puede fallar
    with open(archivo, 'r') as f:
        datos = json.load(f)
except FileNotFoundError:
    print("El archivo no existe")
except json.JSONDecodeError:
    print("Formato JSON inválido")
except Exception as e:
    print(f"Error inesperado: {e}")


### 2. Estructuras de Control


# Condicional
if calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")

# Bucle for
for estudiante in estudiantes:
    print(estudiante['nombre'])

# List comprehension
aprobados = [e for e in estudiantes if e['calificacion'] >= 70]


### 3. Tipos de Datos y Colecciones


# Lista (mutable, ordenada)
numeros = [1, 2, 3, 4, 5]

# Diccionario (clave-valor)
persona = {"nombre": "Luis", "edad": 22}

# Tupla (inmutable, ordenada)
coordenadas = (10, 20)

# Set (único, desordenado)
categorias = {"Muebles", "Libros", "Electrónicos"}


### 4. Expresiones Regulares


import re

# Validar formato de fecha
patron = r'^\d{4}-\d{2}-\d{2}$'
if re.match(patron, fecha_str):
    print("Fecha válida")


## Errores Comunes y Soluciones

### 1. IndentationError
**Problema**: Espacios inconsistentes
**Solución**: Usar siempre 4 espacios o configurar tu editor

### 2. KeyError
**Problema**: Acceder a clave que no existe
**Solución**: Usar `.get()` con valor por defecto

# Incorrecto
nombre = estudiante['nombre']  # Puede fallar

# Correcto
nombre = estudiante.get('nombre', 'Desconocido')


### 3. TypeError
**Problema**: Operación con tipos incompatibles
**Solución**: Validar tipos antes de operar

if isinstance(edad, int) and edad > 0:
    # Procesar edad

