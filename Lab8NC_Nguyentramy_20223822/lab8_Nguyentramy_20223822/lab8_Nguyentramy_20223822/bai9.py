import pandas as pd

# 1. Đọc file JSON
df = pd.read_json('products.json')

# 2. Hiển thị dữ liệu
print("Dữ liệu ban đầu:")
print(df.head())

# 3. Chọn các cột cần thiết
df_selected = df[['ma_sp', 'ten_sp', 'nhom', 'gia']]

print("\nCác trường cần hiển thị:")
print(df_selected)
