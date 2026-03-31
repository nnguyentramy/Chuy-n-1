import numpy as np

# -----------------------------
# Dữ liệu Bài Giáo dục (Bài 1)
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
weights = np.array([0.1, 0.2, 0.3, 0.4])
final_score = scores @ weights

# Boolean indexing
good_students = final_score[final_score >= 7.0]
low_score_students = np.where(np.any(scores < 5.0, axis=1))[0] + 1

# -----------------------------
# Dữ liệu Bài Kinh doanh (Bài 3)
# -----------------------------
sales = np.array([
    [120, 150, 130, 140, 160],
    [125, 145, 128, 142, 158],
    [130, 155, 135, 150, 162],
    [135, 160, 140, 152, 168],
    [140, 165, 145, 155, 170],
    [138, 162, 142, 153, 169],
    [145, 170, 150, 160, 175]
])

daily_total = sales.sum(axis=1)
product_total = sales.sum(axis=0)

# Boolean indexing minh họa (các ngày doanh thu > trung bình)
high_days = np.where(daily_total > daily_total.mean())[0] + 1

# -----------------------------
# Trả lời câu hỏi
# -----------------------------
print("1. Giống nhau về cấu trúc:")
print("- Cả hai dữ liệu đều là ma trận 2 chiều (ndarray).")
print("- Hàng: đối tượng (sinh viên/ngày), Cột: thuộc tính (điểm/sản phẩm).")
print("- Có thể dùng sum, mean, argmax/argmin để tổng hợp.\n")

print("2. Phép toán NumPy dùng ở cả hai bài:")
print("- sum(axis=0/1), mean(), argmax(), argmin(), boolean indexing (np.where).\n")

print("3. Bài sử dụng boolean indexing nhiều hơn:")
print("- Bài Giáo dục dùng nhiều hơn để lọc sinh viên điểm >=7, phát hiện điểm <5.")
print("- Bài Kinh doanh chủ yếu tổng hợp và so sánh doanh thu, ít dùng boolean indexing.\n")

print("4. Lợi ích vector hóa so với vòng lặp:")
print("- Thực hiện nhanh hơn nhờ xử lý nguyên khối trên mảng.")
print("- Mã ngắn gọn, dễ đọc, ít lỗi.")
print("- Tận dụng tối ưu C/Fortran bên dưới NumPy.\n")

print("5. Khi dữ liệu tăng gấp 100 lần:")
print("- NumPy vẫn xử lý nhanh nhờ vector hóa, tránh vòng lặp Python chậm.")
print("- Hỗ trợ slicing, boolean indexing, các hàm thống kê tối ưu cho dữ liệu lớn.")
print("- Dễ mở rộng, dự đoán, phân tích dữ liệu lớn.\n")

# -----------------------------
# Minh họa kết quả boolean indexing
# -----------------------------
print("Minh họa boolean indexing Bài Giáo dục:")
print("Sinh viên điểm >=7:", good_students)
print("Sinh viên có ít nhất 1 điểm <5:", low_score_students)

print("\nMinh họa boolean indexing Bài Kinh doanh:")
print("Các ngày có tổng doanh thu > trung bình:", high_days)
