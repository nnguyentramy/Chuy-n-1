import sqlite3

# Tạo database
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# Xóa bảng cũ nếu có (tránh lỗi)
cursor.execute("DROP TABLE IF EXISTS orders")

# Tạo bảng mới
cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    total INTEGER
)
""")

# Thêm dữ liệu mẫu
cursor.execute("INSERT INTO orders (customer, total) VALUES ('An', 100000)")
cursor.execute("INSERT INTO orders (customer, total) VALUES ('Bình', 200000)")
cursor.execute("INSERT INTO orders (customer, total) VALUES ('Cường', 150000)")
cursor.execute("INSERT INTO orders (customer, total) VALUES ('Dũng', 300000)")
cursor.execute("INSERT INTO orders (customer, total) VALUES ('Hà', 250000)")

# Lưu và đóng
conn.commit()
conn.close()

print("✅ Đã tạo database shop.db và bảng orders")
