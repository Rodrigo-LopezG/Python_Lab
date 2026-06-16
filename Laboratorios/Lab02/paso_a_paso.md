# Guía Paso a Paso para el Laboratorio de Python Lab02

### PASO 1: Configuración del Entorno

### 1.1 Verificar instalación de Python

python --version

### 1.2 Crear carpeta de trabajo

mkdir laboratorio_python
cd laboratorio_python


### 1.3 Descargar los archivos del laboratorio
Asegúrate de tener todos los archivos:
- `Sistema ventas`
- `ventas.json`
- `README.md`
- `guia_paso_a_paso.md`

### PASO 2: Entender la Estructura de los Archivos

### 2.1 Analizar el archivo JSON de ventas
Abre `ventas.json` y observa:
- Estructura similar al anterior
- Cada venta tiene: id, producto, categoria, cantidad, precio, fecha

###  PASO 3: Practicar con el ejemplo Sistema_ventas

### 3.1 Entender las diferencias
El Sistema_ventas introduce conceptos adicionales:
- **Expresiones regulares** para validación de fechas
- **Agregaciones más complejas**
- **Generación de reportes en JSON**
- **Filtrado por categorías**

### 3.2 Ejecutar el Sistema_ventas

### Análisis general
python ejemplo2_ventas.py ventas.json

### Filtrar por categoría
python ejemplo2_ventas.py ventas.json Electrónicos

### 3.3 Analizar la salida
Observa cómo se genera un reporte JSON adicional con los resultados.

### PASO 4: Análisis del Código

Dibuja un diagrama de flujo del programa:
1. Inicio Leer argumentos
2. Validar archivo Leer JSON
3. Procesar datos Filtrar
4. Calcular estadísticas Mostrar resultados
5. Fin

---
