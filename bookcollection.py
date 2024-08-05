import json
from book import Book


class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_unread_pages(self):
        return sum(book.number_of_pages for book in self.books if not book.is_completed)

    def get_completed_pages(self):
        return sum(book.number_of_pages for book in self.books if book.is_completed)

    def load_books(self, filename):
        with open(filename, 'r') as file:
            books_data = json.load(file)
            self.books = [Book(**data) for data in books_data]

    def save_books(self, filename):
        with open(filename, 'w') as file:
            books_data = [book.__dict__ for book in self.books]
            json.dump(books_data, file, indent=4)

    def sort(self, key):
        self.books.sort(key=lambda book: (getattr(book, key), book.title))

