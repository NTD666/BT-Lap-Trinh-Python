import pytest
from BT01 import DemChuSoLe, S, nhap_n


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
