import pandas as pd
import numpy as np


students = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 5, 6, 7],
    'Name': ['An', 'Bình', 'Chi', np.nan, 'Em', 'Em', 'Phúc', 'Giang'],
    'Math': [8.5, 7.0, np.nan, 6.5, 8.0, 8.0, 7.5, 9.0],
    'Physics': [7.5, 8.0, 8.5, 7.0, 9.0, 9.0, 8.5, 8.0]
})

print("=== DATA GỐC ===")
print(students)


cleaned = students.dropna().drop_duplicates()

print("\n=== SAU KHI LÀM SẠCH ===")
print(cleaned)


math_max = cleaned['Math'].max()
math_min = cleaned['Math'].min()
physics_mean = cleaned['Physics'].mean()
count_math_8 = (cleaned['Math'] >= 8.0).sum()

print("\n=== THỐNG KÊ ===")
print(f"Math cao nhất: {math_max}")
print(f"Math thấp nhất: {math_min}")
print(f"Physics trung bình: {physics_mean:.2f}")
print(f"Số SV Math ≥ 8.0: {count_math_8}")


print("\n=== SV PHYSICS > 8.0 ===")
print(cleaned[cleaned['Physics'] > 8.0])

print("\n=== SV CÓ MATH CAO NHẤT ===")
print(cleaned[cleaned['Math'] == math_max])


# Chuyển kiểu dữ liệu
cleaned['Math'] = cleaned['Math'].astype(float)
cleaned['Physics'] = cleaned['Physics'].astype(float)

# Tính điểm trung bình
cleaned['Average'] = (cleaned['Math'] + cleaned['Physics']) / 2

# Xếp loại
def classify(avg):
    if avg >= 9.0:
        return 'Xuất sắc'
    elif avg >= 8.0:
        return 'Giỏi'
    elif avg >= 7.0:
        return 'Khá'
    else:
        return 'Trung bình'

cleaned['Grade'] = cleaned['Average'].apply(classify)

print("\n=== DATA SAU XỬ LÝ NÂNG CAO ===")
print(cleaned)


stats = cleaned[['Math', 'Physics', 'Average']].describe()

stats.rename(index={
    'count': 'Số lượng',
    'mean': 'Trung bình',
    'std': 'Độ lệch chuẩn',
    'min': 'Nhỏ nhất',
    '25%': 'Phân vị 25%',
    '50%': 'Trung vị',
    '75%': 'Phân vị 75%',
    'max': 'Lớn nhất'
}, inplace=True)

print("\n=== BẢNG THỐNG KÊ (TIẾNG VIỆT) ===")
print(stats)
