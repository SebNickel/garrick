import sqlite3

def connect(db_file):

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
        
    return conn, cursor
    
def disconnect(conn, cursor):

    cursor.close()
    conn.close()
