from book import Book

def run_tests():
    """Test Book class."""

    # Test empty book with defaults
    print("Test empty book:")
    default_book = Book()
    print(default_book)
    assert default_book.title == ""
    assert default_book.author == ""
    assert default_book.number_of_pages == 0
    assert not default_book.is_completed

    # Test initial-value book
    print("Test initial-value book:")
    new_book = Book("Fish Fingers", "Dory", 501, True)
    print(new_book)
    assert new_book.title == "Fish Fingers"
    assert new_book.author == "Dory"
    assert new_book.number_of_pages == 501
    assert new_book.is_completed

    # Test mark_unread()
    print("Test mark_unread():")
    new_book.mark_unread()
    print(new_book)
    assert not new_book.is_completed

    # Test mark_completed()
    print("Test mark_completed():")
    new_book.mark_completed()
    print(new_book)
    assert new_book.is_completed

    # Test is_long()
    print("Test is_long():")
    assert new_book.is_long()  # Should be True for 501 pages
    short_book = Book("Short Story", "Author", 100)
    assert not short_book.is_long()  # Should be False for 100 pages

    # Additional tests
    print("Test additional book:")
    another_book = Book("1984", "George Orwell", 328, False)
    print(another_book)
    assert another_book.title == "1984"
    assert another_book.author == "George Orwell"
    assert another_book.number_of_pages == 328
    assert not another_book.is_completed

run_tests()

