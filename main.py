import streamlit as st
import sqlite3
import pandas as pd
from erp_percistente.database import create_tables


# Asegurarse de que las tablas se creen antes de usarlas
create_tables()

# Función para conectarse a la base de datos
def get_connection():
    return sqlite3.connect('erp_system.db')
    
# Ejemplo: Insertar y consultar clientes
cursor.execute("INSERT INTO clientes (nombre, correo, telefono, direccion) VALUES ('Juan', 'juan@example.com', '123456789', 'Calle 123')")
conn.commit()

cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()
print(clientes)

conn.close()
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
