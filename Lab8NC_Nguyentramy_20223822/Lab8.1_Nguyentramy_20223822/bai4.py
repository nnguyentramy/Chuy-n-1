import pandas as pd
import os

def load_data(file_path):
    try:
        # Lấy phần mở rộng
        ext = os.path.splitext(file_path)[1].lower()

        # Xử lý theo loại file
        if ext == '.csv':
            df = pd.read_csv(file_path)
        elif ext == '.xlsx':
            df = pd.read_excel(file_path)
        elif ext == '.json':
            df = pd.read_json(file_path)
        else:
            print(f"❌ Không hỗ trợ định dạng: {ext}")
            return None

        print(f"✅ Đọc thành công file: {file_path}")
        return df

    except Exception as e:
        print(f"❌ Lỗi khi đọc file {file_path}: {e}")
        return None


# ===== TEST HÀM =====

files = [
    'students.csv',
    'scores.xlsx',
    'products.json'
]

for f in files:
    print("\n--- Đang đọc:", f, "---")
    df = load_data(f)

    if df is not None:
        print(df.head())
