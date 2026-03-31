import numpy as np

# -----------------------------
# 1. Tạo ma trận chuyên cần
# -----------------------------
attendance = np.array([
    [1,1,1,1,1,1,1,1],
    [1,1,0,1,1,0,1,1],
    [1,0,0,1,1,1,0,1],
    [1,1,1,1,0,1,1,1],
    [0,1,1,0,1,1,1,0],
    [1,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,1,0],
    [1,1,1,1,1,1,1,0],
    [0,0,1,1,0,1,1,1],
    [1,1,1,0,1,1,1,1],
    [1,1,0,0,1,0,1,1],
    [1,1,1,1,1,0,1,1]
])

print("Ma trận chuyên cần (1=có mặt, 0=vắng):\n", attendance)
print("-"*50)

# -----------------------------
# 2. Tổng số buổi đi học từng sinh viên
# -----------------------------
present_count = attendance.sum(axis=1)
print("Tổng số buổi đi học từng sinh viên:", present_count)

# Tỉ lệ chuyên cần theo %
rate = present_count / attendance.shape[1] * 100
print("Tỉ lệ chuyên cần (%):", rate)
print("-"*50)

# -----------------------------
# 3. Sinh viên bị cảnh báo (<75%)
# -----------------------------
warning_idx = np.where(rate < 75)[0] + 1  # cộng 1 để đánh số sinh viên từ 1
print("Sinh viên bị cảnh báo học vụ (tỉ lệ <75%):", warning_idx)
print("-"*50)

# -----------------------------
# 4. Buổi học có số lượng vắng nhiều nhất
# -----------------------------
absent_count_by_session = (attendance == 0).sum(axis=0)
worst_session = np.argmax(absent_count_by_session) + 1  # đánh số buổi từ 1
print("Số lượng vắng theo buổi:", absent_count_by_session)
print(f"Buổi học có nhiều sinh viên vắng nhất: Buổi {worst_session}")
print("-"*50)

# -----------------------------
# 5. Sinh viên đi học đầy đủ cả 8 buổi
# -----------------------------
full_attendance = np.where(np.all(attendance == 1, axis=1))[0] + 1
print("Sinh viên đi học đầy đủ 8 buổi:", full_attendance)
print("-"*50)

# -----------------------------
# 6. Sinh viên có ít nhất 2 buổi vắng liên tiếp
# -----------------------------
two_absent_in_row = np.where(np.any((attendance[:, :-1] == 0) & 
                                   (attendance[:, 1:] == 0), axis=1))[0] + 1
print("Sinh viên có ít nhất 2 buổi vắng liên tiếp:", two_absent_in_row)
print("-"*50)

# -----------------------------
# 7. Nhận xét ngắn
# -----------------------------
print("Nhận xét:")
print("- Một số sinh viên có tỉ lệ chuyên cần thấp (<75%), cần cảnh báo học vụ.")
print("- Buổi học 1,2,5,... có nhiều sinh viên vắng, cần lưu ý tổ chức lớp.")
print("- Một số sinh viên đi học đầy đủ 8 buổi, thể hiện ý thức tốt.")
print("- Một số sinh viên có 2 buổi vắng liên tiếp, cần nhắc nhở theo dõi sát.")
