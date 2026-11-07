import sys
from pathlib import Path

# Thêm thư mục gốc của dự án vào sys.path để pytest có thể import trực tiếp các module BT01..BT05
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
