import pandas as pd

# B1: Đọc dữ liệu từ file CSV
df = pd.read_csv("diem_sinhvien.csv")

# B2: Tính điểm trung bình theo trọng số
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

# B3: Làm tròn (cho đẹp)
df["DiemTB"] = df["DiemTB"].round(2)

# B4: Hiển thị kết quả
print(df[["MaSV", "HoTen", "DiemQT", "DiemGK", "DiemCK", "DiemTB"]].head())