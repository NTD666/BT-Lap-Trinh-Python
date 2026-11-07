from BT03 import dem_so_lan_xuat_hien, nhap_danh_sach, tong_duong_chan


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
