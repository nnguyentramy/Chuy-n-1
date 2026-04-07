import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính lại DiemTB nếu chưa có
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

# Xếp loại nếu chưa có
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

# Tổng hợp số sinh viên và điểm trung bình theo chuyên ngành
tong_hop_cn = df.groupby("ChuyenNganh").agg(
    SoSinhVien=("MaSV", "count"),
    DiemTrungBinh=("DiemTB", "mean")
)

# Tính số sinh viên đạt loại A hoặc B
tyle_ab = df[df["XepLoai"].isin(["A", "B"])].groupby("ChuyenNganh")["MaSV"].count()
tong_hop_cn["SoDatAB"] = tyle_ab
tong_hop_cn["SoDatAB"] = tong_hop_cn["SoDatAB"].fillna(0)

# Tỷ lệ đạt A hoặc B (%)
tong_hop_cn["TyLeDatAB"] = tong_hop_cn["SoDatAB"] / tong_hop_cn["SoSinhVien"] * 100

# In kết quả làm tròn 2 chữ số
print("=== Báo cáo tổng hợp theo chuyên ngành ===")
print(tong_hop_cn.round(2))