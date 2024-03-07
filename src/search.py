import logging
from .library import Library

logger = logging.getLogger(__name__)

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
