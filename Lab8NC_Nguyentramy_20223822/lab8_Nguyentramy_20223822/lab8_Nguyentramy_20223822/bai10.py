import pandas as pd
import sqlite3
import os

# =========================
# 1. Kiểm tra file DB
# =========================
db_path = 'shop.db'

if not os.path.exists(db_path):
    print(f"Lỗi: Không tìm thấy file '{db_path}'")
else:
    # =========================
    # 2. Kết nối database
    # =========================
    conn = sqlite3.connect(db_path)

    try:
        # =========================
        # 3. Đọc bảng orders
        # =========================
        df = pd.read_sql_query("SELECT * FROM orders", conn)

        # =========================
        # 4. Hiển thị 5 dòng đầu
        # =========================
        print("=== 5 BẢN GHI ĐẦU ===")
        print(df.head())

        # =========================
        # 5. Tổng số đơn hàng
        # =========================
        total_orders = len(df)
        print("\nTổng số đơn hàng:", total_orders)

        # =========================
        # 6. Tổng doanh thu
        # =========================
        # ⚠️ Giả sử cột tên là 'total'
        total_revenue = df['total'].sum()
        print("Tổng doanh thu:", total_revenue)

    except Exception as e:
        print("Lỗi:", e)

    finally:
        conn.close()
