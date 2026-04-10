import pandas as pd

# Đọc file KHÔNG có header
df = pd.read_csv(
    'scores_no_header.csv',
    header=None,
    names=['MaSV', 'HoTen', 'Lop', 'DiemQT', 'DiemThi']
)

# Hiển thị dữ liệu
print("=== Dữ liệu sau khi gán tên cột ===")
print(df.head())

# Thông tin dữ liệu
print("\n=== Thông tin DataFrame ===")
df.info()