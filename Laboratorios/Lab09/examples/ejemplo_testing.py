"""
Ejemplo 3: Testing Automatizado de la API
Este ejemplo muestra cómo realizar pruebas automatizadas
"""

import pytest
import requests
import json
import time
import sqlite3
import hashlib
import os

# Configuración de pruebas
BASE_URL = "http://localhost:8000"
TEST_DB = "test_orders.db"

class TestOrdersAPI:
    """Clase de testing para la API de Orders"""
    
    @classmethod
    def setup_class(cls):
        """Configuración inicial para todas las pruebas"""
        print("\n=== INICIANDO PRUEBAS AUTOMATIZADAS ===")
        
        # Verificar que el servidor esté corriendo
        try:
            response = requests.get(f"{BASE_URL}/docs", timeout=5)
            if response.status_code != 200:
                pytest.skip("El servidor no está corriendo o no es accesible")
        except requests.exceptions.RequestException:
            pytest.skip("No se puede conectar al servidor. Inicia el servidor con: python main.py")
        
        # Configurar base de datos de prueba
        cls.setup_test_database()
        
        # Obtener token de autenticación
        cls.token = cls.get_auth_token()
        cls.headers = {"Authorization": f"Bearer {cls.token}"}
    
    @classmethod
    def setup_test_database(cls):
        """Configurar base de datos para pruebas"""
        # Crear base de datos de prueba
        conn = sqlite3.connect(TEST_DB)
        cursor = conn.cursor()
        
        # Crear tablas
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            product TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending'
        )
        ''')
        
        # Insertar usuario de prueba
        hashed_password = hashlib.sha256("test123".encode()).hexdigest()
        cursor.execute("INSERT OR REPLACE INTO users VALUES (?, ?)", ("testuser", hashed_password))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_auth_token(cls):
        
        result = response.json()
        assert "message" in result
        
        # Verificar que la orden fue eliminada
        response = requests.get(f"{BASE_URL}/orders/{self.test_order_id}", headers=self.headers)
        assert response.status_code == 404
        
        print(f"    Orden {self.test_order_id} eliminada correctamente")
    
    def test_07_validation_errors(self):
        """Prueba 7: Validación de errores"""
        print("\n7. Probando validación de datos...")
        
        # Datos inválidos
        invalid_orders = [
            {
                "customer_name": "Test",
                "product": "Test",
                "quantity": -1,  # Inválido
                "price": 10.00
            },
            {
                "customer_name": "",  # Inválido
                "product": "Test",
                "quantity": 1,
                "price": 10.00
            },
            {
                "customer_name": "Test",
                "product": "Test",
                "quantity": 1,
                "price": -10.00  # Inválido
            }
        ]
        
        for i, invalid_order in enumerate(invalid_orders, 1):
            response = requests.post(f"{BASE_URL}/orders/", json=invalid_order, headers=self.headers)
            assert response.status_code == 422  # Unprocessable Entity
            print(f"    Orden inválida {i} rechazada correctamente")
    
    def test_08_unauthorized_access(self):
        """Prueba 8: Acceso no autorizado"""
        print("\n8. Probando acceso no autorizado...")
        
        # Intentar acceder sin token
        response = requests.get(f"{BASE_URL}/orders/")
        assert response.status_code == 403  # Forbidden
        
        # Intentar acceder con token inválido
        invalid_headers = {"Authorization": "Bearer invalid_token"}
        response = requests.get(f"{BASE_URL}/orders/", headers=invalid_headers)
        assert response.status_code == 401  # Unauthorized
        
        print("    Acceso no autorizado manejado correctamente")
    
    @classmethod
    def teardown_class(cls):
        """Limpieza después de todas las pruebas"""
        print("\n=== LIMPIEZA DE PRUEBAS ===")
        
        # Eliminar base de datos de prueba
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)
            print("✅ Base de datos de prueba eliminada")
        
        print("=== PRUEBAS COMPLETADAS ===\n")

def run_manual_tests():
    """Ejecutar pruebas manuales sin pytest"""
    print("=== EJECUTANDO PRUEBAS MANUALES ===")
    
    # Crear instancia de pruebas
    test_instance = TestOrdersAPI()
    
    try:
        # Configurar
        test_instance.setup_class()
        
        # Ejecutar pruebas una por una
        test_methods = [
            test_instance.test_01_authentication,
            test_instance.test_02_create_order,
            test_instance.test_03_get_orders,
            test_instance.test_04_get_order_by_id,
            test_instance.test_05_update_order,
            test_instance.test_06_delete_order,
            test_instance.test_07_validation_errors,
            test_instance.test_08_unauthorized_access
        ]
        
        passed = 0
        failed = 0
        
        for test_method in test_methods:
            try:
                test_method()
                passed += 1
                print(f" {test_method.__name__} - PASÓ")
            except Exception as e:
                failed += 1
                print(f" {test_method.__name__} - FALLÓ: {e}")
        
        # Limpiar
        test_instance.teardown_class()
        
        print(f"\n=== RESUMEN DE PRUEBAS ===")
        print(f" Pasadas: {passed}")
        print(f" Fallidas: {failed}")
        print(f"Total: {passed + failed}")
        
    except Exception as e:
        print(f" Error en la configuración de pruebas: {e}")

if __name__ == "__main__":
    # Opción 1: Ejecutar con pytest (recomendado)
    # pytest.run([__file__, "-v"])
    
    # Opción 2: Ejecutar pruebas manuales
    run_manual_tests()
