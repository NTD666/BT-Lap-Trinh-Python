# ĐỀ THI KẾT THÚC MÔN HỌC & ĐÁP ÁN CHI TIẾT

**TRƯỜNG CAO ĐẲNG CÔNG THƯƠNG TP.HCM**  
**KHOA: CÔNG NGHỆ THÔNG TIN** — **BỘ MÔN: CÔNG NGHỆ PHẦN MỀM**  
- **Môn thi:** Lập trình Python  
- **Mã môn học:** 229152 | **Số đvht/tín chỉ:** 02  
- **Mã đề thi:** 11301  
- **Hình thức thi:** Thực hành | **Thời gian:** 90 phút  
- **Quy cách nộp bài:** Folder `HOTEN_MSSV` chứa 5 file `.py` (`BT01.py` đến `BT05.py`)

---

## NỘI DUNG ĐỀ THI

### Câu 1 (2.0 điểm)
Viết chương trình nhập vào số nguyên dương $n$ và thực hiện các công việc sau:
- **a. (0.5đ)** Kiểm tra giá trị $n$ nếu ngoài đoạn $[1; 1500]$ thì yêu cầu nhập lại.
- **b. (0.75đ)** Viết hàm con đếm số lượng chữ số lẻ của số nguyên dương $n$.  
  *Ví dụ:* $n = 635$, số lượng chữ số lẻ của $n$ là $2$.
- **c. (0.75đ)** Viết hàm con tính $S = \frac{1}{2} + \frac{1}{4} + \frac{1}{6} + \dots + \frac{1}{2n}$.

### Câu 2 (2.0 điểm)
Viết chương trình nhập một chuỗi $s$ từ bàn phím và thực hiện các công việc sau:
- **a. (0.75đ)** Đếm số ký tự chữ hoa có trong chuỗi.
- **b. (0.5đ)** Kiểm tra xem chuỗi $s$ có đối xứng hay không.
- **c. (0.75đ)** Tính tổng các chữ số trong chuỗi.

### Câu 3 (2.0 điểm)
Tạo một danh sách rỗng, viết chương trình xử lý danh sách với các chức năng sau:
- **a. (0.75đ)** Nhập các phần tử số nguyên vào danh sách, ngưng khi người dùng nhập số $0$. In danh sách vừa nhập.
- **b. (0.75đ)** Tính tổng các số dương chẵn có trong danh sách.
- **c. (0.5đ)** Đếm số lần xuất hiện của phần tử $k$ có trong danh sách (với $k$ nhập từ bàn phím).

### Câu 4 (2.0 điểm)
Viết chương trình nhập thông tin của các cuốn sách trong thư viện và thực hiện các công việc sau:
- **a. (1.5đ)** Nhập thông tin gồm: Mã số sách, Tên sách, Tên tác giả, Nhà xuất bản, Năm xuất bản. Lưu các thông tin này trong một từ điển (năm xuất bản phải $\le$ năm hiện tại).
- **b. (0.5đ)** Nhập vào một Mã số sách từ bàn phím. Nếu tồn tại cuốn sách có mã số cần tìm thì tiến hành xóa cuốn sách này khỏi từ điển, ngược lại thông báo `"Không tìm thấy cuốn sách cần xóa"`.

### Câu 5 (2.0 điểm)
Tạo lớp có tên `DienThoai` với các yêu cầu sau:
- **a. (1.0đ)** Lớp `DienThoai` có các thuộc tính và phương thức:
  - Thuộc tính: `MaMay`, `TenMay`, `HangSanXuat`, `DungLuongPin`, `GiaBan`.
  - Phương thức:
    - Khởi tạo `__init__()`: khởi tạo thông tin cho `MaMay`, `TenMay`, `HangSanXuat`, `DungLuongPin`, `GiaBan`.
    - `thongtindienthoai()`: dùng để hiển thị thông tin của `MaMay`, `TenMay`, `HangSanXuat`, `DungLuongPin`, `GiaBan`.
- **b. (1.0đ)** Tạo 2 đối tượng:
  - `DT01`: ("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
  - `DT02`: ("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)  
  và thực thi phương thức `thongtindienthoai()`. In kết quả ra màn hình.
