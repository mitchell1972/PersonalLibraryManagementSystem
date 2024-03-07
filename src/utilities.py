import json
from .library import Library
from .book import Book

def save_library_to_file(library, filepath):
    """Saves the library's current state to a JSON file."""
    try:
        with open(filepath, 'w') as file:
            # Convert library to a list of dicts to prepare for JSON serialization
            json.dump([book.get_details() for book in library.get_all_books()], file)
    except IOError as e:
        raise IOError(f"Failed to save library data: {e}")

def load_library_from_file(library, filepath):
    """Loads the library's state from a JSON file."""
    try:
        with open(filepath, 'r') as file:
            books_data = json.load(file)
            for book_data in books_data:
                book = Book(**book_data)
                library.add_book(book)
    except IOError as e:
        raise IOError(f"Failed to load library data: {e}")

def search_books(library, title=None, author=None, category=None):
    """Searches for books in the library matching the given criteria."""
    # All criteria are optional and can be combined
    books = library.get_all_books()
    if title:
        books = [book for book in books if book.title == title]
    if author:
        books = [book for book in books if book.author == author]
    if category:
        books = [book for book in books if book.category == category]
    return books
