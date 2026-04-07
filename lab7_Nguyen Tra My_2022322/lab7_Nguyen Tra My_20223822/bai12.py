import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Tính lại DiemTB nếu chưa có
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

# Tạo cột NhomDiem
bins = [0, 5, 7, 8.5, 10]  # Các khoảng điểm
labels = ["<5", "5-6.9", "7-8.4", ">=8.5"]  # Nhãn tương ứng
df["NhomDiem"] = pd.cut(df["DiemTB"], bins=bins, labels=labels, right=False)

# Thống kê số lượng sinh viên theo nhóm điểm của mỗi lớp
bang_nhomdiem = pd.crosstab(df["Lop"], df["NhomDiem"])

# In kết quả
print("=== Bảng phân nhóm điểm học lực theo lớp ===")
print(bang_nhomdiem)