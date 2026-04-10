import pandas as pd

# Đọc file CSV
df = pd.read_csv('students.csv')

# Hiển thị 5 dòng đầu
print("=== 5 dòng đầu ===")
print(df.head())

# In số dòng và số cột
print("\n=== Kích thước dữ liệu ===")
print("Số dòng:", df.shape[0])
print("Số cột:", df.shape[1])

# Liệt kê tên các cột
print("\n=== Danh sách cột ===")
print(df.columns.tolist())

# (Khuyến khích) Xem thông tin chi tiết
print("\n=== Thông tin dữ liệu ===")
print(df.info())