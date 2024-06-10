from lib.helpers import get_connection

def create_book(title,author,user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books(title,author,user_id) VALUES (?,?,?)',(title,author, user_id))
    conn.commit()
    conn.close()

def get_all_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def get_book_by_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE user_id=?',(user_id))
    books = cursor.fetchall()
    conn.close()
    return books

def get_book_by_id(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id=?',(book_id))
    book = cursor.fetchone()
    conn.close()
    return book
def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id=?',(book_id))
    conn.commit()
    conn.close()
    