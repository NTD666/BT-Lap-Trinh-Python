# Hướng Dẫn Cài Đặt & Sử Dụng (SETUP.md)

Tài liệu hướng dẫn thiết lập môi trường Python và các công cụ kiểm thử cho bộ bài tập đề thi.

## 1. Yêu cầu tiên quyết
- Python phiên bản `>= 3.12`.
- Kiểm tra phiên bản Python hiện tại trong terminal:
  ```powershell
  python --version
  ```

## 2. Tạo môi trường ảo (Khuyến nghị)

Trong thư mục `BT_2_de_thi`, tạo và kích hoạt virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

## 3. Cài đặt công cụ kiểm thử (pytest & ruff)

Cài đặt các gói phụ thuộc dùng cho kiểm thử:
```powershell
python -m pip install --upgrade pip
pip install pytest ruff
```

## 4. Chạy kiểm thử & Chấm điểm tự động

- **Chấm điểm tự động theo thang điểm 10 của đề thi:**
  ```powershell
  python cham_diem.py
  ```
- Chạy nhanh tất cả các bài kiểm tra bằng pytest:
  ```powershell
  pytest
  ```
- Chạy chi tiết từng test trong file kiểm thử tổng hợp:
  ```powershell
  pytest -v tests/test_all.py
  ```


## 5. Kiểm tra chất lượng mã (Linting)

Sử dụng `ruff` để đảm bảo mã nguồn tuân thủ phong cách lập trình Python:
```powershell
ruff check .
```
Tự động sửa các lỗi format cơ bản:
```powershell
ruff check --fix .
```
