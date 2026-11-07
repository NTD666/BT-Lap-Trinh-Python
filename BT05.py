"""Câu 5: Lập trình hướng đối tượng (OOP) với lớp DienThoai:
a. Lớp DienThoai:
   - Thuộc tính: MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan.
   - Phương thức:
     + __init__(): khởi tạo thông tin cho các thuộc tính trên.
     + thongtindienthoai(): hiển thị thông tin chi tiết của điện thoại.
b. Tạo 2 đối tượng:
   - DT01: iPhone 15 Pro, Apple, 3274 mAh, 28,990,000 VND
   - DT02: Galaxy S24 Ultra, Samsung, 5000 mAh, 29,990,000 VND
   và gọi phương thức thongtindienthoai().
"""


class DienThoai:
    def __init__(
        self,
        MaMay: str,
        TenMay: str,
        HangSanXuat: str,
        DungLuongPin: int,
        GiaBan: int | float,
    ) -> None:
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self) -> None:
        print("Mã máy:", self.MaMay)
        print("Tên máy:", self.TenMay)
        print("Hãng sản xuất:", self.HangSanXuat)
        print("Dung lượng pin:", self.DungLuongPin)
        print("Giá bán:", self.GiaBan)


if __name__ == "__main__":
    # b. Khởi tạo 2 đối tượng mẫu theo đề bài
    DT1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    DT2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    print("--- THÔNG TIN ĐIỆN THOẠI 1 ---")
    DT1.thongtindienthoai()

    print("\n--- THÔNG TIN ĐIỆN THOẠI 2 ---")
    DT2.thongtindienthoai()
