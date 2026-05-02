# test_data_operations.py
"""
Unit tests for data_operations.py functions.
"""

import os
from data_operations import (
    initialize_database,
    add_record,
    load_records,
    edit_record,
    delete_record,
    calculate_statistics
)
from constants import DATABASE_NAME, FIELDS, MAX_LENGTHS

def test_initialize_database():
    """
    Test database initialization.
    """
    initialize_database(DATABASE_NAME, FIELDS, MAX_LENGTHS)
    assert os.path.exists(f"{DATABASE_NAME}_system.txt"), "System file not created."
    assert os.path.exists(f"{DATABASE_NAME}_data.txt"), "Data file not created."
    print("Test: initialize_database - Passed.")

def test_add_and_load_records():
    """
    Test adding and loading records.
    """
    add_record(DATABASE_NAME, FIELDS, MAX_LENGTHS)
    records = load_records(DATABASE_NAME)
    assert len(records) > 0, "Record not added correctly."
    print("Test: add_and_load_records - Passed.")

def test_edit_record():
    """
    Test editing a record.
    """
    add_record(DATABASE_NAME, FIELDS, MAX_LENGTHS)
    records = load_records(DATABASE_NAME)
    original_record = records[0]
    book_id = original_record[0]
    edit_record(DATABASE_NAME, book_id, FIELDS, MAX_LENGTHS)
    updated_records = load_records(DATABASE_NAME)
    assert updated_records[0] != original_record, "Record not updated correctly."
    print("Test: edit_record - Passed.")

def test_delete_record():
    """
    Test deleting a record.
    """
    add_record(DATABASE_NAME, FIELDS, MAX_LENGTHS)
    records = load_records(DATABASE_NAME)
    book_id = records[0][0]
    delete_record(DATABASE_NAME, book_id)
    updated_records = load_records(DATABASE_NAME)
    assert len(updated_records) == len(records) - 1, "Record not deleted correctly."
    print("Test: delete_record - Passed.")

def test_calculate_statistics():
    """
    Test calculating statistics.
    """
    add_record(DATABASE_NAME, FIELDS, MAX_LENGTHS)
    calculate_statistics(DATABASE_NAME)  # Should not raise exceptions
    print("Test: calculate_statistics - Passed.")

if __name__ == "__main__":
    # Run all tests
    test_initialize_database()
    test_add_and_load_records()
    test_edit_record()
    test_delete_record()
    test_calculate_statistics()
    print("All tests passed successfully.")
