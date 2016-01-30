import sqlite3

def connect(db_file):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        return conn, cursor

    except sqlite3.Error as error:
        raise Exception(error)
    
def disconnect(conn, cursor):
    cursor.close()
    conn.close()
