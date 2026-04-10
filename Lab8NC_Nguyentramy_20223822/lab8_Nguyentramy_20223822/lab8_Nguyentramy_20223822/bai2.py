import pandas as pd

# ❌ Đọc SAI (vẫn dùng mặc định sep='')
df_sai = pd.read_csv('students.csv')

print("=== Đọc SAI (không dùng sep=';') ===")
print(df_sai.head())
print("Số cột:", df_sai.shape[1])


# ✅ Đọc ĐÚNG (dùng sep=';')
df_dung = pd.read_csv('students.csv', sep=',')

print("\n=== Đọc ĐÚNG (sep=';') ===")
print(df_dung.head())
print("Số cột:", df_dung.shape[1])