import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính lại DiemTB nếu chưa có
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

# Tổng hợp theo lớp: số lượng, trung bình, max, min
tonghop = df.groupby("Lop")["DiemTB"].agg(["count", "mean", "max", "min"])

# In kết quả
print("=== Tổng hợp điểm theo lớp ===")
print(tonghop)