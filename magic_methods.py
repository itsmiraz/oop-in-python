# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__ they are automatically called by many of python's built-in operations
#   they allow developers to define or customize the behavior of objects


class Book:
    def __init__(self, title, author, num_page):
        self.title = title
        self.author = author
        self.num_page = num_page

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_page < other.num_page

    def __gt__(self, other):
        return self.num_page > other.num_page

    def __add__(self, other):
        return self.num_page + other.num_page

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title

        elif key == 'author':
            return self.author
        else:
            return f"Key '{key}' was not found"


book1 = Book('38 Laws', 'Miraj Hossen', 248)
book2 = Book('38 Laws', 'Miraj Hossen', 2248)
book3 = Book('THe lion the watch', 'JK ROWLING', 224)

# print(book1)


# print("Miraj" in book2)
print(book1['audio'])

# print(book1 == book2)
# print(book2 + book3)
