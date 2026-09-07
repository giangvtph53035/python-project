class Book:
    def __init__(self, book_id, title, author, year, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        status = "Có sẵn" if self.available else "Đang mượn"
        return (
            f"[{self.book_id}] {self.title} - {self.author} "
            f"({self.year}) - {status}"
        )
