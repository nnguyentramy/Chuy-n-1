import pandas as pd

# ==============================
# 1. ĐỌC DỮ LIỆU
# ==============================
df_customers = pd.read_csv('customers.csv')
df_orders = pd.read_excel('orders.xlsx')
df_products = pd.read_json('products1.json')  # ✅ đổi tên ở đây

# ==============================
# 2. CHUẨN HÓA TÊN CỘT
# ==============================
df_customers.columns = df_customers.columns.str.lower()
df_orders.columns = df_orders.columns.str.lower()
df_products.columns = df_products.columns.str.lower()

# chuẩn hóa orders
df_orders = df_orders.rename(columns={
    'soluong': 'quantity',
    'so_luong': 'quantity',
    'giaban': 'price',
    'gia_ban': 'price'
})

# ==============================
# 3. KIỂM TRA CỘT QUAN TRỌNG
# ==============================
required_cols = ['customer_id', 'product_id', 'quantity', 'price']

for col in required_cols:
    if col not in df_orders.columns:
        raise Exception(f"❌ Thiếu cột {col} trong orders.xlsx")

# ==============================
# 4. MERGE DỮ LIỆU
# ==============================
df_merge = df_orders.merge(df_customers, on='customer_id', how='left')
df_merge = df_merge.merge(df_products, on='product_id', how='left')

# ==============================
# 5. TÍNH TOÁN
# ==============================
df_merge['total'] = df_merge['quantity'] * df_merge['price']

# ==============================
# 6. BÁO CÁO KHÁCH HÀNG
# ==============================
report_customer = df_merge.groupby(
    ['customer_id', 'customer_name'], as_index=False
).agg(
    total_orders=('order_id', 'count'),
    total_amount=('total', 'sum')
)

# ==============================
# 7. BÁO CÁO SẢN PHẨM
# ==============================
report_product = df_merge.groupby(
    ['category'], as_index=False
).agg(
    total_quantity=('quantity', 'sum'),
    total_amount=('total', 'sum')
)

# ==============================
# 8. XUẤT FILE EXCEL
# ==============================
with pd.ExcelWriter('report.xlsx') as writer:
    report_customer.to_excel(writer, sheet_name='BaoCaoKhachHang', index=False)
    report_product.to_excel(writer, sheet_name='BaoCaoSanPham', index=False)

print("✅ Đã xuất file report.xlsx thành công!")
