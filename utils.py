# utils.py
"""
Helper functions for validation, file operations, and user input.
"""

import os

def validate_input(prompt, max_length):
    """
    Validates user input based on the maximum allowed length.
    """
    while True:
        value = input(prompt).strip()
        if len(value) <= max_length:
            return value
        print(f"Error: Input exceeds maximum length of {max_length} characters.")

def file_exists(filename):
    """
    Checks if a file exists.
    """
    return os.path.exists(filename)

def authenticate_user(credentials):
    """
    Authenticates a user based on predefined credentials.
    """
    print("\nUser Authentication")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    return credentials.get(username) == password

def format_record(fields, record):
    """
    Formats a record for display.
    """
    return ", ".join([f"{field}: '{value}'" for field, value in zip(fields, record)])
