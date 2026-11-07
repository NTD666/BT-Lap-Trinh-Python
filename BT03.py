"""Câu 3: Tạo một danh sách rỗng, viết chương trình xử lý danh sách:
a. Nhập các phần tử số nguyên vào danh sách, ngưng khi người dùng nhập số 0.
   In danh sách vừa nhập.
b. Tính tổng các số dương chẵn có trong danh sách.
c. Đếm số lần xuất hiện của phần tử k có trong danh sách (k nhập từ bàn phím).
"""


def nhap_danh_sach() -> list[int]:
    """Nhập danh sách số nguyên, kết thúc khi nhập số 0."""
    danhsach: list[int] = []
    while True:
        x = int(input("Nhập phần tử (nhập 0 để kết thúc): "))
        if x == 0:
            break
        danhsach.append(x)
    return danhsach


def tong_duong_chan(danhsach: list[int]) -> int:
    """Tính tổng các số dương chẵn (> 0 và chia hết cho 2) trong danh sách."""
    tong = 0
    for i in danhsach:
        if i > 0 and i % 2 == 0:
            tong += i
    return tong


def dem_so_lan_xuat_hien(danhsach: list[int], k: int) -> int:
    """Đếm số lần xuất hiện của phần tử k trong danh sách."""
    dem = 0
    for i in danhsach:
        if i == k:
            dem += 1
    return dem


if __name__ == "__main__":
    # a. Nhập danh sách
    danhsach = nhap_danh_sach()
    print("Danh sách vừa nhập:", danhsach)

    # b. Tổng các số dương chẵn
    tong = tong_duong_chan(danhsach)
    if tong != 0:
        print("Tổng các số dương chẵn trong danh sách:", tong)
    else:
        print("Không có số dương chẵn trong danh sách.")

    # c. Đếm số lần xuất hiện của k
    k = int(input("Nhập k: "))
    dem_k = dem_so_lan_xuat_hien(danhsach, k)
    if dem_k == 0:
        print("Không có phần tử", k, "trong danh sách")
    else:
        print("Số lần xuất hiện của", k, "là:", dem_k)
