import sqlite3
import os

def get_connection():
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'database.db')
    return sqlite3.connect(db_path)
