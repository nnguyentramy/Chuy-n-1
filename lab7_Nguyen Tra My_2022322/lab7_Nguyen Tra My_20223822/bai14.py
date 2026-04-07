import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính lại DiemTB nếu chưa có
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

# Tìm sinh viên có điểm cao nhất trong từng lớp
idx = df.groupby("Lop")["DiemTB"].idxmax()  # chỉ số của sinh viên điểm cao nhất
sv_max = df.loc[idx, ["HoTen", "Lop", "DiemTB"]]  # lấy thông tin cần thiết

# In kết quả
print("=== Sinh viên có điểm cao nhất từng lớp ===")
print(sv_max)