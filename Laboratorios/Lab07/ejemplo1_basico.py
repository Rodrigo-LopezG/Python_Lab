#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EJEMPLO 1: Cliente HTTP Básico con httpx
========================================

Este ejemplo te enseña los fundamentos de httpx:
- Realizar peticiones GET, POST, PUT, DELETE
- Manejar respuestas y códigos de estado
- Trabajar con JSON y datos binarios
- Headers y parámetros de URL

Autor: Programador Python Experto
Nivel: Principiante
"""

import httpx
import json
import sys
import io
from typing import Dict, Any

# Configurar codificación para Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def ejemplo_get_sencillo():
    """
    Ejemplo 1.1: Petición GET básica
    Obtenemos información de una API pública de usuarios
    """
    print(" Ejemplo 1.1: Petición GET básica")
    print("-" * 40)
    
    # URL de la API (JSONPlaceholder - API gratuita para pruebas)
    url = "https://jsonplaceholder.typicode.com/users/1"
    
    try:
        # Realizar petición GET
        response = httpx.get(url)
        
        # Verificar si la petición fue exitosa (código 200-299)
        if response.status_code == 200:
            print(" Petición exitosa!")
            print(f"Status Code: {response.status_code}")
            print(f"Headers: {dict(response.headers)}")
            
            # Convertir respuesta JSON a diccionario Python
            usuario = response.json()
            print(f"\n Usuario encontrado:")
            print(f"  Nombre: {usuario['name']}")
            print(f"  Email: {usuario['email']}")
            print(f"  Ciudad: {usuario['address']['city']}")
        else:
            print(f" Error en la petición: {response.status_code}")
            
    except httpx.RequestError as e:
        print(f" Error de conexión: {e}")

def ejemplo_get_con_parametros():
    """
    Ejemplo 1.2: GET con parámetros de consulta
    Buscamos posts con filtros
    """
    print("\n Ejemplo 1.2: GET con parámetros")
    print("-" * 40)
    
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Parámetros de consulta (query params)
    params = {
        "userId": 1,      # Solo posts del usuario 1
        "_limit": 5       # Máximo 5 resultados
    }
        "body": "Este es el contenido de mi post creado con httpx",
        "userId": 1
    }
    
    # Headers personalizados
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "MiClientePython/1.0"
    }
    
    try:
        response = httpx.post(
            url, 
            json=nuevo_post,  # httpx convierte automáticamente a JSON
            headers=headers
        )
        
        if response.status_code == 201:  # 201 = Created
            resultado = response.json()
            print(" Post creado exitosamente!")
            print(f"  ID asignado: {resultado['id']}")
            print(f"  Título: {resultado['title']}")
            print(f"  ID del usuario: {resultado['userId']}")
        else:
            print(f" Error al crear post: {response.status_code}")
            
    except httpx.RequestError as e:
        print(f" Error: {e}")

def ejemplo_put_y_delete():
    """
    Ejemplo 1.4: PUT (actualizar) y DELETE (eliminar)
    Modificamos y eliminamos recursos
    """
    print("\n Ejemplo 1.4: PUT y DELETE")
    print("-" * 40)
    
    # Primero actualizamos un post existente
    url_update = "https://jsonplaceholder.typicode.com/posts/1"
    
    datos_actualizados = {
        "id": 1,
        "title": "Título actualizado desde Python",
        "body": "Contenido modificado usando httpx",
        "userId": 1
    }
    
    try:
        # PUT para actualizar
        response = httpx.put(url_update, json=datos_actualizados)
        
        if response.status_code == 200:
            print(" Post actualizado!")
            actualizado = response.json()
            print(f"  Nuevo título: {actualizado['title']}")
        
        # Ahora eliminamos el post
        url_delete = "https://jsonplaceholder.typicode.com/posts/1"
        response = httpx.delete(url_delete)
        
        if response.status_code == 200:
            print(" Post eliminado!")
            
    except httpx.RequestError as e:
        print(f" Error: {e}")

def ejemplo_descargar_imagen():
    """
    Ejemplo 1.5: Descargar contenido binario (imagen)
    """
    print("\n Ejemplo 1.5: Descargar imagen")
    print("-" * 40)
    
    # URL de una imagen de prueba (logo de Python)
    url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
    
    try:
        response = httpx.get(url)
        
        if response.status_code == 200:
            # Guardar la imagen en un archivo
            with open("python_logo.png", "wb") as f:
                f.write(response.content)
            
            tamaño = len(response.content)
            print(f" Imagen descargada!")
            print(f"  Tamaño: {tamaño:,} bytes")
            print(f"  Guardada como: python_logo.png")
        else:
            print(f" Error al descargar: {response.status_code}")
            
    except httpx.RequestError as e:
        print(f" Error: {e}")

def main():
    """
    Función principal que ejecuta todos los ejemplos
    """
    print(" Laboratorio HTTP con httpx - Ejemplo 1: Cliente Básico")
    print("=" * 60)
    print("Aprende los fundamentos de las peticiones HTTP en Python\n")
    
    # Ejecutar todos los ejemplos
    ejemplo_get_sencillo()
    ejemplo_get_con_parametros()
    ejemplo_post_json()
    ejemplo_put_y_delete()
    ejemplo_descargar_imagen()
    
    print("\n" + "=" * 60)
    print(" Ejemplo 1 completado!")
    print(" Conceptos aprendidos:")
    print("   Peticiones GET, POST, PUT, DELETE")
    print("   Manejo de códigos de estado")
    print("   Trabajo con JSON y datos binarios")
    print("   Parámetros y headers")
    print("\n Siguiente paso: Ejemplo 2 (Reintentos y Timeouts)")

if __name__ == "__main__":
    main()
