import pandas as pd

# Đọc dữ liệu sales
df = pd.read_csv("sales.csv")

# Đặt ngưỡng doanh thu
ng_threshold = 10000

# Lọc các đơn hàng có DoanhThu > ngưỡng
df_high = df[df["DoanhThu"] > ng_threshold]

# Ghi kết quả ra CSV
df_high.to_csv("high_sales.csv", index=False, encoding='utf-8')

# Ghi kết quả ra Excel
df_high.to_excel("high_sales.xlsx", index=False)

print("Đã ghi xong high_sales.csv và high_sales.xlsx:")
print(df_high)