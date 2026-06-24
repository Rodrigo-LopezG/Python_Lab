# Laboratorio 08: Acceso a datos y ORM

Este proyecto implementa un sistema básico de gestión de usuarios, pedidos y items de pedido usando SQLAlchemy ORM.

## Estructura
- `models.py`: Modelos de datos (User, Order, OrderItem)
- `database.py`: Configuración de la base de datos
- `crud.py`: Operaciones CRUD básicas
- `alembic/`: Migraciones de base de datos
- `test_crud.py`: Pruebas unitarias

## Instalación
```bash
pip install -r requirements.txt
```

## Ejecutar pruebas
```bash
pytest test_crud.py -v
```
## Laboratorio Completo: Acceso a datos y ORM con Python
He creado un proyecto completo para tu laboratorio de Python con SQLAlchemy ORM. A continuación te explico detalladamente cada componente:

##  Archivos Creados
Archivos principales:

requirements.txt - Dependencias necesarias
models.py - Modelos User, Order, OrderItem con relaciones
database.py - Configuración de SQLite en memoria
crud.py - Operaciones CRUD completas
test_crud.py - Pruebas unitarias exhaustivas
Ejemplos prácticos:

ejemplo1_basico.py - Uso fundamental del ORM
ejemplo2_avanzado.py - Consultas complejas y transacciones
ejemplo3_migraciones.py - Gestión de esquemas con Alembic


## Configuración de migraciones:
alembic.ini - Configuración de Alembic
alembic/env.py - Entorno de migraciones
alembic/versions/001_initial_migration.py - Migración inicial

## Pasos para Completar el Laboratorio
1. Instalación de Dependencias
bash
pip install -r requirements.txt
2. Entender los Modelos
User: Usuarios con username, email único
Order: Pedidos pertenecientes a usuarios
OrderItem: Items dentro de cada pedido
3. Ejecutar Ejemplos
bash
python ejemplo1_basico.py      # Conceptos básicos
python ejemplo2_avanzado.py    # Operaciones avanzadas  
python ejemplo3_migraciones.py  # Migraciones
4. Realizar Pruebas
bash
pytest test_crud.py -v

## Conceptos Clave Explicados
ORM (Object-Relational Mapping): Transforma tablas SQL en clases Python, permitiéndote trabajar con objetos en lugar de SQL directo.

CRUD Operations:

Create: Insertar nuevos registros
Read: Consultar datos existentes
Update: Modificar registros
Delete: Eliminar registros
Relaciones:

User → Orders (uno a muchos)
Order → OrderItems (uno a muchos)
Migraciones con Alembic: Gestiona cambios en el esquema de base de datos de forma versionada y segura.

## Para Empezar
Instala las dependencias con pip install -r requirements.txt
Ejecuta python ejemplo1_basico.py para entender lo básico
Corre las pruebas con pytest test_crud.py -v
