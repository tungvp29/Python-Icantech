#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ĐÁP ÁN HOÀN CHỈNH - ĐỀ KIỂM TRA TỔNG HỢP PYTHON
Khóa học I-PP5-030: Bài 01 - Bài 09

File này chứa toàn bộ code giải đề kiểm tra
Chạy: streamlit run dap_an_de_kiem_tra.py
"""

import pandas as pd
import numpy as np
import streamlit as st

def main():
    # Cấu hình trang
    st.set_page_config(
        page_title="Đề Kiểm Tra Python",
        page_icon="📊",
        layout="wide"
    )
    
    # Header
    st.title("📊 ĐÁP ÁN ĐỀ KIỂM TRA TỔNG HỢP PYTHON")
    st.markdown("**Khóa học I-PP5-030: Bài 01 - Bài 09**")
    st.markdown("---")
    
    # Sidebar với điều hướng
    st.sidebar.title("Điều hướng")
    selected_section = st.sidebar.selectbox(
        "Chọn phần cần xem:",
        ["Tổng quan", "Bài 1", "Bài 2", "Bài 3", "Bài 4", "Kết luận"]
    )
    
    if selected_section == "Tổng quan":
        show_overview()
    elif selected_section == "Bài 1":
        show_bai_1()
    elif selected_section == "Bài 2":
        show_bai_2()
    elif selected_section == "Bài 3":
        show_bai_3()
    elif selected_section == "Bài 4":
        show_bai_4()
    elif selected_section == "Kết luận":
        show_conclusion()

def show_overview():
    st.header("📋 Tổng quan đề kiểm tra")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Phần Trắc nghiệm (30 điểm)")
        st.markdown("""
        **Đáp án:**
        1. D - Cả A và C đều đúng
        2. C - pd.read_csv('data.csv')
        3. C - st.dataframe(df)
        4. B - st.bar_chart(data, x='col1', y='col2')
        5. C - df._append(new_data, ignore_index=True)
        6. B - df.drop_duplicates()
        7. B - df.astype({'col': 'int'})
        8. C - df.describe()
        9. C - df[df['col'] > 5]
        10. B - df.dropna()
        """)
    
    with col2:
        st.subheader("Phần Tự luận (70 điểm)")
        st.markdown("""
        **Cấu trúc:**
        - **Bài 1 (20đ):** Tạo và thao tác DataFrame
        - **Bài 2 (15đ):** Streamlit Application  
        - **Bài 3 (20đ):** Data Cleaning & Analysis
        - **Bài 4 (15đ):** Advanced Data Operations
        
        **Kiến thức chính:**
        - Pandas Series, DataFrame
        - Streamlit components
        - Data visualization
        - Data cleaning techniques
        - Statistical analysis
        """)

def show_bai_1():
    st.header("📝 Bài 1: Tạo và thao tác DataFrame (20 điểm)")
    
    # a) Tạo DataFrame
    st.subheader("a) Tạo DataFrame từ dictionary (10 điểm)")
    
    with st.expander("Xem code"):
        st.code("""
students_data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['An', 'Bình', 'Chi', 'Dũng', 'Em'],
    'Math': [8.5, 7.0, 9.0, 6.5, 8.0],
    'Physics': [7.5, 8.0, 8.5, 7.0, 9.0]
}

df_students = pd.DataFrame(students_data)
        """)
    
    students_data = {
        'ID': [1, 2, 3, 4, 5],
        'Name': ['An', 'Bình', 'Chi', 'Dũng', 'Em'],
        'Math': [8.5, 7.0, 9.0, 6.5, 8.0],
        'Physics': [7.5, 8.0, 8.5, 7.0, 9.0]
    }
    
    df_students = pd.DataFrame(students_data)
    st.dataframe(df_students)
    
    # b) Thêm cột Average
    st.subheader("b) Thêm cột Average (5 điểm)")
    
    with st.expander("Xem code"):
        st.code("""
df_students['Average'] = (df_students['Math'] + df_students['Physics']) / 2
        """)
    
    df_students['Average'] = (df_students['Math'] + df_students['Physics']) / 2
    st.dataframe(df_students)
    df_students
    # c) Thêm sinh viên mới
    st.subheader("c) Thêm sinh viên mới (5 điểm)")
    
    with st.expander("Xem code"):
        st.code("""
new_student = {'ID': 6, 'Name': 'Phúc', 'Math': 7.5, 'Physics': 8.5}
new_student['Average'] = (new_student['Math'] + new_student['Physics']) / 2
df_students = df_students._append(new_student, ignore_index=True)
        """)
    
    new_student = {'ID': 6, 'Name': 'Phúc', 'Math': 7.5, 'Physics': 8.5}
    new_student['Average'] = (new_student['Math'] + new_student['Physics']) / 2
    df_students = df_students._append(new_student, ignore_index=True)
    st.dataframe(df_students)
    
    # Lưu vào session state để dùng cho bài khác
    st.session_state.df_students = df_students

def show_bai_2():
    st.header("🌐 Bài 2: Streamlit Application (15 điểm)")
    
    # Lấy DataFrame từ session state hoặc tạo mới
    if 'df_students' in st.session_state:
        df_students = st.session_state.df_students
    else:
        students_data = {
            'ID': [1, 2, 3, 4, 5, 6],
            'Name': ['An', 'Bình', 'Chi', 'Dũng', 'Em', 'Phúc'],
            'Math': [8.5, 7.0, 9.0, 6.5, 8.0, 7.5],
            'Physics': [7.5, 8.0, 8.5, 7.0, 9.0, 8.5],
            'Average': [8.0, 7.5, 8.75, 6.75, 8.5, 8.0]
        }
        df_students = pd.DataFrame(students_data)
    
    # a) Tiêu đề
    st.subheader("a) Tiêu đề (5 điểm)")
    st.markdown("### 🎓 Quản lý điểm sinh viên")
    
    # b) Hiển thị DataFrame 3 cách
    st.subheader("b) Hiển thị DataFrame dưới 3 dạng (5 điểm)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**st.write():**")
        st.write(df_students)
    
    with col2:
        st.write("**st.table():**")
        st.table(df_students)
    
    with col3:
        st.write("**st.dataframe():**")
        st.dataframe(df_students)
    
    # c) Biểu đồ
    st.subheader("c) Biểu đồ cột điểm Math (5 điểm)")
    
    with st.expander("Xem code"):
        st.code("st.bar_chart(df_students, x='Name', y='Math')")
    
    st.bar_chart(df_students, x='Name', y='Math')

def show_bai_3():
    st.header("🧹 Bài 3: Data Cleaning và Analysis (20 điểm)")
    
    # Tạo DataFrame bẩn
    st.subheader("DataFrame gốc (có dữ liệu bẩn)")
    
    students_dirty = pd.DataFrame({
        'ID': [1, 2, 3, 4, 5, 5, 6, 7],
        'Name': ['An', 'Bình', 'Chi', np.nan, 'Em', 'Em', 'Phúc', 'Giang'],
        'Math': [8.5, 7.0, np.nan, 6.5, 8.0, 8.0, 7.5, 9.0],
        'Physics': [7.5, 8.0, 8.5, 7.0, 9.0, 9.0, 8.5, 8.0]
    })
    
    st.dataframe(students_dirty)
    st.write(f"📊 Số dòng ban đầu: {students_dirty.shape[0]}")
    
    # a) Làm sạch dữ liệu
    st.subheader("a) Làm sạch dữ liệu (8 điểm)")
    
    with st.expander("Xem code làm sạch"):
        st.code("""
# Loại bỏ dòng có NaN
students_clean = students_dirty.dropna()

# Loại bỏ dòng trùng lặp  
students_clean = students_clean.drop_duplicates()
        """)
    
    students_clean = students_dirty.dropna().drop_duplicates()
    st.dataframe(students_clean)
    st.write(f"📊 Số dòng sau khi làm sạch: {students_clean.shape[0]}")
    
    # b) Tính toán thống kê
    st.subheader("b) Tính toán thống kê (6 điểm)")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Math cao nhất", students_clean['Math'].max())
    with col2:
        st.metric("Math thấp nhất", students_clean['Math'].min())
    with col3:
        st.metric("Physics TB", f"{students_clean['Physics'].mean():.2f}")
    with col4:
        st.metric("Math >= 8.0", (students_clean['Math'] >= 8.0).sum())
    
    # c) Lọc và hiển thị
    st.subheader("c) Lọc và hiển thị (6 điểm)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Sinh viên có Physics > 8.0:**")
        physics_above_8 = students_clean[students_clean['Physics'] > 8.0]
        st.dataframe(physics_above_8)
    
    with col2:
        st.write("**Sinh viên có Math cao nhất:**")
        math_max = students_clean['Math'].max()
        top_math = students_clean[students_clean['Math'] == math_max]
        st.dataframe(top_math)
    
    # Lưu vào session state
    st.session_state.students_clean = students_clean

def show_bai_4():
    st.header("⚙️ Bài 4: Advanced Data Operations (15 điểm)")
    
    # Lấy DataFrame đã làm sạch
    if 'students_clean' in st.session_state:
        students_clean = st.session_state.students_clean
    else:
        # Tạo DataFrame mẫu nếu chưa có
        students_clean = pd.DataFrame({
            'ID': [1, 2, 5, 6, 7],
            'Name': ['An', 'Bình', 'Em', 'Phúc', 'Giang'],
            'Math': [8.5, 7.0, 8.0, 7.5, 9.0],
            'Physics': [7.5, 8.0, 9.0, 8.5, 8.0]
        })
    
    # a) Chuyển đổi kiểu dữ liệu
    st.subheader("a) Chuyển đổi kiểu dữ liệu (5 điểm)")
    
    st.write("**Kiểu dữ liệu ban đầu:**")
    st.write(students_clean.dtypes)
    
    with st.expander("Xem code chuyển đổi"):
        st.code("""
students_clean = students_clean.astype({
    'Math': 'float64',
    'Physics': 'float64'
})
        """)
    
    students_final = students_clean.copy()
    students_final = students_final.astype({
        'Math': 'float64',
        'Physics': 'float64'
    })
    
    st.write("**Kiểu dữ liệu sau chuyển đổi:**")
    st.write(students_final.dtypes)
    
    # b) Tạo cột Grade
    st.subheader("b) Tạo cột Grade (5 điểm)")
    
    with st.expander("Xem code tạo Grade"):
        st.code("""
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
        """)
    
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
    
    st.dataframe(students_final)
    
    # c) Bảng thống kê tiếng Việt
    st.subheader("c) Bảng thống kê với tên tiếng Việt (5 điểm)")
    
    with st.expander("Xem code thống kê"):
        st.code("""
stats = students_final[['Math', 'Physics', 'Average']].describe()

stats.index = [
    'Số lượng', 'Trung bình', 'Độ lệch chuẩn', 'GTNN',
    'Phân vị 25%', 'Phân vị 50%', 'Phân vị 75%', 'GTLN'
]
stats.columns = ['Toán', 'Vật lý', 'Điểm TB']
        """)
    
    stats = students_final[['Math', 'Physics', 'Average']].describe()
    
    stats.index = [
        'Số lượng', 'Trung bình', 'Độ lệch chuẩn', 'GTNN',
        'Phân vị 25%', 'Phân vị 50%', 'Phân vị 75%', 'GTLN'
    ]
    stats.columns = ['Toán', 'Vật lý', 'Điểm TB']
    
    st.dataframe(stats)
    
    # Biểu đồ phân bố điểm
    st.subheader("📊 Biểu đồ phân bố điểm")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.bar_chart(students_final, x='Name', y=['Math', 'Physics'])
    
    with col2:
        # Biểu đồ phân bố Grade
        grade_counts = students_final['Grade'].value_counts()
        st.bar_chart(grade_counts)

def show_conclusion():
    st.header("🎯 Kết luận và Đánh giá")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Tóm tắt điểm số")
        st.markdown("""
        **Phần Trắc nghiệm (30 điểm):**
        - 10 câu hỏi về pandas và streamlit cơ bản
        - Mỗi câu 3 điểm
        
        **Phần Tự luận (70 điểm):**
        - Bài 1: DataFrame operations (20đ)
        - Bài 2: Streamlit components (15đ)  
        - Bài 3: Data cleaning & analysis (20đ)
        - Bài 4: Advanced operations (15đ)
        """)
    
    with col2:
        st.subheader("🎓 Kiến thức đã kiểm tra")
        st.markdown("""
        **Pandas:**
        - Series và DataFrame
        - Đọc/ghi file CSV
        - Data cleaning (dropna, drop_duplicates)
        - Data analysis (describe, filtering)
        - Data types conversion
        
        **Streamlit:**
        - Hiển thị dữ liệu (write, table, dataframe)
        - Tạo biểu đồ (bar_chart, line_chart)
        - Layout và components
        """)
    
    st.subheader("💡 Lời khuyên cho học viên")
    st.success("""
    **Để đạt điểm cao:**
    - Nắm vững cú pháp pandas cơ bản
    - Thực hành nhiều với DataFrame operations
    - Hiểu rõ các phương thức data cleaning
    - Biết cách tạo ứng dụng Streamlit đơn giản
    - Code sạch, có comment, chạy được
    """)
    
    st.info("""
    **Tài liệu tham khảo:**
    - Pandas Documentation: https://pandas.pydata.org/docs/
    - Streamlit Documentation: https://docs.streamlit.io/
    - Python Data Analysis: Wes McKinney
    """)

if __name__ == "__main__":
    main()
