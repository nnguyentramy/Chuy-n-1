import pandas as pd

# =========================
# 1. Đọc dữ liệu
# =========================
df_students = pd.read_csv('students.csv')
df_scores = pd.read_excel('scores.xlsx')

print("=== STUDENTS ===")
print(df_students.head())

print("\n=== SCORES ===")
print(df_scores.head())


# =========================
# 2. Ghép dữ liệu theo MaSV
# =========================
df_merge = pd.merge(df_students, df_scores, on='MaSV')

print("\n=== SAU KHI GHÉP ===")
print(df_merge.head())


# =========================
# 3. Tính điểm tổng kết
# =========================
# ⚠️ Giả sử:
# DiemQT = điểm quá trình
# DiemThi = điểm thi

df_merge['DiemTongKet'] = df_merge['DiemQT'] * 0.4 + df_merge['DiemThi'] * 0.6


# =========================
# 4. Chọn cột cần thiết
# =========================
df_final = df_merge[['MaSV', 'HoTen', 'Lop', 'DiemQT', 'DiemThi', 'DiemTongKet']]

print("\n=== BẢNG TỔNG HỢP ===")
print(df_final)


# =========================
# 5. Lưu ra Excel
# =========================
df_final.to_excel('tonghop_diem.xlsx', index=False)

print("\n✅ Đã lưu file tonghop_diem.xlsx")
