from BT05 import DienThoai


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
