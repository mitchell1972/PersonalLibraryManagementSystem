# src/__init__.py

# Import the core classes into the package namespace so they can be
# conveniently imported from the package.

from .book import Book
from .library import Library
from .utilities import save_library_to_file, load_library_from_file

# Define an __all__ for import * (though it's not a recommended practice)
__all__ = ['Book', 'Library', 'save_library_to_file', 'load_library_from_file']
