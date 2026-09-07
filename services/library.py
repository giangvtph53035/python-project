from models.book import Book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> bool:
        """Add a book if its ID is not already in the library."""
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                return False

        self.books.append(book)
        return True

    def show_books(self) -> None:
        if not self.books:
            print("Thư viện chưa có sách.")
            return

        print("\n===== DANH SÁCH SÁCH =====")
        for book in self.books:
            print(book)

    def search_book(self, title: str):
        """Linear Search by a case-insensitive title keyword."""
        for book in self.books:
            if title.lower() in book.title.lower():
                return book
        return None

    def remove_book(self, book_id: int) -> bool:
        """Find the real list index with enumerate, then remove it with pop."""
        for i, book in enumerate(self.books):
            if book.book_id == book_id:
                self.books.pop(i)
                return True
        return False

    def borrow_book(self, book_id: int):
        """True = success, False = already borrowed, None = not found."""
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    return True
                return False
        return None

    def return_book(self, book_id: int):
        """True = success, False = already available, None = not found."""
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    return True
                return False
        return None

    def sort_by_year_bubble(self) -> None:
        """Bubble Sort by publication year in ascending order."""
        for i in range(len(self.books)):
            for j in range(len(self.books) - 1 - i):
                if self.books[j].year > self.books[j + 1].year:
                    self.books[j], self.books[j + 1] = (
                        self.books[j + 1],
                        self.books[j],
                    )

    def sort_by_title_bubble(self) -> None:
        """Bubble Sort by title in ascending alphabetical order."""
        for i in range(len(self.books)):
            for j in range(len(self.books) - 1 - i):
                if self.books[j].title.lower() > self.books[j + 1].title.lower():
                    self.books[j], self.books[j + 1] = (
                        self.books[j + 1],
                        self.books[j],
                    )

    def sort_by_year_insertion(self) -> None:
        """Insertion Sort by publication year in ascending order."""
        for i in range(1, len(self.books)):
            key = self.books[i]
            j = i - 1

            while j >= 0 and self.books[j].year > key.year:
                self.books[j + 1] = self.books[j]
                j -= 1

            self.books[j + 1] = key
