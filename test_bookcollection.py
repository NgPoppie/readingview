from book import Book
from bookcollection import BookCollection

def run_tests():
    """Test BookCollection class."""

    # Test empty BookCollection with defaults
    print("Test empty BookCollection:")
    book_collection = BookCollection()
    print(book_collection.books)
    assert not book_collection.books  # This list should evaluate to False since it is empty

    # Test adding a new Book with values
    print("Test adding new book:")
    book_collection.add_book(Book("War and Peace", "William Shakespeare", 999, False))
    print(book_collection.books)
    assert len(book_collection.books) == 1

    # Test get_unread_pages()
    print("Test get_unread_pages():")
    unread_pages = book_collection.get_unread_pages()
    print(f"Unread pages: {unread_pages}")
    assert unread_pages == 999

    # Test get_completed_pages()
    print("Test get_completed_pages():")
    completed_pages = book_collection.get_completed_pages()
    print(f"Completed pages: {completed_pages}")
    assert completed_pages == 0

    # Test loading books (Assuming you have 'books.json' with appropriate data)
    print("Test loading books:")
    book_collection.load_books('books.json')
    print(book_collection.books)
    assert book_collection.books  # assuming data file is non-empty, list evaluates to True

    # Test saving books
    print("Test saving books:")
    book_collection.save_books('test_books.json')
    # Manually check 'test_books.json' for expected content

    # Test sorting books by author
    print("Test sorting - author:")
    book_collection.sort("author")
    print([book.author for book in book_collection.books])

    # Test sorting books by title
    print("Test sorting - title:")
    book_collection.sort("title")
    print([book.title for book in book_collection.books])

run_tests()

