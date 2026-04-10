import pandas as pd
import os

# =========================
# 1. Kiểm tra file tồn tại
# =========================
file_path = 'inventory.xlsx'

if not os.path.exists(file_path):
    print(f"Lỗi: Không tìm thấy file '{file_path}'")
    print("👉 Hãy kiểm tra lại:")
    print("- File có cùng thư mục với file .py không")
    print("- Tên file có đúng không (inventory.xlsx)")
else:
    # =========================
    # 2. Đọc file Excel
    # =========================
    try:
        df = pd.read_excel(file_path, sheet_name='HangHoa')

        print("=== 10 DÒNG ĐẦU ===")
        print(df.head(10))

        print("\nTên các cột:")
        print(df.columns)

    except Exception as e:
        print("Lỗi khi đọc file:", e)
        exit()

    # =========================
    # 3. Lọc dữ liệu
    # =========================
    try:
        # ⚠️ Sửa tên cột nếu cần
        df_low_stock = df[df['SoLuong'] < 20]

        print("\n=== HÀNG TỒN KHO < 20 ===")
        print(df_low_stock)

    except KeyError:
        print("\nLỗi: Không tìm thấy cột 'SoLuong'")
        print("👉 Tên cột hiện có là:")
        print(df.columns)
        exit()

    # =========================
    # 4. Lưu file
    # =========================
    try:
        df_low_stock.to_excel('hanghoa_tonkho_thap.xlsx', index=False)
        print("\nĐã lưu file: hanghoa_tonkho_thap.xlsx")

    except Exception as e:
        print("Lỗi khi lưu file:", e)
