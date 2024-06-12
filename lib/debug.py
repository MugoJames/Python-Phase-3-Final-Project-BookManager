from lib.models.book import create_book_table
from lib.models.user import create_user_table

def create_tables():
    create_user_table()
    create_book_table()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully")
