# Library Management System

Ứng dụng quản lý thư viện chạy trên terminal, xây dựng bằng Python thuần và OOP.

## Chức năng

- Thêm sách
- Hiển thị danh sách sách
- Tìm kiếm sách theo tên
- Xóa sách
- Mượn / trả sách
- Sắp xếp theo tên hoặc năm xuất bản

## Cấu trúc dữ liệu & giải thuật

- `List` để lưu danh sách các đối tượng `Book`
- Linear Search để tìm sách theo tên
- `enumerate()` + `pop(index)` để xóa theo ID
- Bubble Sort để sắp xếp theo tên và năm
- Insertion Sort để sắp xếp theo năm

## Độ phức tạp

- Linear Search: `O(n)`
- Bubble Sort: `O(n²)` worst/average; bản triển khai hiện tại chưa có early-exit nên best case vẫn chạy theo hai vòng lặp
- Insertion Sort: `O(n)` best, `O(n²)` average/worst
- List access by index: `O(1)`

## Chạy chương trình

Yêu cầu Python 3.10+.

```bash
python main.py
```

Không yêu cầu thư viện bên ngoài.
