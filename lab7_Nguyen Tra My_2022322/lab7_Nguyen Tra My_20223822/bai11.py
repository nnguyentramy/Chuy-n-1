import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tạo bảng chéo: hàng = lớp, cột = giới tính
bang_cheo = pd.crosstab(df["Lop"], df["GioiTinh"])

# In kết quả
print("=== Bảng Crosstab: Số lượng sinh viên theo lớp và giới tính ===")
print(bang_cheo)