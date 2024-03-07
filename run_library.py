import logging
from src.library import Library
from src.utilities import load_library_from_file, save_library_to_file
from src.config import DATA_FILE_PATH, LOGGING_LEVEL
from src.search import search_books

def configure_logging():
    """Configures the logging settings for the application."""
    logging_level = getattr(logging, LOGGING_LEVEL.upper(), None)
    if not isinstance(logging_level, int):
        raise ValueError(f'Invalid log level: {LOGGING_LEVEL}')
    logging.basicConfig(level=logging_level)

def prompt_for_title():
    """Prompts the user to enter a book title for searching."""
    return input("Please enter the book title to search for: ")

def main(data_file_path):
    """Runs the main application logic with user interaction."""
    logging.info("Starting the library application...")
    library = Library()

    try:
        load_library_from_file(library, data_file_path)
        logging.info(f"Loaded {len(library.get_all_books())} books into the library.")

        # Prompt the user for a title to search
        search_title = prompt_for_title()
        found_books = search_books(library, title=search_title)
        if found_books:
            logging.info(f"Books found with title '{search_title}':")
            for book in found_books:
                logging.info(book)
        else:
            logging.info(f"No books found with title '{search_title}'.")

        save_library_to_file(library, data_file_path)

    except IOError as e:
        logging.error(f"File operation error occurred: {e}", exc_info=True)
    except ValueError as e:
        logging.error(f"Value error: {e}", exc_info=True)
    except Exception as e:
        logging.exception("An unexpected error occurred.")

    logging.info("Library application has completed running.")

if __name__ == '__main__':
    configure_logging()
    main(DATA_FILE_PATH)
