import numpy as np

# -----------------------------
# 1. Dữ liệu tồn kho
# -----------------------------
stock = np.array([35, 8, 12, 5, 40, 18, 7, 22, 9, 15])
min_stock = np.array([20, 15, 15, 10, 25, 20, 12, 18, 12, 15])
price = np.array([30, 25, 28, 22, 35, 20, 18, 24, 19, 21])

print("Tồn kho hiện tại:", stock)
print("Mức tồn tối thiểu:", min_stock)
print("Giá nhập dự kiến:", price)
print("-"*50)

# -----------------------------
# 2. Xác định mặt hàng thiếu và số lượng cần nhập
# -----------------------------
need_import = np.maximum(min_stock - stock, 0)
print("Số lượng cần nhập cho từng mặt hàng:", need_import)

# -----------------------------
# 3. Chỉ tính chi phí nhập cho mặt hàng thiếu
# -----------------------------
cost = need_import * price
print("Chi phí nhập từng mặt hàng thiếu:", cost)

# -----------------------------
# 4. Tổng chi phí nhập hàng
# -----------------------------
total_cost = cost.sum()
print(f"Tổng chi phí nhập hàng: {total_cost}")
print("-"*50)

# -----------------------------
# 5. Phân loại trạng thái hàng
# -----------------------------
status = np.where(stock < min_stock, "Thiếu hàng", "Đủ hàng")
print("Trạng thái từng mặt hàng:", status)
print("-"*50)

# -----------------------------
# 6. 3 mặt hàng thiếu nhiều nhất
# -----------------------------
top3_shortage = np.argsort(need_import)[::-1][:3] + 1
print("3 mặt hàng thiếu nhiều nhất (theo số thứ tự):", top3_shortage)
print("-"*50)

# -----------------------------
# 7. Giới hạn số lượng nhập tối đa mỗi mặt hàng là 20
# -----------------------------
limited_need = np.clip(need_import, 0, 20)
print("Số lượng nhập sau giới hạn tối đa 20:", limited_need)

# -----------------------------
# 8. Tổng chi phí sau giới hạn
# -----------------------------
limited_total_cost = (limited_need * price).sum()
print(f"Tổng chi phí nhập hàng sau giới hạn: {limited_total_cost}")
print("-"*50)

# -----------------------------
# 9. Nhận xét ngắn
# -----------------------------
print("Nhận xét:")
print("- Một số mặt hàng đang thiếu so với mức tối thiểu, cần nhập bổ sung.")
print("- Top 3 mặt hàng thiếu nhiều nhất cần ưu tiên nhập trước.")
print("- Giới hạn nhập 20 đơn vị giúp kiểm soát chi phí và tránh tồn kho quá lớn.")
