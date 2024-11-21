import streamlit as st
import sqlite3
import pandas as pd
import sys
import os

# Agrega el directorio raíz al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.db_setup import create_tables


# Función para conectarse a la base de datos
def get_connection():
    # Verifica si el archivo de base de datos existe
    try:
        return sqlite3.connect('data/erp_system.db')  # Usa la ruta completa si está en un subdirectorio
    except sqlite3.Error as e:
        st.error(f"Error al conectar a la base de datos: {e}")
        return None

# Asegúrate de que las tablas se crean antes de usarlas
def create_tables():
    conn = get_connection()
    if conn is None:
        st.error("No se pudo conectar a la base de datos.")
        return
    cursor = conn.cursor()
    try:
        # Crea la tabla si no existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL,
                telefono TEXT NOT NULL,
                direccion TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Error al crear la tabla: {e}")
    finally:
        conn.close()

# Llamada a la función para asegurarse de que la tabla existe
create_tables()

# Inserta y consulta datos
try:
    conn = get_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO clientes (nombre, correo, telefono, direccion) 
            VALUES ('Juan', 'juan@example.com', '123456789', 'Calle 123')
        """)
        conn.commit()

        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        st.write("Clientes en la base de datos:", clientes)
    else:
        st.error("No se pudo insertar ni consultar datos porque la conexión falló.")
finally:
    if conn:
        conn.close()

# Asegurarse de que las tablas se creen antes de usarlas
create_tables()

# Menú de navegación
st.sidebar.title("Sistema ERP")
menu = st.sidebar.selectbox("Seleccione una opción", ["Gestión de Clientes", "Gestión de Productos", "Inventario", "Facturación", "Análisis de Ventas", "Reportes"])

if menu == "Gestión de Clientes":
    st.title("Gestión de Clientes")
    # CRUD para clientes
    conn = get_connection()
    cursor = conn.cursor()

    if st.button("Ver Clientes"):
        df_clientes = pd.read_sql_query("SELECT * FROM clientes", conn)
        st.dataframe(df_clientes)

    with st.form("add_cliente"):
        st.subheader("Añadir Cliente")
        nombre = st.text_input("Nombre")
        correo = st.text_input("Correo")
        telefono = st.text_input("Teléfono")
        direccion = st.text_area("Dirección")
        submit = st.form_submit_button("Guardar")

        if submit and nombre and correo:
            cursor.execute("INSERT INTO clientes (nombre, correo, telefono, direccion) VALUES (?, ?, ?, ?)", (nombre, correo, telefono, direccion))
            conn.commit()
            st.success("Cliente añadido")

    conn.close()

# Similar para otros módulos: Gestión de Productos, Facturación, Inventario, Análisis de Ventas.
