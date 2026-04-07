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

# Tạo Pivot Table: hàng = Lop, cột = XepLoai, giá trị = số lượng sinh viên
pivot1 = pd.pivot_table(
    df,
    index="Lop",
    columns="XepLoai",
    values="MaSV",
    aggfunc="count",
    fill_value=0
)

# In kết quả
print("=== Bảng Pivot Table: Số lượng sinh viên theo lớp và xếp loại ===")
print(pivot1)