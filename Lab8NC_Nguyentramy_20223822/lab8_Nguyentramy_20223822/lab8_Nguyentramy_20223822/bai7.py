import pandas as pd

# Đọc file Excel, tất cả sheet cùng lúc
file_excel = "quanlykho.xlsx"
xls = pd.ExcelFile(file_excel)

# Liệt kê các sheet
print("Các sheet có trong file Excel:")
print(xls.sheet_names)

# Đọc từng sheet vào DataFrame
df_hanghoa = pd.read_excel(file_excel, sheet_name="HangHoa")
df_nhapkho = pd.read_excel(file_excel, sheet_name="NhapKho")
df_xuatkho = pd.read_excel(file_excel, sheet_name="XuatKho")

# Kiểm tra cấu trúc từng sheet
print("\n=== HangHoa ===")
print(df_hanghoa.head())
print(df_hanghoa.info())

print("\n=== NhapKho ===")
print(df_nhapkho.head())
print(df_nhapkho.info())

print("\n=== XuatKho ===")
print(df_xuatkho.head())
print(df_xuatkho.info())