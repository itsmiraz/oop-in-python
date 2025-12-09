# Aggregation = Represents a relationship where one object (the whole ) contains reference to one or more independent objects (the parts)


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


library = Library('New work library ')

book1 = Book('Harry potter', 'Miraj hossen')
book2 = Book('Hobbit', 'JRR TOLKEN')
book3 = Book('Color of magic', ' Terry petrick')


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


# print()

# print(library.list_books())
for book in library.list_books():
    print(book)
