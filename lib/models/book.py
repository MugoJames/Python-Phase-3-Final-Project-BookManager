from lib.helpers import get_connection

def create_book_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

def create_book(title, author, user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (title, author, user_id)
        VALUES (?, ?, ?)
    ''', (title, author, user_id))
    conn.commit()
    conn.close()

def get_all_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def get_books_by_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE user_id = ?', (user_id,))
    books = cursor.fetchall()
    conn.close()
    return books

def find_book_by_id(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    book = cursor.fetchone()
    conn.close()
    return book

def find_books_by_author(author):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE author = ?', (author,))
    books = cursor.fetchall()
    conn.close()
    return books

def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()

def update_book(book_id, title, author, user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE books
        SET title = ?, author = ?, user_id = ?
        WHERE id = ?
    ''', (title, author, user_id, book_id))
    conn.commit()
    conn.close()
