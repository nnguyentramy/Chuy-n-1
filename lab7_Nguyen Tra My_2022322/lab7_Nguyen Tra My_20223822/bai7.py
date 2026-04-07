import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính lại DiemTB nếu chưa có
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

# GroupBy theo giới tính và tính điểm trung bình
tb_theo_gt = df.groupby("GioiTinh")["DiemTB"].mean()

# In kết quả
print("=== Điểm trung bình theo giới tính ===")
print(tb_theo_gt)