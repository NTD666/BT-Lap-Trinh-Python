"""Câu 2: Viết chương trình nhập một chuỗi s từ bàn phím và thực hiện:
a. Đếm số ký tự chữ hoa có trong chuỗi.
b. Kiểm tra xem chuỗi s có đối xứng hay không.
c. Tính tổng các chữ số trong chuỗi.
"""


def dem_chu_hoa(s: str) -> int:
    """Đếm số lượng ký tự in hoa trong chuỗi s."""
    dem = 0
    for ch in s:
        if ch.isupper():
            dem += 1
    return dem


def doi_xung(s: str) -> bool:
    """Kiểm tra xem chuỗi s có đối xứng (palindrome) hay không."""
    return s == s[::-1]


def DoiXung(s: str) -> None:
    """Hiển thị kết quả kiểm tra đối xứng theo đúng định dạng đề thi."""
    if doi_xung(s):
        print("Chuỗi đối xứng.")
    else:
        print("Chuỗi không đối xứng.")


def tong_chu_so(s: str) -> int:
    """Tính tổng các ký tự chữ số xuất hiện trong chuỗi s."""
    tong = 0
    for ch in s:
        if ch.isdigit():
            tong += int(ch)
    return tong


if __name__ == "__main__":
    s = input("Nhập chuỗi s: ")

    # a. Đếm chữ hoa
    so_chu_hoa = dem_chu_hoa(s)
    if so_chu_hoa == 0:
        print("Chuỗi không có ký tự chữ hoa.")
    else:
        print("Số ký tự chữ hoa: ", so_chu_hoa)

    # b. Kiểm tra đối xứng
    DoiXung(s)

    # c. Tính tổng các chữ số
    print("Tổng các chữ số trong chuỗi: ", tong_chu_so(s))
