"""Câu 1: Viết chương trình nhập vào số nguyên dương n và thực hiện:
a. Kiểm tra giá trị n nếu ngoài đoạn [1;1500] thì yêu cầu nhập lại.
b. Viết hàm con đếm số lượng chữ số lẻ của số nguyên dương n.
   Ví dụ: n=635 -> 2 chữ số lẻ (3, 5).
c. Viết hàm con tính S = 1/2 + 1/4 + 1/6 + ... + 1/(2n).
"""


def DemChuSoLe(n: int) -> int:
    """Đếm số lượng chữ số lẻ của số nguyên dương n."""
    dem = 0
    n = abs(n)
    while n != 0:
        tam = n % 10
        if tam % 2 != 0:
            dem += 1
        n //= 10
    return dem


def S(n: int) -> float:
    """Tính S = 1/2 + 1/4 + 1/6 + ... + 1/(2n)."""
    s = 0.0
    for i in range(1, n + 1):
        s += 1 / (2 * i)
    return s


def nhap_n() -> int:
    """Nhập giá trị n trong đoạn [1; 1500], nếu ngoài đoạn thì yêu cầu nhập lại."""
    n = int(input("Nhập giá trị 1<=n<=1500: "))
    while n < 1 or n > 1500:
        n = int(input("Nhập giá trị 1<=n<=1500: "))
    return n


if __name__ == "__main__":
    # a. Kiểm tra n
    n = nhap_n()

    # b. Đếm số lượng chữ số lẻ
    print("Số lượng chữ số lẻ là: ", DemChuSoLe(n))

    # c. Tính tổng S
    print("S = ", S(n))