import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.models import book as book_model
from lib.models import user as user_model
from lib.debug import create_tables

def print_menu():
    print("\n--- BookManager ---")
    print("1. Add new user")
    print("2. Add new book")
    print("3. View All Books")
    print("4. View Books by User ID")
    print("5. View Book by book ID")
    print("6. View Book by Author")
    print("7. Delete Book")
    print("8. Update Book")
    print("9. View all Users")
    print("10. Find user by ID")
    print("11. Delete User")
    print("12. Update User")
    print("13. Exit")

def start_cli():
    create_tables()
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter username: ")
            user_model.create_user(name)
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
            author = input("Enter book author: ")
            books = book_model.find_books_by_author(author)
            for book in books:
                print(book)
                
        elif choice == "7":
            book_id = input("Enter book ID: ")
            book_model.delete_book(book_id)
            print("Book deleted successfully")

        elif choice == "8":
            book_id = input("Enter book ID: ")
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            user_id = input("Enter new user ID: ")
            book_model.update_book(book_id, title, author, user_id)
            print("Book updated successfully")

        elif choice == "9":
            users = user_model.get_all_users()
            for user in users:
                print(user)

        elif choice == "10":
            user_id = input("Enter user ID: ")
            user = user_model.find_user_by_id(user_id)
            if user:
                print(user)
            else:
                print("User not found")

        elif choice == "11":
            user_id = input("Enter user ID: ")
            user_model.delete_user(user_id)
            print("User deleted successfully")

        elif choice == "12":
            user_id = input("Enter user ID: ")
            name = input("Enter new username: ")
            user_model.update_user(user_id, name)
            print("User updated successfully")

        elif choice == "13":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    start_cli()
