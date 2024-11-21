import sqlite3

def get_connection():
    return sqlite3.connect('data/erp_system.db')

def execute_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    conn.close()
