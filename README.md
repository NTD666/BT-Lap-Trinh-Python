# Ôn Luyện Đề Thi Lập Trình Python 🐍

> **Bộ bài tập thực hành & kiểm thử tự động chuẩn hóa từ Đề thi kết thúc môn Lập trình Python (Mã môn: 229152 - Mã đề: 11301).**

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Pytest](https://img.shields.io/badge/Tested%20with-pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)](https://pytest.org)
[![Code Style: Ruff](https://img.shields.io/badge/Code%20Style-Ruff-black?style=flat-square)](https://github.com/astral-sh/ruff)

**Learning Loop:** `Đọc đề → Viết hàm → Chạy thử → Test tự động với pytest → Chuẩn hóa mã`

---

## Danh mục bài tập (Ma trận đề thi)

Toàn bộ đề thi gồm **5 câu (thang điểm 10)**, được thiết kế thành các file độc lập từ `BT01.py` đến `BT05.py`:

| Bài | Tên file | Chủ đề / Kỹ năng chính | Điểm | File kiểm thử tự động |
|:---|:---|:---|:---:|:---|
| **Câu 1** | [`BT01.py`](BT01.py) | Vòng lặp `while`, kiểm tra khoảng $[1; 1500]$, hàm đếm chữ số lẻ, tính tổng cấp số $S(n)$ | 2.0đ | [`tests/test_all.py`](tests/test_all.py) (`TestBT01`) |
| **Câu 2** | [`BT02.py`](BT02.py) | Xử lý chuỗi ký tự (`str`), đếm chữ hoa, kiểm tra palindrome đối xứng, tính tổng chữ số | 2.0đ | [`tests/test_all.py`](tests/test_all.py) (`TestBT02`) |
| **Câu 3** | [`BT03.py`](BT03.py) | Danh sách (`list`), nhập động dừng tại 0, lọc tổng số dương chẵn, đếm tần suất xuất hiện $k$ | 2.0đ | [`tests/test_all.py`](tests/test_all.py) (`TestBT03`) |
| **Câu 4** | [`BT04.py`](BT04.py) | Từ điển (`dict`), thư viện sách, kiểm tra năm xuất bản $\le$ năm hiện tại, xóa phần tử theo key | 2.0đ | [`tests/test_all.py`](tests/test_all.py) (`TestBT04`) |
| **Câu 5** | [`BT05.py`](BT05.py) | Lập trình hướng đối tượng (`OOP`), `class DienThoai`, thuộc tính, hàm khởi tạo `__init__`, phương thức hiển thị | 2.0đ | [`tests/test_all.py`](tests/test_all.py) (`TestBT05`) |

> 📄 Xem toàn văn đề thi gốc và đáp án tại: [`DE_THI.md`](DE_THI.md) hoặc file gốc [`Lập trình Python (229152)_ca7h30, 22-7.pdf`](Lập%20trình%20Python%20%28229152%29_ca7h30,%2022-7.pdf).

---

## Cấu trúc thư mục

```text
BT_2_de_thi/
├── .gitignore             # Quy tắc bỏ qua cache, file tạm
├── .python-version        # Phiên bản Python khuyến nghị (>= 3.12)
├── pyproject.toml         # Cấu hình pytest và ruff
├── README.md              # Tài liệu hướng dẫn chính
├── SETUP.md               # Hướng dẫn thiết lập môi trường
├── DE_THI.md              # Toàn văn đề thi & đáp án biểu điểm
├── cham_diem.py           # Script chấm điểm tự động theo thang 10
├── BT01.py                # Mã nguồn bài 1
├── BT02.py                # Mã nguồn bài 2
├── BT03.py                # Mã nguồn bài 3
├── BT04.py                # Mã nguồn bài 4
├── BT05.py                # Mã nguồn bài 5
└── tests/                 # Thư mục kiểm thử tự động duy nhất
    ├── __init__.py
    ├── conftest.py
    └── test_all.py        # Toàn bộ 28 bài test cho cả 5 câu (BT01 -> BT05)
```


---

## Hướng dẫn chạy & kiểm thử

### 1. Chấm điểm tự động toàn bài thi (Theo thang điểm 10 của đề thi)
```powershell
python cham_diem.py
```
> Hệ thống sẽ tự động chạy toàn bộ các bài test, tính điểm chi tiết cho từng ý (1a, 1b, 1c... đến 5b) và xuất ra bảng điểm tổng kết cùng xếp loại.

### 2. Chạy trực tiếp từng bài tương tác qua bàn phím
```powershell
python BT01.py
python BT02.py
python BT03.py
python BT04.py
python BT05.py
```

### 3. Chạy kiểm thử tự động với Pytest
```powershell
pytest
```

Chạy có hiển thị chi tiết từng test case:
```powershell
pytest -v
```

### 3. Kiểm tra định dạng code (Ruff)
```powershell
ruff check .
```
