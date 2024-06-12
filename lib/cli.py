import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.models import book as book_model  # Renaming to avoid naming conflict
from lib.models import user
from lib.debug import create_tables

def print_menu():
    print("\n--- BookManager ---")
    print("1. Add new user")
    print("2. Add new book")
    print("3. View All Books")
    print("4. View Books by Users")
    print("5. View Book by ID")
    print("6. Delete Book")
    print("7. Update Book")
    print("8. Update User")
    print("9. Exit")

def start_cli():
    create_tables()
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter username: ")
            user.create_user(name)
            print("User created successfully")
        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            user_id = input("Enter user ID: ")
            book_model.create_book(title, author, user_id)
            print("Book created successfully")
        elif choice == "3":
            books = book_model.get_all_books()
            for book in books:
                print(book)
        elif choice == "4":
            user_id = input("Enter user ID: ")
            books = book_model.get_books_by_user(user_id)
            for book in books:
                print(book)
        elif choice == "5":
            book_id = input("Enter book ID: ")
            book = book_model.find_book_by_id(book_id)
            if book:
                print(book)
            else:
                print("Book not found")
        elif choice == "6":
            book_id = input("Enter book ID: ")
            book_model.delete_book(book_id)
            print("Book deleted successfully")
        elif choice == "7":
            book_id = input("Enter book ID: ")
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            user_id = input("Enter new user ID: ")
            book_model.update_book(book_id, title, author, user_id)
            print("Book updated successfully")
        elif choice == "8":
            user_id = input("Enter user ID: ")
            name = input("Enter new username: ")
            user.update_user(user_id, name)
            print("User updated successfully")
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    start_cli()
