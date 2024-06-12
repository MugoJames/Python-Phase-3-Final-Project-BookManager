from lib.helpers import get_connection

def create_user_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_user(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name)
        VALUES (?)
    ''', (name,))
    conn.commit()
    conn.close()

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def find_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

def update_user(user_id, name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users
        SET name = ?
        WHERE id = ?
    ''', (name, user_id))
    conn.commit()
    conn.close()
