from models.book import Book
from services.library import Library


def print_result(result, success_message, false_message, none_message):
    if result is True:
        print(success_message)
    elif result is False:
        print(false_message)
    else:
        print(none_message)


def seed_library() -> Library:
    """Create sample data so the project can be tested immediately."""
    library = Library()

    sample_books = [
        Book(1, "Doraemon", "Fujiko F. Fujio", 2020, False),
        Book(2, "Dragon Ball", "Akira Toriyama", 2021, True),
        Book(3, "Jujutsu Kaisen", "Gege Akutami", 2022, False),
        Book(4, "Naruto", "Masashi Kishimoto", 2025, True),
        Book(5, "One Piece", "Eiichiro Oda", 1997, True),
    ]

    for book in sample_books:
        library.add_book(book)

    return library


def show_menu() -> None:
    print("\n" + "=" * 42)
    print("        LIBRARY MANAGEMENT SYSTEM")
    print("=" * 42)
    print("1. Hiển thị tất cả sách")
    print("2. Thêm sách")
    print("3. Tìm kiếm sách")
    print("4. Xóa sách")
    print("5. Mượn sách")
    print("6. Trả sách")
    print("7. Sắp xếp theo năm - Bubble Sort")
    print("8. Sắp xếp theo tên - Bubble Sort")
    print("9. Sắp xếp theo năm - Insertion Sort")
    print("0. Thoát")
    print("=" * 42)


def add_book_from_input(library: Library) -> None:
    try:
        book_id = int(input("ID sách: "))
        title = input("Tên sách: ").strip()
        author = input("Tác giả: ").strip()
        year = int(input("Năm xuất bản: "))
    except ValueError:
        print("ID và năm xuất bản phải là số.")
        return

    if not title or not author:
        print("Tên sách và tác giả không được để trống.")
        return

    if library.add_book(Book(book_id, title, author, year)):
        print("Thêm sách thành công")
    else:
        print("Thêm sách thất bại: ID đã tồn tại")


def main() -> None:
    library = seed_library()

    while True:
        show_menu()
        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            library.show_books()

        elif choice == "2":
            add_book_from_input(library)

        elif choice == "3":
            keyword = input("Nhập tên sách cần tìm: ").strip()
            book = library.search_book(keyword)
            if book is not None:
                print("\nKết quả:")
                print(book)
            else:
                print("Không tìm thấy sách")

        elif choice == "4":
            try:
                book_id = int(input("Nhập ID sách cần xóa: "))
            except ValueError:
                print("ID phải là số.")
                continue

            result = library.remove_book(book_id)
            print_result(
                result,
                "Xóa sách thành công",
                "Không tìm thấy sách",
                "Không tìm thấy sách",
            )

        elif choice == "5":
            try:
                book_id = int(input("Nhập ID sách muốn mượn: "))
            except ValueError:
                print("ID phải là số.")
                continue

            result = library.borrow_book(book_id)
            print_result(
                result,
                "Mượn sách thành công",
                "Mượn thất bại: sách đang được mượn",
                "Không tìm thấy sách",
            )

        elif choice == "6":
            try:
                book_id = int(input("Nhập ID sách muốn trả: "))
            except ValueError:
                print("ID phải là số.")
                continue

            result = library.return_book(book_id)
            print_result(
                result,
                "Trả sách thành công",
                "Trả thất bại: sách đang có sẵn",
                "Không tìm thấy sách",
            )

        elif choice == "7":
            library.sort_by_year_bubble()
            print("Đã sắp xếp theo năm bằng Bubble Sort")
            library.show_books()

        elif choice == "8":
            library.sort_by_title_bubble()
            print("Đã sắp xếp theo tên bằng Bubble Sort")
            library.show_books()

        elif choice == "9":
            library.sort_by_year_insertion()
            print("Đã sắp xếp theo năm bằng Insertion Sort")
            library.show_books()

        elif choice == "0":
            print("Đã thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
