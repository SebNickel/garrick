from mysql.connector import MySQLConnection, Error
from db_config import read_db_config

def connect():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        
        return conn, cursor

    except Error as error:
        raise Exception(error)
    
def disconnect(conn, cursor):
    cursor.close()
    conn.close()
