import numpy as np

# -----------------------------
# 1. Tạo ma trận điểm
# -----------------------------
scores = np.array([
    [8.0, 7.5, 8.5, 7.0],
    [6.5, 6.0, 7.0, 6.5],
    [9.0, 8.5, 9.0, 8.5],
    [5.0, 5.5, 6.0, 5.5],
    [7.5, 7.0, 8.0, 7.5],
    [4.5, 5.0, 5.5, 5.0],
    [8.5, 9.0, 8.0, 9.0],
    [6.0, 6.5, 6.0, 6.5],
    [7.0, 7.5, 7.0, 8.0],
    [9.5, 9.0, 9.5, 9.0]
])

print("Ma trận điểm:\n", scores)
print("Shape:", scores.shape)
print("Số chiều (ndim):", scores.ndim)
print("Kiểu dữ liệu (dtype):", scores.dtype)
print("-"*50)

# -----------------------------
# 2. Tính điểm tổng kết theo trọng số
# -----------------------------
weights = np.array([0.1, 0.2, 0.3, 0.4])
final_score = scores @ weights  # nhân ma trận
print("Điểm tổng kết của từng sinh viên:", final_score)
print("-"*50)

# -----------------------------
# 3. Xếp loại theo thang A,B,C,D
# -----------------------------
def grade(score):
    if score >= 8.0:
        return 'A'
    elif score >= 7.0:
        return 'B'
    elif score >= 5.0:
        return 'C'
    else:
        return 'D'

grades = np.array([grade(s) for s in final_score])
print("Xếp loại sinh viên:", grades)
print("-"*50)

# -----------------------------
# 4. Sinh viên điểm cao nhất và thấp nhất
# -----------------------------
max_idx = np.argmax(final_score)
min_idx = np.argmin(final_score)
print(f"Điểm cao nhất: Sinh viên {max_idx+1}, {final_score[max_idx]:.2f}")
print(f"Điểm thấp nhất: Sinh viên {min_idx+1}, {final_score[min_idx]:.2f}")
print("-"*50)

# -----------------------------
# 5. Lọc sinh viên có điểm >= 7.0
# -----------------------------
good_students = final_score[final_score >= 7.0]
print("Sinh viên có điểm tổng kết >= 7.0:", good_students)
print("-"*50)

# -----------------------------
# 6. Sinh viên có ít nhất một điểm < 5.0
# -----------------------------
low_component = np.any(scores < 5.0, axis=1)
students_low = np.where(low_component)[0] + 1
print("Sinh viên có ít nhất 1 điểm < 5.0:", students_low)
print("-"*50)

# -----------------------------
# 7. Sắp xếp điểm tổng kết giảm dần và top 3 sinh viên
# -----------------------------
rank_idx = np.argsort(final_score)[::-1]
top3 = rank_idx[:3] + 1  # cộng 1 để đánh số sinh viên từ 1
print("Sinh viên xếp theo điểm giảm dần:", rank_idx + 1)
print("3 sinh viên đứng đầu:", top3)
print("-"*50)

# -----------------------------
# 8. Chuẩn hóa điểm cuối kỳ theo Z-score
# -----------------------------
final_exam = scores[:, 3]
z_final_exam = (final_exam - final_exam.mean()) / final_exam.std()
print("Điểm cuối kỳ chuẩn hóa (Z-score):", z_final_exam)

# Nhận xét ngắn
print("\nNhận xét:")
print("- Điểm cuối kỳ có sự phân hóa rõ ràng: một số sinh viên cao (>0.8), một số thấp (<-0.8).")
print("- Chuẩn hóa Z-score giúp so sánh mức độ phân hóa giữa sinh viên dễ dàng hơn.")
