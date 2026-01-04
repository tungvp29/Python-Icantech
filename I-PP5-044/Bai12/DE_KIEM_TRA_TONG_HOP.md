# ĐỀ KIỂM TRA TỔNG HỢP PYTHON - PANDAS & STREAMLIT
**Khóa học I-PP5-044: Bài 01 - Bài 09**

**Thời gian: 90 phút**  
**Điểm tối đa: 100 điểm**

---

## PHẦN I: TRẮC NGHIỆM (30 điểm)
*Học sinh hoàn thiện bài trắc nghiệm trên study.icantech.vn*

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
2. **Triển khai**: Đưa chương trình lên streamlit.io, gửi lại link sau khi đã deploy

**Lưu ý**: 
- Code phải chạy được, có comment giải thích
- Streamlit app phải hiển thị đúng yêu cầu
- Nộp đúng thời hạn để đạt điểm tối đa

**Chúc các bạn làm bài tốt!** 🚀📊
