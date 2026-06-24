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
        
def main():
    """
    Función principal que ejecuta todos los ejemplos
    """
    print(" Laboratorio HTTP con httpx - Ejemplo 1: Cliente Básico")
    print("=" * 60)
    print("Aprende los fundamentos de las peticiones HTTP en Python\n")
    
    # Ejecutar todos los ejemplos
    ejemplo_get_sencillo()
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
