# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, title, author):
        new_book = Book(title, author)
        self._books.append(new_book)
        print(f"Added '{title}' by {author}")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"Checked out '{title}'")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print("Book not found.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"Returned '{title}'")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print("Book not found.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
