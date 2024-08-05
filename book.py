class Book:
    def __init__(self, title="", author="", number_of_pages=0, is_completed=False):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.is_completed = is_completed

    def __str__(self):
        return f"{self.title} by {self.author}, {self.number_of_pages} pages, {'completed' if self.is_completed else 'not completed'}"

    def mark_completed(self):
        self.is_completed = True

    def mark_unread(self):
        self.is_completed = False

    def is_long(self):
        return self.number_of_pages >= 500

