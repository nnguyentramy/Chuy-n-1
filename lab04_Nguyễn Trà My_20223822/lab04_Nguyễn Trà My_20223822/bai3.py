import numpy as np

# -----------------------------
# 1. Tạo ma trận doanh thu
# -----------------------------
sales = np.array([
    [120, 150, 130, 140, 160],
    [125, 145, 128, 142, 158],
    [130, 155, 135, 150, 162],
    [135, 160, 140, 152, 168],
    [140, 165, 145, 155, 170],
    [138, 162, 142, 153, 169],
    [145, 170, 150, 160, 175]
])

print("Ma trận doanh thu (5 sản phẩm x 7 ngày):\n", sales)
print("-"*50)

# -----------------------------
# 2. Tổng doanh thu từng ngày
# -----------------------------
daily_total = sales.sum(axis=1)
print("Tổng doanh thu từng ngày:", daily_total)

# -----------------------------
# 3. Tổng và trung bình từng sản phẩm
# -----------------------------
product_total = sales.sum(axis=0)
product_mean = sales.mean(axis=0)
print("Tổng doanh thu từng sản phẩm:", product_total)
print("Doanh thu trung bình từng sản phẩm:", product_mean)
print("-"*50)

# -----------------------------
# 4. Ngày cao nhất & sản phẩm bán tốt nhất
# -----------------------------
best_day_idx = np.argmax(daily_total) + 1
best_product_idx = np.argmax(product_total) + 1
print(f"Ngày có doanh thu cao nhất: Ngày {best_day_idx}")
print(f"Sản phẩm bán tốt nhất toàn tuần: Sản phẩm {best_product_idx}")
print("-"*50)

# -----------------------------
# 5. Tăng doanh số sản phẩm 2 và 5 lên 8%
# -----------------------------
new_sales = sales.astype(float).copy()
new_sales[:, [1, 4]] *= 1.08
print("Doanh thu sau điều chỉnh 8% cho sản phẩm 2 và 5:\n", new_sales)

# So sánh tổng doanh thu trước và sau điều chỉnh
before_total = sales.sum()
after_total = new_sales.sum()
print(f"Tổng doanh thu trước điều chỉnh: {before_total}")
print(f"Tổng doanh thu sau điều chỉnh: {after_total}")
print("-"*50)

# -----------------------------
# 6. Lọc các ngày có tổng doanh thu > trung bình toàn tuần
# -----------------------------
high_days = np.where(daily_total > daily_total.mean())[0] + 1
print("Các ngày có tổng doanh thu > trung bình toàn tuần:", high_days)
print("-"*50)

# -----------------------------
# 7. Sản phẩm có độ ổn định cao nhất (độ lệch chuẩn nhỏ nhất)
# -----------------------------
stable_product = np.argmin(sales.std(axis=0)) + 1
print(f"Sản phẩm có độ ổn định cao nhất: Sản phẩm {stable_product}")
print("-"*50)

# -----------------------------
# 8. Nhận xét ngắn
# -----------------------------
print("Nhận xét:")
print("- Sản phẩm bán tốt nhất (tổng doanh thu cao) nên ưu tiên trưng bày và khuyến mãi.")
print("- Sản phẩm ổn định về doanh thu giúp dự đoán bán hàng chính xác hơn.")
print("- Ngày có doanh thu cao cần tập trung nguồn lực, nhân viên và hàng tồn kho.")

