import pandas as pd

# Đọc file và ép kiểu MaKH thành chuỗi
df = pd.read_csv('customers.csv', dtype={'MaKH': str})

# Hiển thị dữ liệu
print("=== Dữ liệu ===")
print(df.head())

# Kiểm tra kiểu dữ liệu
print("\n=== Kiểu dữ liệu ===")
print(df.dtypes)