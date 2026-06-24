#  Instrucciones Paso a Paso para Principiantes

## PASO 1: Entender los Archivos

### Archivo de Datos: `datos_ejemplo.csv`
Este es nuestro archivo de entrada. Contiene:
```
id,nombre,edad,salario,departamento,fecha_ingreso
1,Ana López,28,3500,Ventas,2022-01-15
...
```

**¿Qué significa cada columna?**
- `id`: Número único del empleado
- `nombre`: Nombre completo
- `edad`: Edad en años
- `salario`: Salario mensual en dólares
- `departamento`: Área donde trabaja
- `fecha_ingreso`: Cuándo empezó a trabajar

---

##  PASO 2: Ejecutar el Ejemplo 1 (El más simple)

### ¿Qué hace?
Solo lee el CSV y muestra los datos en pantalla. Perfecto para empezar.

### ¿Cómo ejecutarlo?
1. Abre una terminal o símbolo del sistema
2. Navega a la carpeta Windsurf
3. Escribe: `python ejemplo1_basico.py`

### ¿Qué verás?
```
 Ejemplo 1: Lectura básica de CSV
========================================
 Encabezados: ['id', 'nombre', 'edad', 'salario', 'departamento', 'fecha_ingreso']

 Datos:
  Fila 1: ['1', 'Ana López', '28', '3500', 'Ventas', '2022-01-15']
  Fila 2: ['2', 'Carlos Mendoza', '35', '4200', 'IT', '2021-06-20']
  ...

 Se leyeron 10 registros correctamente
```

### Conceptos que aprendes:
- **pathlib**: Para manejar rutas de archivos
- **csv.reader**: Para leer archivos CSV
- **with open()**: Para abrir archivos de forma segura

---

##  PASO 3: Ejecutar el Ejemplo 2 (Con métricas)

### ¿Qué hace?
Lee el CSV, calcula estadísticas y guarda los resultados en JSON.

### ¿Cómo ejecutarlo?
```bash
python ejemplo2_metricas_json.py
```

### ¿Qué verás?
```
 Ejemplo 2: Cálculo de métricas y exportación JSON

```python
#!/usr/bin/env python3
# Esto indica que es un script de Python 3

"""
Comentario de varias líneas
Explica qué hace el programa
"""

# Importar librerías que necesitamos
import csv
from pathlib import Path

# Definir funciones
def mi_funcion():
    print("Hola mundo")

# Código principal
if __name__ == "__main__":
    mi_funcion()
```

### Conceptos clave explicados:

#### 1. Importaciones
```python
import csv          # Para leer archivos CSV
import json         # Para trabajar con JSON
from pathlib import Path  # Para manejar rutas
import logging      # Para registrar eventos
import subprocess   # Para ejecutar comandos
```

#### 2. Manejo de archivos
```python
# Forma segura de abrir archivos
with open('archivo.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
# El archivo se cierra automáticamente
```

#### 3. Manejo de errores
```python
try:
    # Código que puede fallar
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as e:
    print(f"Ocurrió un error: {e}")
```

---

##  PASO 6: Modificar y Experimentar

### Ejercicio 1: Filtrar por departamento
Modifica el ejemplo 1 para que solo muestre empleados del departamento "IT":

```python
# Dentro del ciclo de lectura
if 'IT' in fila:
    print(f"Fila {contador}: {fila}")
```

### Ejercicio 2: Calcular mínimo y máximo
Modifica el ejemplo 2 para que encuentre el salario más bajo y más alto:

```python
# Después de leer todos los empleados
salarios = [emp['salario'] for emp in empleados]
salario_minimo = min(salarios)
salario_maximo = max(salarios)
```

### Ejercicio 3: Agregar más logs
Modifica el ejemplo 3 para agregar más mensajes de logging:

```python
logger.info("Iniciando procesamiento de empleados")
logger.debug(f"Procesando empleado {emp['nombre']}")
logger.warning(f"Salario alto detectado: {emp['salario']}")
```

---

##  PASO 7: Verificar Resultados

### Revisa los archivos generados:
1. **resultados.json**: Abre con un editor de texto o navegador
2. **logs/laboratorio.log**: Revisa todos los registros
3. **resumen_procesamiento.txt**: Lee el resumen en texto plano

### Prueba diferentes escenarios:
1. Borra el CSV y ejecuta (debería dar error)
2. Modifica datos incorrectos (edad negativa, salario negativo)
3. Ejecuta varias veces para ver cómo se acumulan los logs

---

##  RESUMEN FINAL

### ¿Qué aprendiste?
1. **Leer archivos CSV** con la librería estándar
2. **Calcular métricas** básicas (promedios, totales)
3. **Exportar a JSON** para compartir datos
4. **Configurar logging** profesional
5. **Manejar errores** de forma robusta
6. **Usar subprocess** para automatización


---

**¡Felicidades!** 🎉 Has completado tu primer laboratorio serio de Python.
