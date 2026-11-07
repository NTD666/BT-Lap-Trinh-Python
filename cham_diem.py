"""Script chấm điểm tự động cho Đề thi Lập trình Python (Mã đề: 11301).

Thang điểm: 10.0 điểm theo đúng biểu điểm chính thức từ file PDF.
Sử dụng:
    python cham_diem.py
"""

from __future__ import annotations

import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from dataclasses import dataclass, field
import pytest


@dataclass
class SubQuestion:
    id: str
    title: str
    max_score: float
    test_names: list[str]
    passed_tests: list[str] = field(default_factory=list)
    failed_tests: list[str] = field(default_factory=list)

    @property
    def score(self) -> float:
        if not self.test_names:
            return 0.0
        # Tỷ lệ điểm tương ứng với số test case pass trong phần này
        return round(self.max_score * len(self.passed_tests) / len(self.test_names), 2)


@dataclass
class Question:
    id: str
    title: str
    sub_questions: list[SubQuestion]

    @property
    def max_score(self) -> float:
        return sum(sub.max_score for sub in self.sub_questions)

    @property
    def score(self) -> float:
        return sum(sub.score for sub in self.sub_questions)


class GradeCollector:
    def __init__(self, questions: list[Question]):
        self.questions = questions
        self.test_to_sub: dict[str, SubQuestion] = {}
        for q in self.questions:
            for sub in q.sub_questions:
                for t in sub.test_names:
                    self.test_to_sub[t] = sub

    def pytest_runtest_logreport(self, report: pytest.TestReport):
        if report.when == "call":
            # report.nodeid dạng: tests/test_bt01.py::TestBT01::test_dem_chu_so_le_mau_de_thi
            test_name = report.nodeid.split("::")[-1]
            sub = self.test_to_sub.get(test_name)
            if sub:
                if report.passed:
                    sub.passed_tests.append(test_name)
                else:
                    sub.failed_tests.append(test_name)


def create_rubric() -> list[Question]:
    return [
        Question(
            id="Câu 1",
            title="Nhập số n, đếm chữ số lẻ, tính tổng phân số S",
            sub_questions=[
                SubQuestion(
                    id="1a",
                    title="Kiểm tra khoảng n [1; 1500]",
                    max_score=0.5,
                    test_names=[
                        "test_nhap_n_hop_le_ngay",
                        "test_nhap_n_lap_lai_khi_sai_pham_vi",
                    ],
                ),
                SubQuestion(
                    id="1b",
                    title="Hàm con DemChuSoLe(n)",
                    max_score=0.75,
                    test_names=[
                        "test_dem_chu_so_le_mau_de_thi",
                        "test_dem_chu_so_le_toan_chan",
                        "test_dem_chu_so_le_toan_le",
                        "test_dem_chu_so_le_so_don",
                    ],
                ),
                SubQuestion(
                    id="1c",
                    title="Hàm con tính tổng S(n)",
                    max_score=0.75,
                    test_names=[
                        "test_tong_s_n1",
                        "test_tong_s_n2",
                        "test_tong_s_n3",
                    ],
                ),
            ],
        ),
        Question(
            id="Câu 2",
            title="Xử lý chuỗi (chữ hoa, đối xứng, tổng các chữ số)",
            sub_questions=[
                SubQuestion(
                    id="2a",
                    title="Đếm số ký tự in hoa",
                    max_score=0.75,
                    test_names=[
                        "test_dem_chu_hoa_co_chu_hoa",
                        "test_dem_chu_hoa_khong_co",
                    ],
                ),
                SubQuestion(
                    id="2b",
                    title="Kiểm tra chuỗi đối xứng (DoiXung)",
                    max_score=0.5,
                    test_names=[
                        "test_doi_xung_hop_le",
                        "test_doi_xung_khong_hop_le",
                        "test_doixung_in_ket_qua",
                    ],
                ),
                SubQuestion(
                    id="2c",
                    title="Tính tổng các ký tự chữ số",
                    max_score=0.75,
                    test_names=[
                        "test_tong_chu_so_co_so",
                        "test_tong_chu_so_khong_co_so",
                    ],
                ),
            ],
        ),
        Question(
            id="Câu 3",
            title="Xử lý danh sách (nhập đến khi gặp 0, chẵn dương, đếm k)",
            sub_questions=[
                SubQuestion(
                    id="3a",
                    title="Nhập danh sách ngưng khi nhập 0",
                    max_score=0.75,
                    test_names=["test_nhap_danh_sach_dung_khi_gap_0"],
                ),
                SubQuestion(
                    id="3b",
                    title="Tính tổng các số dương chẵn",
                    max_score=0.75,
                    test_names=[
                        "test_tong_duong_chan_binh_thuong",
                        "test_tong_duong_chan_khong_co_so_thoa_man",
                    ],
                ),
                SubQuestion(
                    id="3c",
                    title="Đếm số lần xuất hiện của phần tử k",
                    max_score=0.5,
                    test_names=[
                        "test_dem_so_lan_xuat_hien_co_phan_tu",
                        "test_dem_so_lan_xuat_hien_khong_co",
                    ],
                ),
            ],
        ),
        Question(
            id="Câu 4",
            title="Quản lý từ điển sách thư viện (thêm / xóa theo mã)",
            sub_questions=[
                SubQuestion(
                    id="4a",
                    title="Nhập & lưu thông tin sách (năm XB <= hiện tại)",
                    max_score=1.5,
                    test_names=[
                        "test_them_sach_hop_le",
                        "test_them_sach_nam_xuat_ban_tuong_lai",
                    ],
                ),
                SubQuestion(
                    id="4b",
                    title="Xóa cuốn sách theo mã số sách",
                    max_score=0.5,
                    test_names=[
                        "test_xoa_sach_ton_tai",
                        "test_xoa_sach_khong_ton_tai",
                    ],
                ),
            ],
        ),
        Question(
            id="Câu 5",
            title="Lập trình OOP: Lớp DienThoai và 2 đối tượng mẫu",
            sub_questions=[
                SubQuestion(
                    id="5a",
                    title="Thuộc tính, __init__ và thongtindienthoai()",
                    max_score=1.0,
                    test_names=[
                        "test_khoi_tao_dienthoai_dt01",
                        "test_phuong_thuc_thongtindienthoai",
                    ],
                ),
                SubQuestion(
                    id="5b",
                    title="Khởi tạo đối tượng DT02 & kiểm tra",
                    max_score=1.0,
                    test_names=["test_khoi_tao_dienthoai_dt02"],
                ),
            ],
        ),
    ]


def in_bang_diem(questions: list[Question]):
    total_score = sum(q.score for q in questions)
    max_total = sum(q.max_score for q in questions)

    print("\n" + "=" * 76)
    print("      HỆ THỐNG CHẤM ĐIỂM TỰ ĐỘNG — ĐỀ THI LẬP TRÌNH PYTHON (MÃ ĐỀ: 11301)")
    print("=" * 76)
    print(f"{'Câu hỏi / Nội dung chi tiết':<50} | {'Điểm đạt':<10} | {'Trạng thái'}")
    print("-" * 76)

    for q in questions:
        q_status = "✅ PASS" if q.score == q.max_score else ("⚠️ PARTIAL" if q.score > 0 else "❌ FAIL")
        print(f"\n{q.id}: {q.title:<42} | {q.score:>4.2f}/{q.max_score:<4.2f} đ | {q_status}")
        for sub in q.sub_questions:
            passed = len(sub.passed_tests)
            total = len(sub.test_names)
            sub_status = "OK" if passed == total else f"{passed}/{total} tests"
            icon = "✓" if passed == total else "✗"
            print(f"  [{icon}] {sub.id}. {sub.title:<42} | {sub.score:>4.2f}/{sub.max_score:<4.2f} đ | {sub_status}")

    print("-" * 76)
    percentage = (total_score / max_total) * 100
    if total_score >= 9.0:
        xep_loai = "XUẤT SẮC"
    elif total_score >= 8.0:
        xep_loai = "GIỎI"
    elif total_score >= 6.5:
        xep_loai = "KHÁ"
    elif total_score >= 5.0:
        xep_loai = "TRUNG BÌNH (ĐẠT)"
    else:
        xep_loai = "CHƯA ĐẠT"

    print(f"TỔNG KẾT: {total_score:.2f} / {max_total:.2f} ĐIỂM  ({percentage:.1f}%) — XẾP LOẠI: {xep_loai}")
    print("=" * 76 + "\n")


def main() -> int:
    questions = create_rubric()
    collector = GradeCollector(questions)

    # Chạy pytest ngầm và thu thập kết quả
    pytest.main(["-q", "--tb=no"], plugins=[collector])

    # Hiển thị bảng điểm
    in_bang_diem(questions)

    total_score = sum(q.score for q in questions)
    max_total = sum(q.max_score for q in questions)
    return 0 if total_score == max_total else 1


if __name__ == "__main__":
    sys.exit(main())
