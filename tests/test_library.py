from src import Book, Library
import pytest

# Fixture to create a book object
@pytest.fixture
def book():
    # Correct order and data types as per Book class constructor
    return Book("Test Title", "Test Author", "123456789", "Test Category")

# Fixture to create a library object
@pytest.fixture
def library():
    return Library()

# Test adding and retrieving a book
def test_add_and_get_book(library, book):
    library.add_book(book)
    assert library.get_book_by_isbn("123456789") == book
    assert book in library.get_all_books()

# Test adding a non-Book object
def test_add_non_book_object(library):
    with pytest.raises(ValueError):
        library.add_book("not a book")

# Test removing a book
def test_remove_book(library, book):
    library.add_book(book)
    library.remove_book(book.isbn)
    assert library.get_book_by_isbn(book.isbn) is None

# Test removing a book that doesn't exist
def test_remove_nonexistent_book(library):
    assert library.remove_book("nonexistent isbn") is None

# Test retrieving books by author
def test_get_books_by_author(library, book):
    library.add_book(book)
    assert book in library.get_books_by_author("Test Author")

# Test retrieving books by category
def test_get_books_by_category(library, book):
    library.add_book(book)
    assert book in library.get_books_by_category("Test Category")

# Test retrieving all books
def test_get_all_books(library, book):
    library.add_book(book)
    assert book in library.get_all_books()

# Test the count of books in the library
def test_get_number_of_books(library, book):
    library.add_book(book)
    assert library.get_number_of_books() == 1

# Test string representation
def test_str_representation(library, book):
    library.add_book(book)
    assert str(library) == "Library with 1 books"

# Test contains method
def test_contains_method(library, book):
    library.add_book(book)
    assert book.isbn in library

