import pandas as pd
import numpy as np

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính lại DiemTB nếu chưa có
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

# Tạo cột KetQua: Đỗ nếu >=4.0, Trượt nếu <4.0
df["KetQua"] = np.where(df["DiemTB"] >= 4.0, "Do", "Truot")

# Thống kê số lượng đỗ/trượt theo lớp
so_luong = pd.crosstab(df["Lop"], df["KetQua"])
print("=== Số lượng sinh viên đỗ/trượt theo lớp ===")
print(so_luong)

# Thống kê tỷ lệ đỗ/trượt theo lớp (theo %)
ty_le = pd.crosstab(df["Lop"], df["KetQua"], normalize="index") * 100
print("\n=== Tỷ lệ đỗ/trượt theo lớp (%) ===")
print(ty_le.round(2))