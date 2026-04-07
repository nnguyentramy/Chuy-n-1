import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính lại DiemTB nếu chưa có
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

# Thống kê mô tả
print("=== Thống kê điểm trung bình ===")
print("Trung bình:", df["DiemTB"].mean())
print("Lớn nhất:", df["DiemTB"].max())
print("Nhỏ nhất:", df["DiemTB"].min())
print("Độ lệch chuẩn:", df["DiemTB"].std())