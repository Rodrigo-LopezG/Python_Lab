from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
import hashlib
import jwt
from datetime import datetime, timedelta
import os

# Configuración
SECRET_KEY = "tu_clave_secreta_aqui"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Inicialización de FastAPI
app = FastAPI(title="API de Orders", version="1.0.0")

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Seguridad
security = HTTPBearer()

# Modelos Pydantic
class User(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Order(BaseModel):
    id: Optional[int] = None
    customer_name: str
    product: str
    quantity: int
    price: float
    status: str = "pending"

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    product: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    status: Optional[str] = None

# Base de datos
def init_db():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    
    # Tabla de usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
    ''')
    
    # Tabla de orders
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO orders (customer_name, product, quantity, price, status)
    VALUES (?, ?, ?, ?, ?)
    ''', (order.customer_name, order.product, order.quantity, order.price, order.status))
    order.id = cursor.lastrowid
    conn.commit()
    conn.close()
    return order

@app.get("/orders/", response_model=List[Order])
async def get_orders(current_user: str = Depends(verify_token)):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    conn.close()
    
    orders = []
    for row in rows:
        orders.append(Order(
            id=row[0],
            customer_name=row[1],
            product=row[2],
            quantity=row[3],
            price=row[4],
            status=row[5]
        ))
    return orders

@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int, current_user: str = Depends(verify_token)):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="Order no encontrada")
    
    return Order(
        id=row[0],
        customer_name=row[1],
        product=row[2],
        quantity=row[3],
        price=row[4],
        status=row[5]
    )

@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, order_update: OrderUpdate, current_user: str = Depends(verify_token)):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    
    # Obtener order actual
    cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Order no encontrada")
    
    # Actualizar campos
    update_data = order_update.dict(exclude_unset=True)
    if not update_data:
        conn.close()
        return Order(
            id=row[0],
            customer_name=row[1],
            product=row[2],
            quantity=row[3],
            price=row[4],
            status=row[5]
        )
    
    set_clause = ", ".join([f"{k} = ?" for k in update_data.keys()])
    values = list(update_data.values()) + [order_id]
    
    cursor.execute(f"UPDATE orders SET {set_clause} WHERE id=?", values)
    conn.commit()
    
    # Obtener order actualizada
    cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
    row = cursor.fetchone()
    conn.close()
    
    return Order(
        id=row[0],
        customer_name=row[1],
        product=row[2],
        quantity=row[3],
        price=row[4],
        status=row[5]
    )

@app.delete("/orders/{order_id}")
async def delete_order(order_id: int, current_user: str = Depends(verify_token)):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
    row = cursor.fetchone()
    
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Order no encontrada")
    
    cursor.execute("DELETE FROM orders WHERE id=?", (order_id,))
    conn.commit()
    conn.close()
    
    return {"message": "Order eliminada exitosamente"}

# Inicializar base de datos al iniciar
@app.on_event("startup")
async def startup_event():
    init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
