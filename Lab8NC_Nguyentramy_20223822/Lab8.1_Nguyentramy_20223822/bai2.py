import pandas as pd

# Hàm chuẩn hóa tên cột
def chuanhoa_cot(df):
    df.columns = df.columns.str.strip()      # bỏ khoảng trắng
    df.columns = df.columns.str.lower()      # viết thường
    df.columns = df.columns.str.replace(' ', '_')  # thay space = _
    return df

# Đọc dữ liệu
df_jan = pd.read_csv('sales_jan.csv')
df_feb = pd.read_csv('sales_feb.csv')
df_mar = pd.read_csv('sales_mar.csv')

# Chuẩn hóa cột
df_jan = chuanhoa_cot(df_jan)
df_feb = chuanhoa_cot(df_feb)
df_mar = chuanhoa_cot(df_mar)

# (Tùy trường hợp) đổi tên về chuẩn chung
rename_map = {
    'masp': 'ma_sp',
    'productid': 'ma_sp',
    'product_id': 'ma_sp',

    'soluong': 'so_luong',
    'quantity': 'so_luong',

    'giaban': 'gia_ban',
    'price': 'gia_ban',

    'ngayban': 'ngay_ban',
    'date': 'ngay_ban'
}

df_jan = df_jan.rename(columns=rename_map)
df_feb = df_feb.rename(columns=rename_map)
df_mar = df_mar.rename(columns=rename_map)

# Ghép dữ liệu
df_all = pd.concat([df_jan, df_feb, df_mar], ignore_index=True)

# Hiển thị
print("===== DỮ LIỆU QUÝ 1 =====")
print(df_all)

# Lưu file
df_all.to_csv('sales_q1.csv', index=False)

print("\n✅ Đã tạo file sales_q1.csv")
