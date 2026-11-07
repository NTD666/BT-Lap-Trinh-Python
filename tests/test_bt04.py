from datetime import datetime
from BT04 import them_sach, xoa_sach


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
