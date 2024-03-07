from src import Book


class Library:
    """
    Represents a collection of books and provides management functions.
    """

    def __init__(self):
        """Initialize an empty library."""
        self._books = {}

    def add_book(self, book):
        """Add a Book object to the library."""
        if not isinstance(book, Book):
            raise ValueError("Must add a Book instance")
        self._books[book.isbn] = book

    def remove_book(self, isbn):
        """Remove a book from the library by ISBN."""
        return self._books.pop(isbn, None)

    def get_book_by_isbn(self, isbn):
        """Retrieve a book by its ISBN."""
        return self._books.get(isbn)

    def get_books_by_author(self, author):
        """Retrieve books by the same author."""
        return [book for book in self._books.values() if book.author == author]

    def get_books_by_category(self, category):
        """Retrieve books by a specific category."""
        return [book for book in self._books.values() if book.category == category]

    def get_all_books(self):
        """Retrieve a list of all the books in the library."""
        return list(self._books.values())

    def get_number_of_books(self):
        """Get the total count of books in the library."""
        return len(self._books)

    def __str__(self):
        """Provide a string representation of the library's collection."""
        return f"Library with {len(self._books)} books"

    def __contains__(self, isbn):
        """Check if a book with given ISBN is in the library."""
        return isbn in self._books
