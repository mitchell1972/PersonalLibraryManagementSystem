import pytest
import json
import os
from src.utilities import Library, save_library_to_file, load_library_from_file, search_books
from src.book import Book


@pytest.fixture
def sample_library():
    library = Library()
    # Use a string of digits for the ISBN value
    book1 = Book("Title One", "Author One", "1234567890", "Category One")
    book2 = Book("Title Two", "Author Two", "1234567891", "Category Two")
    library.add_book(book1)
    library.add_book(book2)
    return library


@pytest.fixture
def filepath(tmpdir):
    return tmpdir.join("library.json")

def test_save_library_to_file(sample_library, filepath):
    save_library_to_file(sample_library, filepath)
    assert os.path.exists(filepath)
    with open(filepath, 'r') as file:
        data = json.load(file)
    assert len(data) == 2
    # You can add more assertions here to check the content

def test_load_library_from_file(sample_library, filepath):
    # First, save the current state of the library to a file
    save_library_to_file(sample_library, filepath)
    # Create a new library instance to load the books into
    new_library = Library()
    load_library_from_file(new_library, filepath)
    assert new_library.get_number_of_books() == 2
    # Additional checks can be added for book details

def test_search_books_by_title(sample_library):
    found_books = search_books(sample_library, title="Title One")
    assert len(found_books) == 1
    assert found_books[0].title == "Title One"

def test_search_books_by_author(sample_library):
    found_books = search_books(sample_library, author="Author Two")
    assert len(found_books) == 1
    assert found_books[0].author == "Author Two"

def test_search_books_by_category(sample_library):
    found_books = search_books(sample_library, category="Category One")
    assert len(found_books) == 1
    assert found_books[0].category == "Category One"

def test_search_books_no_criteria(sample_library):
    found_books = search_books(sample_library)
    assert len(found_books) == 2  # Returns all books when no criteria are given
