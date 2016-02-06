import sqlite3
import re

def match_regex(regex, item):

    return re.search(regex, item) is not None

def connect(db_file):

    conn = sqlite3.connect(db_file)
    conn.create_function("MATCHES", 2, match_regex)
    cursor = conn.cursor()
        
    return conn, cursor
    
def disconnect(conn, cursor):

    cursor.close()
    conn.close()
