class Book:
    """
    A class used to represent a Book in a library management system.

    Attributes
    ----------
    title : str
        the title of the book
    author : str
        the author of the book
    isbn : str
        the International Standard Book Number, a unique book identifier
    category : str
        the category or genre of the book

    Methods
    -------
    update_title(new_title)
        Updates the title of the book to new_title.

    update_author(new_author)
        Updates the author of the book to new_author.

    update_category(new_category)
        Updates the category of the book to new_category.

    get_details()
        Returns a dictionary of the book details.
    """

    def __init__(self, title, author, isbn, category):
        """
        Constructs all the necessary attributes for the book object.

        Parameters
        ----------
        title : str
            Title of the book.
        author : str
            Author of the book.
        isbn : str
            ISBN of the book. Must be a string of digits.
        category : str
            Category or genre of the book.
        """
        if not all(isinstance(arg, str) for arg in (title, author, isbn, category)):
            raise ValueError("All attributes must be of type 'str'.")
        if not isbn.isdigit():
            raise ValueError("ISBN must be a string of digits.")

        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category

    def __str__(self):
        """
        Returns a string representation of the book.
        """
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - Category: {self.category}"

    def __eq__(self, other):
        """
        Compares two book instances for equality based on their ISBN numbers.

        Parameters
        ----------
        other : Book
            The other book to compare with.

        Returns
        -------
        bool
            True if books have the same ISBN, False otherwise.
        """
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn

    def update_title(self, new_title):
        """
        Updates the title of the book.

        Parameters
        ----------
        new_title : str
            The new title of the book.
        """
        self.title = new_title

    def update_author(self, new_author):
        """
        Updates the author of the book.

        Parameters
        ----------
        new_author : str
            The new author of the book.
        """
        self.author = new_author

    def update_category(self, new_category):
        """
        Updates the category of the book.

        Parameters
        ----------
        new_category : str
            The new category of the book.
        """
        self.category = new_category

    def get_details(self):
        """
        Returns a dictionary of the book details.

        Returns
        -------
        dict
            A dictionary containing the book details.
        """
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'category': self.category
        }
