import pandas as pd
import json

# Đọc dữ liệu từ file JSON (giả lập API)
with open('products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Chuyển sang DataFrame
df = pd.DataFrame(data)

# Chọn các cột quan trọng
df_selected = df[['id', 'name', 'category', 'price']]

# Hiển thị
print("===== DỮ LIỆU SẢN PHẨM =====")
print(df_selected)

# Lưu ra CSV
df_selected.to_csv('products_output.csv', index=False, encoding='utf-8-sig')

print("\n✅ Đã lưu file products_output.csv")
