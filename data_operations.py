# data_operations.py
"""
Handles CRUD and search operations for the database, along with statistics.
"""

from utils import validate_input, format_record
import os

def initialize_database(database_name, fields, max_lengths):
    """
    Initializes the database with system and data files.
    """
    if not os.path.exists(f"{database_name}_system.txt"):
        with open(f"{database_name}_system.txt", "w") as system_file:
            for field, length in zip(fields, max_lengths):
                system_file.write(f"{field},{length}\n")
        with open(f"{database_name}_data.txt", "w") as data_file:
            pass  # Create empty data file

def load_records(database_name):
    """
    Loads all records from the data file.
    """
    with open(f"{database_name}_data.txt", "r") as data_file:
        return [line.strip().split(",") for line in data_file]

def save_records(database_name, records):
    """
    Saves all records to the data file.
    """
    with open(f"{database_name}_data.txt", "w") as data_file:
        for record in records:
            data_file.write(",".join(record) + "\n")

def add_record(database_name, fields, max_lengths):
    """
    Adds a new record to the database.
    """
    print("\nAdding a new book.")
    record = [validate_input(f"Enter {field}: ", max_length) for field, max_length in zip(fields, max_lengths)]
    with open(f"{database_name}_data.txt", "a") as data_file:
        data_file.write(",".join(record) + "\n")
    print("Book added successfully.")

def edit_record(database_name, book_id, fields, max_lengths):
    """
    Edits an existing record in the database by Book ID.
    """
    records = load_records(database_name)
    for record in records:
        if record[0] == book_id:
            print(f"\nEditing record: {format_record(fields, record)}")
            for i, (field, max_length) in enumerate(zip(fields, max_lengths)):
                new_value = input(f"Enter new {field} (Leave blank to keep '{record[i]}'): ").strip()
                if new_value:
                    if len(new_value) <= max_length:
                        record[i] = new_value
                    else:
                        print(f"Error: {field} exceeds maximum length of {max_length}.")
            save_records(database_name, records)
            print("Book edited successfully.")
            return
    print(f"No book found with Book ID '{book_id}'.")

def delete_record(database_name, book_id):
    """
    Deletes a record by its Book ID.
    """
    records = load_records(database_name)
    updated_records = [record for record in records if record[0] != book_id]
    if len(updated_records) < len(records):
        save_records(database_name, updated_records)
        print(f"Book with Book ID '{book_id}' deleted successfully.")
    else:
        print(f"No book found with Book ID '{book_id}'.")

def search_records(database_name, query, fields):
    """
    Searches for a record based on a query.
    """
    records = load_records(database_name)
    results = [record for record in records if query in record]
    if results:
        print("\nSearch Results:")
        for record in results:
            print(format_record(fields, record))
    else:
        print("No matching records found.")

def calculate_statistics(database_name):
    """
    Calculates basic statistics for the database.
    """
    records = load_records(database_name)
    total_books = len(records)
    print("\nLibrary Statistics:")
    print(f"Total number of books: {total_books}")
