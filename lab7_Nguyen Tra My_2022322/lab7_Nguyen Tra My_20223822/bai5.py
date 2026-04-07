import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính lại DiemTB và XepLoai nếu chưa có
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return "A"
    elif diem >= 7.0:
        return "B"
    elif diem >= 5.5:
        return "C"
    elif diem >= 4.0:
        return "D"
    else:
        return "F"

df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# Thống kê tần suất
print("=== Số lượng sinh viên theo giới tính ===")
print(df["GioiTinh"].value_counts())

print("\n=== Số lượng sinh viên theo lớp ===")
print(df["Lop"].value_counts())

print("\n=== Số lượng sinh viên theo chuyên ngành ===")
print(df["ChuyenNganh"].value_counts())

print("\n=== Số lượng sinh viên theo xếp loại ===")
print(df["XepLoai"].value_counts())