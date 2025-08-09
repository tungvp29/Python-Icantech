# ĐỀ KIỂM TRA TỔNG HỢP PYTHON - PANDAS & STREAMLIT
**Khóa học I-PP5-030: Bài 01 - Bài 09**

**Thời gian: 90 phút**  
**Điểm tối đa: 100 điểm**

---

## PHẦN I: TRẮC NGHIỆM (30 điểm)
*Chọn đáp án đúng nhất cho mỗi câu hỏi*

### Câu 1 (3 điểm): Pandas Series và DataFrame
Đoạn code nào sau đây tạo một Series từ dictionary?
```python
A. pd.Series({'a': 1, 'b': 2, 'c': 3})
B. pd.DataFrame({'a': 1, 'b': 2, 'c': 3})
C. pd.Series([1, 2, 3], index=['a', 'b', 'c'])
D. Cả A và C đều đúng
```

### Câu 2 (3 điểm): Đọc file CSV
Lệnh nào được sử dụng để đọc file CSV vào DataFrame?
```python
A. pd.read_file('data.csv')
B. pd.load_csv('data.csv')
C. pd.read_csv('data.csv')
D. pd.import_csv('data.csv')
```

### Câu 3 (3 điểm): Streamlit Display
Trong Streamlit, lệnh nào hiển thị DataFrame dưới dạng bảng tương tác?
```python
A. st.write(df)
B. st.table(df)
C. st.dataframe(df)
D. st.show(df)
```

### Câu 4 (3 điểm): Biểu đồ Streamlit
Lệnh nào tạo biểu đồ cột (bar chart) trong Streamlit?
```python
A. st.line_chart(data, x='col1', y='col2')
B. st.bar_chart(data, x='col1', y='col2')
C. st.area_chart(data, x='col1', y='col2')
D. st.scatter_chart(data, x='col1', y='col2')
```

### Câu 5 (3 điểm): DataFrame Operations
Lệnh nào thêm một dòng mới vào DataFrame?
```python
A. df.add_row(new_data)
B. df.append(new_data, ignore_index=True)
C. df._append(new_data, ignore_index=True)
D. df.insert_row(new_data)
```

### Câu 6 (3 điểm): Data Cleaning
Lệnh nào loại bỏ các dòng trùng lặp trong DataFrame?
```python
A. df.remove_duplicates()
B. df.drop_duplicates()
C. df.delete_duplicates()
D. df.clean_duplicates()
```

### Câu 7 (3 điểm): Data Types
Lệnh nào chuyển đổi kiểu dữ liệu của cột trong DataFrame?
```python
A. df.convert({'col': 'int'})
B. df.astype({'col': 'int'})
C. df.change_type({'col': 'int'})
D. df.to_type({'col': 'int'})
```

### Câu 8 (3 điểm): Statistical Functions
Lệnh nào tính toán thống kê mô tả cho DataFrame?
```python
A. df.statistics()
B. df.summary()
C. df.describe()
D. df.info()
```

### Câu 9 (3 điểm): Data Filtering
Cú pháp nào lọc dữ liệu trong DataFrame theo điều kiện?
```python
A. df.filter(df['col'] > 5)
B. df.where(df['col'] > 5)
C. df[df['col'] > 5]
D. df.select(df['col'] > 5)
```

### Câu 10 (3 điểm): Missing Data
Lệnh nào loại bỏ các dòng có giá trị NaN?
```python
A. df.remove_na()
B. df.dropna()
C. df.delete_na()
D. df.clean_na()
```

---

## PHẦN II: TỰ LUẬN (70 điểm)

### Bài 1 (20 điểm): Tạo và thao tác DataFrame
Viết code Python thực hiện các yêu cầu sau:

**a) (10 điểm)** Tạo một DataFrame từ dictionary với thông tin sinh viên:
- Cột 'ID': [1, 2, 3, 4, 5]
- Cột 'Name': ['An', 'Bình', 'Chi', 'Dũng', 'Em']
- Cột 'Math': [8.5, 7.0, 9.0, 6.5, 8.0]
- Cột 'Physics': [7.5, 8.0, 8.5, 7.0, 9.0]

**b) (5 điểm)** Thêm cột 'Average' tính điểm trung bình của Math và Physics

**c) (5 điểm)** Thêm một sinh viên mới: ID=6, Name='Phúc', Math=7.5, Physics=8.5

### Bài 2 (15 điểm): Streamlit Application
Tạo ứng dụng Streamlit với các chức năng:

**a) (5 điểm)** Hiển thị tiêu đề "Quản lý điểm sinh viên"

**b) (5 điểm)** Hiển thị DataFrame từ Bài 1 dưới 3 dạng: write(), table(), dataframe()

**c) (5 điểm)** Tạo biểu đồ cột (bar chart) hiển thị điểm Math của các sinh viên

### Bài 3 (20 điểm): Data Cleaning và Analysis
Cho DataFrame students với dữ liệu:
```python
import pandas as pd
import numpy as np

students = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 5, 6, 7],
    'Name': ['An', 'Bình', 'Chi', np.nan, 'Em', 'Em', 'Phúc', 'Giang'],
    'Math': [8.5, 7.0, np.nan, 6.5, 8.0, 8.0, 7.5, 9.0],
    'Physics': [7.5, 8.0, 8.5, 7.0, 9.0, 9.0, 8.5, 8.0]
})
```

**a) (8 điểm)** Làm sạch dữ liệu:
- Loại bỏ các dòng có giá trị NaN
- Loại bỏ các dòng trùng lặp

**b) (6 điểm)** Tính toán thống kê:
- Điểm Math cao nhất và thấp nhất
- Điểm Physics trung bình
- Số lượng sinh viên có điểm Math >= 8.0

**c) (6 điểm)** Lọc và hiển thị:
- Danh sách sinh viên có điểm Physics > 8.0
- Thông tin sinh viên có điểm Math cao nhất

### Bài 4 (15 điểm): Advanced Data Operations
Sử dụng DataFrame từ Bài 3 (sau khi đã làm sạch):

**a) (5 điểm)** Chuyển đổi kiểu dữ liệu cột 'Math' và 'Physics' thành float

**b) (5 điểm)** Tạo cột 'Grade' dựa trên điểm trung bình:
- >= 9.0: 'Xuất sắc'
- >= 8.0: 'Giỏi'  
- >= 7.0: 'Khá'
- < 7.0: 'Trung bình'

**c) (5 điểm)** Sử dụng describe() để tạo bảng thống kê và đặt lại tên cho các chỉ số thành tiếng Việt

---

## HƯỚNG DẪN NỘP BÀI

1. **File code**: Tạo file Python (.py) chứa toàn bộ code giải bài tự luận
2. **Screenshots**: Chụp màn hình kết quả chạy chương trình

**Lưu ý**: 
- Code phải chạy được, có comment giải thích
- Streamlit app phải hiển thị đúng yêu cầu
- Nộp đúng thời hạn để đạt điểm tối đa

**Chúc các bạn làm bài tốt!** 🚀📊
