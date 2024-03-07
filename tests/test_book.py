# tests/test_book.py

import pytest
from src.book import Book

# Test successful instantiation
def test_book_creation():
    book = Book("Test Title", "Test Author", "1234567890123", "Test Category")
    assert book.title == "Test Title"
    assert book.author == "Test Author"
    assert book.isbn == "1234567890123"
    assert book.category == "Test Category"

# Test instantiation with invalid types
def test_book_creation_invalid_types():
    with pytest.raises(ValueError):
        Book(123, "Test Author", "1234567890123", "Test Category")
    with pytest.raises(ValueError):
        Book("Test Title", 123, "1234567890123", "Test Category")
    with pytest.raises(ValueError):
        Book("Test Title", "Test Author", 123, "Test Category")
    with pytest.raises(ValueError):
        Book("Test Title", "Test Author", "1234567890123", 123)

# Test instantiation with invalid ISBN
def test_book_creation_invalid_isbn():
    with pytest.raises(ValueError):
        Book("Test Title", "Test Author", 1234, "Test Category")

# Test string representation
def test_book_str():
    book = Book("Test Title", "Test Author", "1234567890123", "Test Category")
    assert str(book) == "'Test Title' by Test Author (ISBN: 1234567890123) - Category: Test Category"

# Test updating the title
def test_book_update_title():
    book = Book("Test Title", "Test Author", "1234567890123", "Test Category")
    book.update_title("New Title")
    assert book.title == "New Title"

# Test updating the author
def test_book_update_author():
    book = Book("Test Title", "Test Author", "1234567890123", "Test Category")
    book.update_author("New Author")
    assert book.author == "New Author"

# Test updating the category
def test_book_update_category():
    book = Book("Test Title", "Test Author", "1234567890123", "Test Category")
    book.update_category("New Category")
    assert book.category == "New Category"

# Test equality based on ISBN
def test_book_equality():
    book1 = Book("Test Title", "Test Author", "1234567890123", "Test Category")
    book2 = Book("Test Title", "Test Author", "1234567890123", "Test Category")
    book3 = Book("Test Title", "Test Author", "0000000000000", "Test Category")
    assert book1 == book2
    assert book1 != book3

# Test the get_details method
def test_book_get_details():
    book = Book("Test Title", "Test Author", "1234567890123", "Test Category")
    expected_details = {
        'title': "Test Title",
        'author': "Test Author",
        'isbn': "1234567890123",
        'category': "Test Category"
    }
    assert book.get_details() == expected_details

# Run the tests
if __name__ == "__main__":
    pytest.main()
