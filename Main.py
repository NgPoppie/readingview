# main.py

import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from book import Book
from bookcollection import BookCollection

# Load the Kivy file
Builder.load_file('bookapp.kv')

class MainWidget(BoxLayout):
    sort_spinner = ObjectProperty(None)
    add_button = ObjectProperty(None)
    clear_button = ObjectProperty(None)
    title_input = ObjectProperty(None)
    author_input = ObjectProperty(None)
    pages_input = ObjectProperty(None)
    book_list = ObjectProperty(None)
    status_label_top = ObjectProperty(None)
    status_label_bottom = ObjectProperty(None)

class BookApp(App):
    PADDING = 10
    SPACING = 10
    BUTTON_HEIGHT = 44
    COLOR_COMPLETED = (0.7, 0.7, 0.7, 1)  # Light grey for completed books
    COLOR_UNCOMPLETED = (1, 0.5, 0.5, 1)  # Light red for uncompleted books

    def build(self):
        self.title = 'Book Collection'
        self.book_collection = BookCollection()
        self.load_books()
        return MainWidget()

    def on_start(self):
        """Initialize the GUI components on start."""
        try:
            self.root.ids.sort_spinner.bind(text=self.sort_books)
            self.root.ids.add_button.bind(on_release=self.add_book)
            self.root.ids.clear_button.bind(on_release=self.clear_inputs)
            self.update_book_list()
        except Exception as e:
            print(f"Error in on_start: {e}")

    def load_books(self):
        """Load books from the JSON file."""
        try:
            self.book_collection.load_books('books.json')
        except FileNotFoundError:
            self.root.ids.status_label_bottom.text = 'No books.json file found. Starting with an empty collection.'
        except Exception as e:
            print(f"Error loading books: {e}")

    def save_books(self):
        """Save books to the JSON file."""
        try:
            self.book_collection.save_books('books.json')
        except Exception as e:
            print(f"Error saving books: {e}")

    def sort_books(self, spinner, text):
        """Sort the books based on the selected key."""
        self.book_collection.sort(text)
        self.update_book_list()

    def update_book_list(self):
        """Update the list of books displayed in the GUI."""
        try:
            self.root.ids.book_list.clear_widgets()
            for book in self.book_collection.books:
                book_button = Button(
                    text=str(book),
                    size_hint_y=None,
                    height=self.BUTTON_HEIGHT,
                    background_color=self.COLOR_COMPLETED if book.is_completed else self.COLOR_UNCOMPLETED
                )
                book_button.bind(on_release=self.toggle_book_status)
                self.root.ids.book_list.add_widget(book_button)
            self.root.ids.status_label_top.text = f'Pages to read: {self.book_collection.get_unread_pages()}'
        except Exception as e:
            print(f"Error updating book list: {e}")

    def toggle_book_status(self, instance):
        """Toggle the completion status of a book."""
        try:
            book = next(b for b in self.book_collection.books if str(b) == instance.text)
            if book.is_completed:
                book.mark_unread()
                self.root.ids.status_label_bottom.text = f'{book.title} marked as unread.'
            else:
                book.mark_completed()
                self.root.ids.status_label_bottom.text = f'{book.title} marked as completed. {"Wow, that was a long book!" if book.is_long() else ""}'
            self.update_book_list()
        except Exception as e:
            print(f"Error toggling book status: {e}")

    def add_book(self, instance):
        """Add a new book based on user input."""
        try:
            title = self.root.ids.title_input.text.strip()
            author = self.root.ids.author_input.text.strip()
            pages = self.root.ids.pages_input.text.strip()

            if not title or not author or not pages:
                self.root.ids.status_label_bottom.text = 'Please complete all fields.'
                return

            try:
                pages = int(pages)
            except ValueError:
                self.root.ids.status_label_bottom.text = 'Please enter a valid number.'
                return

            if pages <= 0:
                self.root.ids.status_label_bottom.text = 'The book must have some pages!'
                return

            new_book = Book(title, author, pages)
            self.book_collection.add_book(new_book)
            self.root.ids.status_label_bottom.text = f'Added {new_book.title}.'
            self.clear_inputs()
            self.update_book_list()
        except Exception as e:
            print(f"Error adding book: {e}")

    def clear_inputs(self, instance=None):
        """Clear the input fields and status label."""
        self.root.ids.title_input.text = ''
        self.root.ids.author_input.text = ''
        self.root.ids.pages_input.text = ''
        self.root.ids.status_label_bottom.text = ''

    def on_stop(self):
        """Save books when the application stops."""
        self.save_books()

if __name__ == '__main__':
    BookApp().run()
