from random import randint


class Book:
    CURRENT_YEAR = 2026
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def get_age(self):
        return self.CURRENT_YEAR - self.year_published

    @classmethod
    def get_random_book(cls):
        book = cls(f"book_{randint(1, 10)}", f"author_{randint(1, 10)}",
                    randint(0, 2024))
        return book

    @staticmethod
    def get_classic(book):
        return book.year_published < 1950

    def __str__(self):
        return f"title: {self.title}, author: {self.author}, year: {self.year_published}"

print(Book.CURRENT_YEAR)
book = Book("book 1", "author 1", 2001)
print(book.get_age())
book.year_published = 1900

random_book = Book.get_random_book()
print(random_book.get_age())
print(random_book)

print(Book.get_classic(book))
print(Book.get_classic(random_book))

random_book_1 = book.get_random_book()
print(random_book_1)

print(isinstance(book, Book))

del book.year_published
