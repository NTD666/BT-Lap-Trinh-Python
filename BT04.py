"""Câu 4: Quản lý thông tin sách trong thư viện bằng từ điển (Dictionary):
a. Nhập thông tin: Mã số sách, Tên sách, Tên tác giả, Nhà xuất bản, Năm xuất bản.
   Lưu thông tin trong từ điển: tudien[MaSoSach] = [TenSach, TenTacGia, NhaXuatBan, NamXuatBan].
   Năm xuất bản phải <= năm hiện tại.
b. Nhập Mã số sách cần xóa. Xóa khỏi từ điển nếu tồn tại, ngược lại báo:
   "Không tìm thấy cuốn sách cần xóa".
"""

from datetime import datetime


def them_sach(
    tudien: dict,
    ma_so: str,
    ten_sach: str,
    ten_tac_gia: str,
    nha_xuat_ban: str,
    nam_xuat_ban: int,
) -> bool:
    """Thêm một cuốn sách vào từ điển nếu năm xuất bản hợp lệ."""
    nam_hien_tai = datetime.now().year
    if nam_xuat_ban > nam_hien_tai:
        return False
    tudien[ma_so] = [ten_sach, ten_tac_gia, nha_xuat_ban, nam_xuat_ban]
    return True


def xoa_sach(tudien: dict, ma_so: str) -> bool:
    """Xóa sách khỏi từ điển theo mã sách. Trả về True nếu xóa thành công, False nếu không tìm thấy."""
    if ma_so in tudien:
        del tudien[ma_so]
        return True
    return False


def nhap_thong_tin_sach() -> dict:
    """Nhập thông tin n cuốn sách từ bàn phím."""
    nam_hien_tai = datetime.now().year
    n = int(input("Nhập số lượng sách (n>0): "))
    while n <= 0:
        n = int(input("Nhập số lượng sách (n>0): "))

    tudien = {}
    for i in range(n):
        print(f"\n--- Nhập thông tin cuốn sách thứ {i + 1} ---")
        ma_so = input("Nhập mã số sách: ")
        ten_sach = input("Nhập tên sách: ")
        tac_gia = input("Nhập tên tác giả: ")
        nxb = input("Nhập nhà xuất bản: ")
        nam_xb = int(input("Nhập năm xuất bản: "))
        while nam_xb > nam_hien_tai:
            nam_xb = int(
                input(
                    f"Năm xuất bản không hợp lệ, vui lòng nhập năm <= {nam_hien_tai}: "
                )
            )
        them_sach(tudien, ma_so, ten_sach, tac_gia, nxb, nam_xb)

    return tudien


if __name__ == "__main__":
    # a. Nhập thông tin sách
    tudien = nhap_thong_tin_sach()
    print("\nTừ điển sách hiện có:")
    print(tudien)

    # b. Xóa cuốn sách theo mã
    x = input("\nNhập mã số sách cần xóa: ")
    if xoa_sach(tudien, x):
        print(f"Cuốn sách có mã số {x} đã được xóa.")
    else:
        print("Không tìm thấy cuốn sách cần xóa.")

    print("Từ điển sách sau khi xử lý:")
    print(tudien)
