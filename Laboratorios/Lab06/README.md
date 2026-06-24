# Laboratorio 06: Librería Estándar y E/S

## Descripción del Laboratorio

Manejo de herramientas fundamentales de Python para el procesamiento de datos y la automatización de tareas.

## Estructura de Archivos

```
Windsurf/
├── datos_ejemplo.csv          # Archivo de datos para practicar
├── ejemplo1_basico.py         # Ejemplo 1: Lectura básica de CSV
├── ejemplo2_metricas_json.py  # Ejemplo 2: Métricas y exportación JSON
├── ejemplo3_logging_completo.py # Ejemplo 3: Logging completo
├── README.md                  # Este archivo
├── logs/                      # Directorio para logs (se crea automáticamente)
│   └── laboratorio.log        # Archivo de logs generado
├── resultados.json            # Resultados del ejemplo 2
├── resultados_completos.json  # Resultados del ejemplo 3
└── resumen_procesamiento.txt  # Resumen en texto del ejemplo 3
```

## Cómo Ejecutar los Ejemplos

### Requisitos Previos
- Python 3.6 o superior instalado
- No se necesitan librerías externas (solo librería estándar)

### Ejecutar Ejemplo 1: Lectura Básica
```bash
python ejemplo1_basico.py
```
**¿Qué hace?** Lee el archivo CSV y muestra los datos en pantalla.

### Ejecutar Ejemplo 2: Métricas y JSON
```bash
python ejemplo2_metricas_json.py
```
**¿Qué hace?** Calcula estadísticas y exporta los resultados a un archivo JSON.

### Ejecutar Ejemplo 3: Logging Completo
```bash
python ejemplo3_logging_completo.py
```
**¿Qué hace?** Incluye logging profesional, validación de datos y usa subprocess.

## Explicación Detallada

### Ejemplo 1: Conceptos Básicos
- **pathlib.Path**: Maneja rutas de archivos de forma multiplataforma
- **csv.reader**: Lee archivos CSV fila por fila
- **with open():** Asegura que los archivos se cierren correctamente

### Ejemplo 2: Procesamiento de Datos
- **csv.DictReader**: Convierte cada fila en un diccionario
- **json.dump()**: Exporta datos a formato JSON
- **datetime.now()**: Obtiene la fecha y hora actual

### Ejemplo 3: Logging y Automatización
- **logging.basicConfig()**: Configura el sistema de logs
- **subprocess.run()**: Ejecuta comandos del sistema operativo
- **Múltiples niveles de log**: DEBUG, INFO, WARNING, ERROR, CRITICAL

## Niveles de Logging Explicados

| Nivel | Cuándo usarlo | Ejemplo |
|-------|---------------|---------|
| **DEBUG** | Información detallada para depuración | "Procesando fila 5" |
| **INFO** | Información general del proceso | "Archivo leído correctamente" |
| **WARNING** | Algo inesperado pero no crítico | "Edad fuera de rango" |
| **ERROR** | Error que no detiene el programa | "No se pudo convertir número" |
| **CRITICAL** | Error grave que detiene todo | "No se encuentra el archivo" |

## Datos de Ejemplo

El archivo `datos_ejemplo.csv` contiene información de empleados:
- ID único
- Nombre completo
- Edad (18-65 años)
- Salario en dólares
- Departamento
- Fecha de ingreso

## Ejercicios Propuestos

1. **Modifica el Ejemplo 1** para que filtre empleados por departamento
2. **Amplía el Ejemplo 2** para que calcule el salario mediano
3. **Mejora el Ejemplo 3** para que envíe un email con los resultados
4. **Crea un nuevo script** que lea el JSON generado y cree un reporte en HTML

## Tips para Principiantes

1. **Siempre usa `pathlib`** en lugar de cadenas para rutas
2. **Usa `with open()`** siempre que trabajes con archivos
3. **Configura logging desde el principio** en tus proyectos
4. **Valida los datos** antes de procesarlos
5. **Maneja excepciones** con try/except

## Solución de Problemas Comunes

### "FileNotFoundError"
- Verifica que el archivo `datos_ejemplo.csv` esté en la misma carpeta
- Usa rutas absolutas si es necesario

### "UnicodeDecodeError"
- Asegúrate de usar `encoding='utf-8'` al abrir archivos

### "Permission denied"
- Cierra el archivo antes de volver a abrirlo
- Verifica permisos de escritura en la carpeta

## Referencias Útiles

- [Documentación oficial de pathlib](https://docs.python.org/3/library/pathlib.html)
- [Tutorial de CSV en Python](https://docs.python.org/3/library/csv.html)
- [Guía de logging](https://docs.python.org/3/howto/logging.html)

---
