
# Bài 1: Tạo và thao tác DataFrame
import pandas as pd
import streamlit as st
import numpy as np
# Thêm tiêu đề và biểu tượng cho trang
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="📊",
)
st.title('Bài làm-Nguyễn Bình Minh')
# Phần a: Tạo DataFrame từ dictionary
sinh_vien = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Tên': ['An', 'Bình', 'Chi', 'Dũng', 'Em'],
    'Toán': [8.5, 7.0, 9.0, 6.5, 8.0],
    'Lý': [7.5, 8.0, 8.5, 7.0, 9.0]
})

# Phần b: Thêm cột 'Trung bình'
sinh_vien['Trung bình'] = sinh_vien[['Toán', 'Lý']].mean(axis=1)

# Phần c: Thêm một sinh viên mới
sinh_vien_moi = {'ID': 6, 'Tên': 'Phúc', 'Toán': 7.5, 'Lý': 8.5, 'Trung bình': (7.5 + 8.5) / 2}
sinh_vien = pd.concat([sinh_vien, pd.DataFrame([sinh_vien_moi])], ignore_index=True)

# Thêm cột 'Average' và sinh viên mới vào DataFrame câu a bài 1
sinh_vien['Average'] = sinh_vien[['Toán', 'Lý']].mean(axis=1)
new_student = {'ID': 6, 'Tên': 'Phúc', 'Toán': 7.5, 'Lý': 8.5, 'Average': (7.5 + 8.5) / 2}
sinh_vien = pd.concat([sinh_vien, pd.DataFrame([new_student])], ignore_index=True)

# Hiển thị DataFrame câu a bài 1
st.write("### DataFrame câu a bài 1")# Thêm 3 gạch ### để hiển thị tiêu đề to ra
st.write(sinh_vien)

# Hiển thị DataFrame sau khi thêm câu b và c
st.write("### DataFrame sau khi thêm câu b và c bài 1")
st.write(sinh_vien)

# Bài 2: Ứng dụng Streamlit
# Phần a: Hiển thị tiêu đề
st.title("Quản lý điểm sinh viên")

# Phần b: Hiển thị DataFrame dưới 3 dạng
st.write("### Dữ liệu sinh viên (write)")
st.write(sinh_vien)

st.write("### Dữ liệu sinh viên (table)")
st.table(sinh_vien)

st.write("### Dữ liệu sinh viên (dataframe)")
st.dataframe(sinh_vien)

# Phần c: Tạo biểu đồ cột hiển thị điểm Toán
st.write("### Biểu đồ điểm Toán")
st.bar_chart(sinh_vien.set_index('Tên')['Toán'])

# Bài 3: Làm sạch dữ liệu và Phân tích
# Tạo DataFrame ban đầu
du_lieu_tho = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 5, 6, 7],
    'Tên': ['An', 'Bình', 'Chi', np.nan, 'Em', 'Em', 'Phúc', 'Giang'],
    'Toán': [8.5, 7.0, np.nan, 6.5, 8.0, 8.0, 7.5, 9.0],
    'Lý': [7.5, 8.0, 8.5, 7.0, 9.0, 9.0, 8.5, 8.0]
})

# Phần a: Làm sạch dữ liệu
du_lieu_sach = du_lieu_tho.dropna().drop_duplicates()

st.write("### Dữ liệu sau khi làm sạch")
st.write(du_lieu_sach)

# Phần b: Tính toán thống kê
toan_cao_nhat = du_lieu_sach['Toán'].max()
toan_thap_nhat = du_lieu_sach['Toán'].min()
ly_trung_binh = du_lieu_sach['Lý'].mean()
toan_tren_8 = du_lieu_sach[du_lieu_sach['Toán'] >= 8.0].shape[0]

# Phần c: Lọc và hiển thị
ly_tren_8 = du_lieu_sach[du_lieu_sach['Lý'] > 8.0]
toan_cao_nhat_sv = du_lieu_sach[du_lieu_sach['Toán'] == toan_cao_nhat]

# Hiển thị kết quả
st.write("### Kết quả phân tích dữ liệu")
st.write(f"Điểm Toán cao nhất: {toan_cao_nhat}")
st.write(f"Điểm Toán thấp nhất: {toan_thap_nhat}")
st.write(f"Điểm Lý trung bình: {ly_trung_binh}")
st.write(f"Số lượng sinh viên có điểm Toán >= 8.0: {toan_tren_8}")

st.write("### Danh sách sinh viên có điểm Lý > 8.0")
st.write(ly_tren_8)

st.write("### Thông tin sinh viên có điểm Toán cao nhất")
st.write(toan_cao_nhat_sv)

# Bài 4: Các thao tác nâng cao
# Sử dụng DataFrame từ Bài 3 (sau khi đã làm sạch)

# Phần a: Chuyển đổi kiểu dữ liệu cột 'Math' và 'Physics' thành float
du_lieu_sach['Toán'] = du_lieu_sach['Toán'].astype(float)
du_lieu_sach['Lý'] = du_lieu_sach['Lý'].astype(float)

# Phần b: Tạo cột 'Grade' dựa trên điểm trung bình
def tinh_xep_loai(tb):
    if tb >= 9.0:
        return 'Xuất sắc'
    elif tb >= 8.0:
        return 'Giỏi'
    elif tb >= 7.0:
        return 'Khá'
    else:
        return 'Trung bình'

du_lieu_sach['Xếp loại'] = du_lieu_sach[['Toán', 'Lý']].mean(axis=1).apply(tinh_xep_loai)

# Phần c: Sử dụng describe() để tạo bảng thống kê và đặt lại tên cho các chỉ số thành tiếng Việt
thong_ke = du_lieu_sach.describe()
thong_ke.rename(index={
    'count': 'Số lượng',
    'mean': 'Giá trị trung bình',
    'std': 'Độ lệch chuẩn',
    'min': 'Giá trị nhỏ nhất',
    '25%': 'Phân vị 25%',
    '50%': 'Phân vị 50%',
    '75%': 'Phân vị 75%',
    'max': 'Giá trị lớn nhất'
}, inplace=True)

st.write("### Bảng thống kê dữ liệu")
st.write(thong_ke)

# Hiển thị dữ liệu sau khi chuyển đổi kiểu dữ liệu
st.write("### Dữ liệu sau khi chuyển đổi kiểu dữ liệu")
st.write(du_lieu_sach)

# Hiển thị câu 1 trước câu 2
st.write("### Câu 1: Tạo và thao tác DataFrame")
st.write(sinh_vien)

# Hiển thị câu 2
st.write("### Câu 2: Ứng dụng Streamlit")
st.write("### Dữ liệu sinh viên (write)")
st.write(sinh_vien)

st.write("### Dữ liệu sinh viên (table)")
st.table(sinh_vien)

st.write("### Dữ liệu sinh viên (dataframe)")
st.dataframe(sinh_vien)

st.write("### Biểu đồ điểm Toán")
st.bar_chart(sinh_vien.set_index('Tên')['Toán'])

# Thêm nút bấm ở cuối (bónus lol)
if st.button("Nhấn vào đây để hoàn thành"):
    st.success("Congratulation! Bạn đã hoàn thành!")