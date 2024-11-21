import sqlite3
import os

def create_tables():
    # Ruta absoluta al archivo de base de datos
    db_path = os.path.join(os.path.dirname(__file__), "../data/erp_system.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear las tablas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        correo TEXT,
        telefono TEXT,
        direccion TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        categoria TEXT,
        precio REAL,
        cantidad INTEGER
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS facturas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        fecha TEXT,
        total REAL,
        FOREIGN KEY(cliente_id) REFERENCES clientes(id)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS detalles_factura (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        factura_id INTEGER,
        producto_id INTEGER,
        cantidad INTEGER,
        precio_unitario REAL,
        subtotal REAL,
        FOREIGN KEY(factura_id) REFERENCES facturas(id),
        FOREIGN KEY(producto_id) REFERENCES productos(id)
    )''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
