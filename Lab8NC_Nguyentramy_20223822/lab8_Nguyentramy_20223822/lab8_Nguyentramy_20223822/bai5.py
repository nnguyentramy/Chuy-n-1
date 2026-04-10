import pandas as pd

# =========================
# 1. Đọc file UTF-8
# =========================
print("=== FILE UTF-8 ===")

try:
    df_utf8 = pd.read_csv('sinhvien_utf8.csv', encoding='utf-8')

    print("\nĐọc bằng utf-8 (ĐÚNG):")
    print(df_utf8.head())

except Exception as e:
    print("Lỗi khi đọc UTF-8:", e)


# =========================
# 2. Đọc file ANSI (thường là cp1258 hoặc latin1)
# =========================
print("\n\n=== FILE ANSI ===")

# Thử sai trước (utf-8)
try:
    df_ansi_wrong = pd.read_csv('sinhvien_ansi.csv', encoding='utf-8')

    print("\nĐọc ANSI bằng utf-8 (SAI):")
    print(df_ansi_wrong.head())

except Exception as e:
    print("\nLỗi khi đọc ANSI bằng utf-8:", e)


# Thử đúng encoding
try:
    df_ansi_correct = pd.read_csv('sinhvien_ansi.csv', encoding='latin1')

    print("\nĐọc ANSI bằng latin1 (ĐÚNG):")
    print(df_ansi_correct.head())

except Exception as e:
    print("Lỗi khi đọc ANSI:", e)


# =========================
# 3. So sánh
# =========================
print("\n\n=== SO SÁNH ===")
print("""
- File UTF-8:
  + Dùng encoding='utf-8'
  + Hiển thị tiếng Việt đúng

- File ANSI:
  + Nếu đọc bằng utf-8 → lỗi hoặc hiển thị sai ký tự
  + Phải dùng encoding='latin1' hoặc 'cp1258'
""")


# =========================
# 4. Kết luận
# =========================
print("\n=== KẾT LUẬN ===")
print("""
- encoding quyết định cách đọc ký tự trong file.
- Sai encoding → lỗi font, ký tự bị lỗi (�, ?, ...).
- UTF-8: chuẩn hiện đại, dùng phổ biến.
- ANSI: thường gặp ở file Excel cũ trên Windows.
- Khi đọc file thực tế → cần thử nhiều encoding nếu bị lỗi.
""")
