"""Bộ kiểm thử tổng hợp toàn bộ Đề thi Lập trình Python (Mã đề: 11301).

Bao gồm 28 test cases kiểm thử tự động cho cả 5 câu (BT01 -> BT05):
- Câu 1: Kiểm tra khoảng n, đếm chữ số lẻ, tính tổng S
- Câu 2: Xử lý chuỗi (chữ hoa, đối xứng, tổng các chữ số)
- Câu 3: Xử lý danh sách (dừng tại 0, tổng chẵn dương, đếm k)
- Câu 4: Quản lý từ điển sách thư viện (thêm, xóa theo mã)
- Câu 5: Lập trình OOP - Lớp DienThoai
"""

from datetime import datetime
import pytest

from BT01 import DemChuSoLe, S, nhap_n
from BT02 import DoiXung, dem_chu_hoa, doi_xung, tong_chu_so
from BT03 import dem_so_lan_xuat_hien, nhap_danh_sach, tong_duong_chan
from BT04 import them_sach, xoa_sach
from BT05 import DienThoai


# ==============================================================================
# CÂU 1 (2.0 điểm): Xử lý số nguyên dương n
# ==============================================================================
class TestBT01:
    def test_dem_chu_so_le_mau_de_thi(self):
        """Ví dụ đề thi: n=635 có 2 chữ số lẻ (3 và 5)."""
        assert DemChuSoLe(635) == 2

    def test_dem_chu_so_le_toan_chan(self):
        """Số toàn chữ số chẵn trả về 0."""
        assert DemChuSoLe(2468) == 0

    def test_dem_chu_so_le_toan_le(self):
        """Số toàn chữ số lẻ."""
        assert DemChuSoLe(13579) == 5

    def test_dem_chu_so_le_so_don(self):
        """Số có 1 chữ số."""
        assert DemChuSoLe(7) == 1
        assert DemChuSoLe(8) == 0

    def test_tong_s_n1(self):
        """S(1) = 1/(2*1) = 0.5."""
        assert S(1) == pytest.approx(0.5)

    def test_tong_s_n2(self):
        """S(2) = 1/2 + 1/4 = 0.75."""
        assert S(2) == pytest.approx(0.75)

    def test_tong_s_n3(self):
        """S(3) = 1/2 + 1/4 + 1/6 = 11/12 ≈ 0.9166667."""
        assert S(3) == pytest.approx(11 / 12)

    def test_nhap_n_hop_le_ngay(self, monkeypatch):
        """Nhập n hợp lệ ngay lần đầu."""
        monkeypatch.setattr("builtins.input", lambda _: "500")
        assert nhap_n() == 500

    def test_nhap_n_lap_lai_khi_sai_pham_vi(self, monkeypatch):
        """Nhập < 1 hoặc > 1500 phải yêu cầu nhập lại cho đến khi hợp lệ."""
        inputs = iter(["0", "2000", "-5", "1500"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        assert nhap_n() == 1500


# ==============================================================================
# CÂU 2 (2.0 điểm): Xử lý chuỗi ký tự s
# ==============================================================================
class TestBT02:
    def test_dem_chu_hoa_co_chu_hoa(self):
        assert dem_chu_hoa("Python Journey") == 2
        assert dem_chu_hoa("HELLO") == 5

    def test_dem_chu_hoa_khong_co(self):
        assert dem_chu_hoa("python 123") == 0
        assert dem_chu_hoa("") == 0

    def test_doi_xung_hop_le(self):
        assert doi_xung("radar") is True
        assert doi_xung("madam") is True
        assert doi_xung("12321") is True
        assert doi_xung("") is True

    def test_doi_xung_khong_hop_le(self):
        assert doi_xung("python") is False
        assert doi_xung("hello") is False

    def test_doixung_in_ket_qua(self, capsys):
        DoiXung("radar")
        captured = capsys.readouterr()
        assert "Chuỗi đối xứng." in captured.out

        DoiXung("python")
        captured = capsys.readouterr()
        assert "Chuỗi không đối xứng." in captured.out

    def test_tong_chu_so_co_so(self):
        assert tong_chu_so("a1b2c3") == 6
        assert tong_chu_so("999") == 27

    def test_tong_chu_so_khong_co_so(self):
        assert tong_chu_so("Hello World") == 0
        assert tong_chu_so("") == 0


# ==============================================================================
# CÂU 3 (2.0 điểm): Xử lý danh sách (list)
# ==============================================================================
class TestBT03:
    def test_nhap_danh_sach_dung_khi_gap_0(self, monkeypatch):
        inputs = iter(["10", "25", "-8", "0", "99"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        ds = nhap_danh_sach()
        assert ds == [10, 25, -8]

    def test_tong_duong_chan_binh_thuong(self):
        # 2, 4, 6 là số dương chẵn (tổng = 12)
        # -6 là số âm chẵn -> bỏ qua
        # 5, 7 là số lẻ -> bỏ qua
        ds = [2, 4, -6, 5, 6, 7]
        assert tong_duong_chan(ds) == 12

    def test_tong_duong_chan_khong_co_so_thoa_man(self):
        assert tong_duong_chan([1, 3, 5, -2, -4]) == 0
        assert tong_duong_chan([]) == 0

    def test_dem_so_lan_xuat_hien_co_phan_tu(self):
        ds = [1, 2, 3, 2, 4, 2, 5]
        assert dem_so_lan_xuat_hien(ds, 2) == 3
        assert dem_so_lan_xuat_hien(ds, 1) == 1

    def test_dem_so_lan_xuat_hien_khong_co(self):
        ds = [1, 2, 3, 4]
        assert dem_so_lan_xuat_hien(ds, 100) == 0
        assert dem_so_lan_xuat_hien([], 5) == 0


# ==============================================================================
# CÂU 4 (2.0 điểm): Quản lý từ điển sách thư viện (dict)
# ==============================================================================
class TestBT04:
    def test_them_sach_hop_le(self):
        tudien = {}
        hien_tai = datetime.now().year
        success = them_sach(
            tudien,
            ma_so="B01",
            ten_sach="Học Python",
            ten_tac_gia="Nguyễn Văn A",
            nha_xuat_ban="NXB Trẻ",
            nam_xuat_ban=hien_tai - 1,
        )
        assert success is True
        assert "B01" in tudien
        assert tudien["B01"] == ["Học Python", "Nguyễn Văn A", "NXB Trẻ", hien_tai - 1]

    def test_them_sach_nam_xuat_ban_tuong_lai(self):
        tudien = {}
        hien_tai = datetime.now().year
        # Năm lớn hơn năm hiện tại không được phép
        success = them_sach(
            tudien,
            ma_so="B02",
            ten_sach="Tương lai",
            ten_tac_gia="Trần B",
            nha_xuat_ban="NXB Kim Đồng",
            nam_xuat_ban=hien_tai + 5,
        )
        assert success is False
        assert "B02" not in tudien

    def test_xoa_sach_ton_tai(self):
        tudien = {
            "B01": ["Sách 1", "Tác giả 1", "NXB 1", 2020],
            "B02": ["Sách 2", "Tác giả 2", "NXB 2", 2021],
        }
        res = xoa_sach(tudien, "B01")
        assert res is True
        assert "B01" not in tudien
        assert "B02" in tudien

    def test_xoa_sach_khong_ton_tai(self):
        tudien = {"B01": ["Sách 1", "Tác giả 1", "NXB 1", 2020]}
        res = xoa_sach(tudien, "B99")
        assert res is False
        assert "B01" in tudien


# ==============================================================================
# CÂU 5 (2.0 điểm): Lập trình hướng đối tượng (OOP) - Lớp DienThoai
# ==============================================================================
class TestBT05:
    def test_khoi_tao_dienthoai_dt01(self):
        dt1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
        assert dt1.MaMay == "DT01"
        assert dt1.TenMay == "iPhone 15 Pro"
        assert dt1.HangSanXuat == "Apple"
        assert dt1.DungLuongPin == 3274
        assert dt1.GiaBan == 28990000

    def test_khoi_tao_dienthoai_dt02(self):
        dt2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)
        assert dt2.MaMay == "DT02"
        assert dt2.TenMay == "Galaxy S24 Ultra"
        assert dt2.HangSanXuat == "Samsung"
        assert dt2.DungLuongPin == 5000
        assert dt2.GiaBan == 29990000

    def test_phuong_thuc_thongtindienthoai(self, capsys):
        dt = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
        dt.thongtindienthoai()
        captured = capsys.readouterr()
        assert "Mã máy: DT01" in captured.out
        assert "Tên máy: iPhone 15 Pro" in captured.out
        assert "Hãng sản xuất: Apple" in captured.out
        assert "Dung lượng pin: 3274" in captured.out
        assert "Giá bán: 28990000" in captured.out
