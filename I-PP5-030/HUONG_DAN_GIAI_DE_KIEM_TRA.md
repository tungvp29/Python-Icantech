# HƯỚNG DẪN GIẢI ĐỀ KIỂM TRA TỔNG HỢP PYTHON
**Khóa học I-PP5-030: Bài 01 - Bài 09**

---

## PHẦN I: ĐÁP ÁN TRẮC NGHIỆM (30 điểm)

### Câu 1: **D** - Cả A và C đều đúng
- **Giải thích**: Cả hai cách đều tạo Series với index và values tương ứng

### Câu 2: **C** - pd.read_csv('data.csv')
- **Giải thích**: Đây là hàm chuẩn của pandas để đọc file CSV

### Câu 3: **C** - st.dataframe(df)
- **Giải thích**: st.dataframe() tạo bảng tương tác, st.table() tạo bảng tĩnh

### Câu 4: **B** - st.bar_chart(data, x='col1', y='col2')
- **Giải thích**: st.bar_chart() tạo biểu đồ cột

### Câu 5: **C** - df._append(new_data, ignore_index=True)
- **Giải thích**: _append() là phương thức mới thay thế append() (deprecated)

### Câu 6: **B** - df.drop_duplicates()
- **Giải thích**: Phương thức chuẩn để loại bỏ dòng trùng lặp

### Câu 7: **B** - df.astype({'col': 'int'})
- **Giải thích**: astype() chuyển đổi kiểu dữ liệu

### Câu 8: **C** - df.describe()
- **Giải thích**: describe() tính các thống kê mô tả như mean, std, min, max...

### Câu 9: **C** - df[df['col'] > 5]
- **Giải thích**: Cú pháp boolean indexing để lọc dữ liệu

### Câu 10: **B** - df.dropna()
- **Giải thích**: dropna() loại bỏ các dòng/cột có giá trị NaN

---

## PHẦN II: HƯỚNG DẪN GIẢI TỰ LUẬN (70 điểm)

### Bài 1: Tạo và thao tác DataFrame (20 điểm)

```python
import pandas as pd
import numpy as np

# a) Tạo DataFrame từ dictionary (10 điểm)
students_data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['An', 'Bình', 'Chi', 'Dũng', 'Em'],
    'Math': [8.5, 7.0, 9.0, 6.5, 8.0],
    'Physics': [7.5, 8.0, 8.5, 7.0, 9.0]
}

df_students = pd.DataFrame(students_data)
print("DataFrame ban đầu:")
print(df_students)

# b) Thêm cột 'Average' (5 điểm)
df_students['Average'] = (df_students['Math'] + df_students['Physics']) / 2
print("\nSau khi thêm cột Average:")
print(df_students)

# c) Thêm sinh viên mới (5 điểm)
new_student = {'ID': 6, 'Name': 'Phúc', 'Math': 7.5, 'Physics': 8.5}
new_student['Average'] = (new_student['Math'] + new_student['Physics']) / 2
df_students = df_students._append(new_student, ignore_index=True)
print("\nSau khi thêm sinh viên mới:")
print(df_students)
```

**Chấm điểm:**
- Tạo dictionary đúng cấu trúc: 4 điểm
- Tạo DataFrame: 3 điểm  
- Tính cột Average đúng công thức: 3 điểm
- Thêm dòng mới đúng cú pháp: 4 điểm
- Code chạy được và có kết quả: 3 điểm
- Comment và trình bày rõ ràng: 3 điểm

### Bài 2: Streamlit Application (15 điểm)

```python
import streamlit as st
import pandas as pd

# Tạo DataFrame (sử dụng kết quả từ Bài 1)
students_data = {
    'ID': [1, 2, 3, 4, 5, 6],
    'Name': ['An', 'Bình', 'Chi', 'Dũng', 'Em', 'Phúc'],
    'Math': [8.5, 7.0, 9.0, 6.5, 8.0, 7.5],
    'Physics': [7.5, 8.0, 8.5, 7.0, 9.0, 8.5],
    'Average': [8.0, 7.5, 8.75, 6.75, 8.5, 8.0]
}

df_students = pd.DataFrame(students_data)

# a) Hiển thị tiêu đề (5 điểm)
st.title("Quản lý điểm sinh viên")
st.markdown("---")

# b) Hiển thị DataFrame dưới 3 dạng (5 điểm)
st.subheader("1. Hiển thị bằng st.write()")
st.write(df_students)

st.subheader("2. Hiển thị bằng st.table()")
st.table(df_students)

st.subheader("3. Hiển thị bằng st.dataframe()")
st.dataframe(df_students)

# c) Tạo biểu đồ cột (5 điểm)
st.subheader("4. Biểu đồ điểm Math")
st.bar_chart(df_students, x='Name', y='Math')
```

**Chấm điểm:**
- Import và setup đúng: 2 điểm
- Tiêu đề và cấu trúc: 3 điểm
- 3 cách hiển thị DataFrame: 6 điểm
- Biểu đồ cột hiển thị đúng: 4 điểm

### Bài 3: Data Cleaning và Analysis (20 điểm)

```python
import pandas as pd
import numpy as np
import streamlit as st

# Tạo DataFrame mẫu
students = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 5, 6, 7],
    'Name': ['An', 'Bình', 'Chi', np.nan, 'Em', 'Em', 'Phúc', 'Giang'],
    'Math': [8.5, 7.0, np.nan, 6.5, 8.0, 8.0, 7.5, 9.0],
    'Physics': [7.5, 8.0, 8.5, 7.0, 9.0, 9.0, 8.5, 8.0]
})

print("DataFrame gốc:")
print(students)
print(f"Số dòng ban đầu: {students.shape[0]}")

# a) Làm sạch dữ liệu (8 điểm)
# Loại bỏ dòng có NaN
students_clean = students.dropna()
print(f"\nSau khi loại bỏ NaN: {students_clean.shape[0]} dòng")

# Loại bỏ dòng trùng lặp
students_clean = students_clean.drop_duplicates()
print(f"Sau khi loại bỏ trùng lặp: {students_clean.shape[0]} dòng")

print("\nDataFrame sau khi làm sạch:")
print(students_clean)

# b) Tính toán thống kê (6 điểm)
math_max = students_clean['Math'].max()
math_min = students_clean['Math'].min()
physics_mean = students_clean['Physics'].mean()
math_above_8 = (students_clean['Math'] >= 8.0).sum()

print(f"\nThống kê:")
print(f"Điểm Math cao nhất: {math_max}")
print(f"Điểm Math thấp nhất: {math_min}")
print(f"Điểm Physics trung bình: {physics_mean:.2f}")
print(f"Số sinh viên có Math >= 8.0: {math_above_8}")

# c) Lọc và hiển thị (6 điểm)
# Sinh viên có Physics > 8.0
physics_above_8 = students_clean[students_clean['Physics'] > 8.0]
print(f"\nSinh viên có Physics > 8.0:")
print(physics_above_8)

# Sinh viên có Math cao nhất
top_math_student = students_clean[students_clean['Math'] == math_max]
print(f"\nSinh viên có Math cao nhất:")
print(top_math_student)
```

**Chấm điểm:**
- Sử dụng dropna() đúng: 4 điểm
- Sử dụng drop_duplicates() đúng: 4 điểm
- Tính toán 4 thống kê đúng: 6 điểm
- Lọc dữ liệu đúng điều kiện: 6 điểm

### Bài 4: Advanced Data Operations (15 điểm)

```python
# Sử dụng DataFrame đã làm sạch từ Bài 3
print("DataFrame sau khi làm sạch:")
print(students_clean)
print(f"Kiểu dữ liệu ban đầu:")
print(students_clean.dtypes)

# a) Chuyển đổi kiểu dữ liệu (5 điểm)
students_clean = students_clean.astype({
    'Math': 'float64',
    'Physics': 'float64'
})
print(f"\nKiểu dữ liệu sau khi chuyển đổi:")
print(students_clean.dtypes)

# b) Tạo cột 'Grade' (5 điểm)
def calculate_grade(row):
    avg = (row['Math'] + row['Physics']) / 2
    if avg >= 9.0:
        return 'Xuất sắc'
    elif avg >= 8.0:
        return 'Giỏi'
    elif avg >= 7.0:
        return 'Khá'
    else:
        return 'Trung bình'

students_clean['Average'] = (students_clean['Math'] + students_clean['Physics']) / 2
students_clean['Grade'] = students_clean.apply(calculate_grade, axis=1)

print(f"\nDataFrame với cột Grade:")
print(students_clean)

# c) Tạo bảng thống kê với tên tiếng Việt (5 điểm)
stats = students_clean[['Math', 'Physics', 'Average']].describe()

# Đặt lại tên cho index
stats.index = [
    'Số lượng', 
    'Trung bình', 
    'Độ lệch chuẩn',
    'Giá trị nhỏ nhất',
    'Phân vị 25%',
    'Phân vị 50% (Trung vị)',
    'Phân vị 75%',
    'Giá trị lớn nhất'
]

# Đặt lại tên cho columns
stats.columns = ['Toán', 'Vật lý', 'Điểm TB']

print(f"\nBảng thống kê:")
print(stats)

# Hiển thị trong Streamlit (bonus)
if 'st' in globals():
    st.title("Bảng thống kê điểm số")
    st.dataframe(stats)
```

**Chấm điểm:**
- Chuyển đổi kiểu dữ liệu đúng: 5 điểm
- Logic tính Grade đúng: 3 điểm
- Apply function đúng cách: 2 điểm
- Sử dụng describe(): 2 điểm
- Đặt lại tên index/columns: 3 điểm

---

## CODE HOÀN CHỈNH - FILE SUBMIT

Dưới đây là file code hoàn chỉnh có thể chạy được:

```python
# ket_qua_bai_kiem_tra.py
import pandas as pd
import numpy as np
import streamlit as st

def main():
    st.title("KẾT QUẢ BÀI KIỂM TRA TỔNG HỢP PYTHON")
    st.markdown("**Khóa học I-PP5-030: Bài 01 - Bài 09**")
    st.markdown("---")
    
    # Bài 1: Tạo và thao tác DataFrame
    st.header("Bài 1: Tạo và thao tác DataFrame")
    
    # a) Tạo DataFrame
    students_data = {
        'ID': [1, 2, 3, 4, 5],
        'Name': ['An', 'Bình', 'Chi', 'Dũng', 'Em'],
        'Math': [8.5, 7.0, 9.0, 6.5, 8.0],
        'Physics': [7.5, 8.0, 8.5, 7.0, 9.0]
    }
    
    df_students = pd.DataFrame(students_data)
    st.subheader("a) DataFrame ban đầu:")
    st.dataframe(df_students)
    
    # b) Thêm cột Average
    df_students['Average'] = (df_students['Math'] + df_students['Physics']) / 2
    st.subheader("b) Sau khi thêm cột Average:")
    st.dataframe(df_students)
    
    # c) Thêm sinh viên mới
    new_student = {'ID': 6, 'Name': 'Phúc', 'Math': 7.5, 'Physics': 8.5}
    new_student['Average'] = (new_student['Math'] + new_student['Physics']) / 2
    df_students = df_students._append(new_student, ignore_index=True)
    st.subheader("c) Sau khi thêm sinh viên mới:")
    st.dataframe(df_students)
    
    # Bài 2: Streamlit Application
    st.header("Bài 2: Streamlit Application")
    st.subheader("Quản lý điểm sinh viên")
    
    st.write("**Hiển thị bằng st.write():**")
    st.write(df_students)
    
    st.write("**Hiển thị bằng st.table():**")
    st.table(df_students)
    
    st.write("**Biểu đồ điểm Math:**")
    st.bar_chart(df_students, x='Name', y='Math')
    
    # Bài 3: Data Cleaning và Analysis
    st.header("Bài 3: Data Cleaning và Analysis")
    
    # Tạo DataFrame với dữ liệu bẩn
    students_dirty = pd.DataFrame({
        'ID': [1, 2, 3, 4, 5, 5, 6, 7],
        'Name': ['An', 'Bình', 'Chi', np.nan, 'Em', 'Em', 'Phúc', 'Giang'],
        'Math': [8.5, 7.0, np.nan, 6.5, 8.0, 8.0, 7.5, 9.0],
        'Physics': [7.5, 8.0, 8.5, 7.0, 9.0, 9.0, 8.5, 8.0]
    })
    
    st.subheader("DataFrame gốc (có dữ liệu bẩn):")
    st.dataframe(students_dirty)
    st.write(f"Số dòng ban đầu: {students_dirty.shape[0]}")
    
    # a) Làm sạch dữ liệu
    students_clean = students_dirty.dropna().drop_duplicates()
    st.subheader("a) DataFrame sau khi làm sạch:")
    st.dataframe(students_clean)
    st.write(f"Số dòng sau khi làm sạch: {students_clean.shape[0]}")
    
    # b) Tính toán thống kê
    st.subheader("b) Thống kê:")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Điểm Math cao nhất", students_clean['Math'].max())
        st.metric("Điểm Math thấp nhất", students_clean['Math'].min())
    
    with col2:
        st.metric("Điểm Physics trung bình", f"{students_clean['Physics'].mean():.2f}")
        st.metric("Số SV có Math >= 8.0", (students_clean['Math'] >= 8.0).sum())
    
    # c) Lọc và hiển thị
    st.subheader("c) Lọc dữ liệu:")
    
    physics_above_8 = students_clean[students_clean['Physics'] > 8.0]
    st.write("**Sinh viên có Physics > 8.0:**")
    st.dataframe(physics_above_8)
    
    math_max = students_clean['Math'].max()
    top_math = students_clean[students_clean['Math'] == math_max]
    st.write("**Sinh viên có Math cao nhất:**")
    st.dataframe(top_math)
    
    # Bài 4: Advanced Data Operations
    st.header("Bài 4: Advanced Data Operations")
    
    # a) Chuyển đổi kiểu dữ liệu
    students_final = students_clean.copy()
    students_final = students_final.astype({
        'Math': 'float64',
        'Physics': 'float64'
    })
    
    st.subheader("a) Kiểu dữ liệu sau chuyển đổi:")
    st.write(students_final.dtypes)
    
    # b) Tạo cột Grade
    def calculate_grade(row):
        avg = (row['Math'] + row['Physics']) / 2
        if avg >= 9.0:
            return 'Xuất sắc'
        elif avg >= 8.0:
            return 'Giỏi'
        elif avg >= 7.0:
            return 'Khá'
        else:
            return 'Trung bình'
    
    students_final['Average'] = (students_final['Math'] + students_final['Physics']) / 2
    students_final['Grade'] = students_final.apply(calculate_grade, axis=1)
    
    st.subheader("b) DataFrame với cột Grade:")
    st.dataframe(students_final)
    
    # c) Bảng thống kê tiếng Việt
    stats = students_final[['Math', 'Physics', 'Average']].describe()
    stats.index = [
        'Số lượng', 'Trung bình', 'Độ lệch chuẩn', 'GTNN',
        'Phân vị 25%', 'Phân vị 50%', 'Phân vị 75%', 'GTLN'
    ]
    stats.columns = ['Toán', 'Vật lý', 'Điểm TB']
    
    st.subheader("c) Bảng thống kê (tiếng Việt):")
    st.dataframe(stats)

if __name__ == "__main__":
    main()
```

---

## TIÊU CHÍ CHẤM ĐIỂM

### Phần Trắc nghiệm (30 điểm):
- Mỗi câu đúng: 3 điểm
- Tổng: 10 câu × 3 điểm = 30 điểm

### Phần Tự luận (70 điểm):

**Bài 1 (20 điểm):**
- Tạo DataFrame đúng: 10 điểm
- Thêm cột Average: 5 điểm  
- Thêm dòng mới: 5 điểm

**Bài 2 (15 điểm):**
- Tiêu đề và cấu trúc: 5 điểm
- 3 cách hiển thị: 5 điểm
- Biểu đồ: 5 điểm

**Bài 3 (20 điểm):**
- Data cleaning: 8 điểm
- Thống kê: 6 điểm
- Lọc dữ liệu: 6 điểm

**Bài 4 (15 điểm):**
- Chuyển đổi kiểu: 5 điểm
- Tạo cột Grade: 5 điểm
- Bảng thống kê: 5 điểm

### Điểm thưởng:
- Code chạy được hoàn toàn: +5 điểm
- Comment đầy đủ, code sạch: +3 điểm
- Streamlit app đẹp, có styling: +2 điểm

**Tổng điểm tối đa: 110 điểm (chuẩn hóa về 100)**
