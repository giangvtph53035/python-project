class Book:
    def __init__(self, book_id, tensach, tacgia, nam, trangthai=True):
        self.book_id = book_id
        self.tensach = tensach
        self.tacgia = tacgia
        self.nam = nam
        self.trangthai = trangthai
        
    def __str__(self):
        if self.trangthai:
            status = "Có sẵn"
        else:
            status = "Đã có người mượn"
        
        return f"{self.tensach}\n{self.tacgia}\n{self.nam}\n{status}"
    
book1 = Book(1, "Doraemon", "Fujiko F. Fujio", 2020, False)

book2 = Book(2, "Dragon Ball", "Akira Toriyama", 2021, True)
print(book1)
print(book2)

books = []
books.append(book1)
books.append(book2)

for book in books:
    print(book)