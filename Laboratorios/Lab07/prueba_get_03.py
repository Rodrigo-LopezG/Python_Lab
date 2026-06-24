#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EJEMPLO 2: Cliente HTTP Asincrónico y Concurrente
=================================================
"""

import asyncio
import httpx
import time
from typing import Any, Dict, List, Optional

BASE_URL = "https://jsonplaceholder.typicode.com"

async def obtener_usuario_async(client: httpx.AsyncClient, user_id: int) -> Optional[Dict[str, Any]]:
    """
    Corrutina para obtener datos de un usuario de forma asincrónica.
    """
    url = f"{BASE_URL}/users/{user_id}"
    
    try:
        # El uso de 'await' cede el control al event loop mientras espera la red
        response = await client.get(url, timeout=5.0)
        response.raise_for_status()
        return response.json()
        
    except httpx.HTTPStatusError as e:
        print(f" Error HTTP {e.response.status_code} para {e.request.url}")
    except httpx.RequestError as e:
        print(f" Error de red en {e.request.url}: {e}")
    except Exception as e:
        print(f" Error inesperado con usuario {user_id}: {e}")
        
    return None

async def ejecutar_descarga_masiva() -> None:
    """
    Orquesta la ejecución concurrente de múltiples peticiones HTTP.
    """
    # Simularemos la obtención de 15 usuarios
    user_ids = list(range(1, 16))
    print(f" Iniciando descarga concurrente de {len(user_ids)} usuarios...")
    
    start_time = time.perf_counter()
    
    # httpx.AsyncClient maneja el pool de conexiones asincrónicas
    async with httpx.AsyncClient() as client:
        # 1. Creamos una lista de tareas (corrutinas pendientes de ejecución)
        # CRÍTICO: No usamos 'await' dentro de este bucle for.
        tareas = [obtener_usuario_async(client, uid) for uid in user_ids]
        
        # 2. Ejecutamos TODAS las tareas concurrentemente con asyncio.gather
        # Esto es lo que realmente paraleliza las peticiones en la red
        resultados: List[Optional[Dict[str, Any]]] = await asyncio.gather(*tareas)
        
    end_time = time.perf_counter()
    
    # Filtramos los resultados nulos (peticiones fallidas)
    usuarios_exitosos = [u for u in resultados if u is not None]
    
    print("-" * 40)
    print(f" Tiempo total de ejecución: {end_time - start_time:.3f} segundos.")
    print(f" Usuarios recuperados con éxito: {len(usuarios_exitosos)} de {len(user_ids)}")
    print("-" * 40)

def main() -> None:
    print(" Laboratorio HTTP - Ejecución Asincrónica")
    print("=" * 60)
    # Punto de entrada para el bucle de eventos (Event Loop) de asyncio
    asyncio.run(ejecutar_descarga_masiva())

if __name__ == "__main__":
    main()
