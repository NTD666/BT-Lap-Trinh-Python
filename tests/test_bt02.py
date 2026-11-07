from BT02 import DoiXung, dem_chu_hoa, doi_xung, tong_chu_so


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
