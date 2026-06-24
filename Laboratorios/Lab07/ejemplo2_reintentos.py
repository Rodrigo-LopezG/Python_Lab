#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EJEMPLO 2: Cliente HTTP con Reintentos y Timeouts
=================================================

Este ejemplo te enseña a construir clientes HTTP robustos:
- Configurar timeouts para evitar esperas infinitas
- Implementar reintentos automáticos con backoff exponencial
- Manejar diferentes tipos de errores de conexión
- Crear un cliente reutilizable con configuración personalizada

Autor: Programador Python Experto
Nivel: Intermedio
"""

import httpx
import time
import sys
import io
from typing import Optional, Dict, Any
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from utils.exceptions import TimeoutError, RetryExhaustedError

# Configurar codificación para Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

class RobustHTTPClient:
    """
    Cliente HTTP robusto con reintentos y timeouts
    """
    
    def __init__(self, 
                 timeout_connect: float = 5.0,
                 timeout_read: float = 30.0,
                 timeout_write: float = 10.0,
                 max_retries: int = 3,
                 retry_delay: float = 1.0):
        """
        Inicializa el cliente HTTP con configuración de timeouts y reintentos
        
        Args:
            timeout_connect: Tiempo máximo para establecer conexión (segundos)
            timeout_read: Tiempo máximo para recibir respuesta (segundos)
            timeout_write: Tiempo máximo para enviar datos (segundos)
            max_retries: Número máximo de reintentos
            retry_delay: Tiempo base entre reintentos (segundos)
        """
        self.timeout_connect = timeout_connect
        self.timeout_read = timeout_read
        self.timeout_write = timeout_write
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        
        # Configurar timeouts para httpx
        self.timeouts = httpx.Timeout(
            connect=timeout_connect,
            read=timeout_read,
            write=timeout_write,
            pool=timeout_connect
        )
        
        # Crear cliente con configuración
        self.client = httpx.Client(timeout=self.timeouts)
        
        print(f"🔧 Cliente HTTP configurado:")
        print(f"  Timeout conexión: {timeout_connect}s")
        print(f"  Timeout lectura: {timeout_read}s")
        print(f"  Timeout escritura: {timeout_write}s")
        print(f"  Reintentos máximos: {max_retries}")

    @retry(
        stop=stop_after_attempt(3),
    Ejemplo 2.3: POST con reintentos
    """
    print("\n Ejemplo 2.3: POST con reintentos")
    print("-" * 50)
    
    url = "https://httpbin.org/post"
    
    datos = {
        "nombre": "Python Developer",
        "mensaje": "Probando reintentos en POST",
        "timestamp": time.time()
    }
    
    client = RobustHTTPClient(max_retries=3, retry_delay=1.0)
    
    try:
        response = client.post_with_retry(url, datos)
        print(" POST exitoso!")
        
        resultado = response.json()
        print(f"  Datos recibidos: {resultado['json']}")
        
    except Exception as e:
        print(f" Error en POST: {e}")
    
    client.close()

def ejemplo_cliente_personalizado():
    """
    Ejemplo 2.4: Crear un cliente completamente personalizado
    """
    print("\n Ejemplo 2.4: Cliente HTTP personalizado")
    print("-" * 50)
    
    # Configuración personalizada para un caso específico
    class APIClient(RobustHTTPClient):
        """Cliente personalizado para una API específica"""
        
        def __init__(self):
            super().__init__(
                timeout_connect=3.0,
                timeout_read=15.0,
                timeout_write=5.0,
                max_retries=5,
                retry_delay=0.5
            )
            
            # Headers personalizados para todas las peticiones
            self.client.headers.update({
                "User-Agent": "MiAPIClient/1.0",
                "Accept": "application/json",
                "X-API-Key": "mi-clave-secreta"  # En producción usar variables de entorno
            })
        
        def get_user(self, user_id: int) -> Dict[str, Any]:
            """Obtener información de un usuario"""
            url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
            response = self.get_with_retry(url)
            return response.json()
        
        def create_post(self, user_id: int, title: str, body: str) -> Dict[str, Any]:
            """Crear un nuevo post"""
            url = "https://jsonplaceholder.typicode.com/posts"
            data = {
                "title": title,
                "body": body,
                "userId": user_id
            }
            response = self.post_with_retry(url, data)
            return response.json()
    
    # Usar el cliente personalizado
    api = APIClient()
    
    try:
        # Obtener usuario
        print(" Obteniendo información del usuario...")
        user = api.get_user(1)
        print(f" Usuario: {user['name']} ({user['email']})")
        
        # Crear post
        print("\n Creando nuevo post...")
        post = api.create_post(
            user_id=1,
            title="Post desde cliente personalizado",
            body="Este post fue creado usando nuestro cliente HTTP robusto"
        )
        print(f" Post creado con ID: {post['id']}")
        
    except Exception as e:
        print(f" Error: {e}")
    finally:
        api.close()

def main():
    """
    Función principal que ejecuta todos los ejemplos
    """
    print(" Laboratorio HTTP con httpx - Ejemplo 2: Reintentos y Timeouts")
    print("=" * 70)
    print("Aprende a construir clientes HTTP robustos y resilientes\n")
    
    # Ejecutar todos los ejemplos
    ejemplo_timeout_configurado()
    ejemplo_reintentos_con_fallos()
    ejemplo_post_con_reintentos()
    ejemplo_cliente_personalizado()
    
    print("\n" + "=" * 70)
    print(" Ejemplo 2 completado!")
    print(" Conceptos aprendidos:")
    print("   Configuración de timeouts (connect, read, write)")
    print("   Reintentos automáticos con backoff exponencial")
    print("   Manejo de diferentes tipos de errores")
    print("   Creación de clientes HTTP reutilizables")
    print("   Uso de decoradores para reintentos")
    print("\n Siguiente paso: Ejemplo 3 (Streaming de archivos)")

if __name__ == "__main__":
    main()
