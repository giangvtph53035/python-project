import time


class Book:
    def __init__(self, book_id, title, author, year, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        if self.available:
            status = "Có sẵn"
        else:
            status = "Đang mượn"

        return f"{self.title}\n{self.author}\n{self.year}\n{status}"


book1 = Book(1, "Doraemon", "Fujiko F. Fujio", 2020, False)

book2 = Book(2, "Dragon Ball", "Akira Toriyama", 2021, True)
# print(book2)

books = []

book3 = Book(3, "Jujutsu Kaisen", "Gege Akutami", 2022, False)

book4 = Book(4, "Naruto", "Masashi Kishimoto", 2025, True)

book5 = Book(5, "One Piece", "Eiichiro Oda", 1997, True)

books.append(book3)
books.append(book4)

# for book in books:
#     print(book)


class Library:
    def __init__(self):
        self.books = []

    def show_books(self):
        for book in self.books:
            print(book)

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                return book
        return None

    def remove_book(self, book_id):
        for i, book in enumerate(self.books):
            if book.book_id == book_id:
                self.books.pop(i)
                return True
        return False

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    return True
                else:
                    return False
        return None

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    return True
                else:
                    return False
        return None

    def sort_by_year(self):
        for i in range(len(self.books)):
            for j in range(len(self.books) - 1 - i):
                if self.books[j].year > self.books[j + 1].year:
                    self.books[j], self.books[j + 1] = self.books[j + 1], self.books[j]

    def sort_by_title(self):
        for i in range(len(self.books)):
            for j in range(len(self.books) - 1 - i):
                if self.books[j].title > self.books[j + 1].title:
                    self.books[j], self.books[j + 1] = self.books[j + 1], self.books[j]

    def sort_by_year_insertion(self):
        for i in range(1, len(self.books)):
            key = self.books[i]
            j = i - 1
            while j >= 0 and self.books[j].year > key.year:
                self.books[j + 1] = self.books[j]
                j -= 1
            self.books[j + 1] = key

library = Library()

print(library.books)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
# library.show_books()

# print(library.search_book("Do"))


# print(library.remove_book(3))

# library.show_books()

# print(library.remove_book(99))

print(library.borrow_book(1))
print(library.borrow_book(1))
print(library.borrow_book(99))

# library.show_books()

# result = library.return_book(1)

# if result is True:
#     print("Trả sách thành công")
# elif result is False:
#     print("Trả sách thất bại: sách đang có sẵn")
# else:
#     print("Không tìm thấy sách")

library.show_books()

print("----- SAU KHI SORT -----")

library.sort_by_year()
library.sort_by_title()

library.show_books()
