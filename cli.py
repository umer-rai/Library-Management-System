# cli.py
"""
Command-line interface for the Library Management System.
"""

from data_operations import (
    initialize_database,
    add_record,
    edit_record,
    delete_record,
    search_records,
    load_records,
    calculate_statistics,
)
from constants import DATABASE_NAME, FIELDS, MAX_LENGTHS, USER_CREDENTIALS
from utils import authenticate_user, format_record

def run_cli():
    """
    Runs the CLI for interacting with the LMS.
    """
    print("Welcome to the Library Management System (LMS)!")
    
    # User authentication
    if not authenticate_user(USER_CREDENTIALS):
        print("Access denied. Exiting system.")
        return

    # Initialize database
    initialize_database(DATABASE_NAME, FIELDS, MAX_LENGTHS)

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add a new book")
        print("2. Edit a book")
        print("3. Delete a book")
        print("4. Search for a book")
        print("5. View all books")
        print("6. View statistics")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_record(DATABASE_NAME, FIELDS, MAX_LENGTHS)
        elif choice == "2":
            book_id = input("Enter the Book ID to edit: ").strip()
            edit_record(DATABASE_NAME, book_id, FIELDS, MAX_LENGTHS)
        elif choice == "3":
            book_id = input("Enter the Book ID to delete: ").strip()
            delete_record(DATABASE_NAME, book_id)
        elif choice == "4":
            query = input("Enter search query (Book ID, Name, or Author): ").strip()
            search_records(DATABASE_NAME, query, FIELDS)
        elif choice == "5":
            records = load_records(DATABASE_NAME)
            print("\nAll Books:")
            for record in records:
                print(format_record(FIELDS, record))
        elif choice == "6":
            calculate_statistics(DATABASE_NAME)
        elif choice == "7":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
