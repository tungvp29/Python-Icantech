import pandas as pd
import numpy as np
import streamlit as st

st.title("Quản lý điểm sinh viên")

st.header("Bài 1: Tạo và thao tác DataFrame")

df = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Name': ['An', 'Bình', 'Chi', 'Dũng', 'Em'],
    'Math': [8.5, 7.0, 9.0, 6.5, 8.0],
    'Physics': [7.5, 8.0, 8.5, 7.0, 9.0]
})

df['Average'] = (df['Math'] + df['Physics']) / 2
df.loc[len(df)] = [6, 'Phúc', 7.5, 8.5, (7.5 + 8.5) / 2]

st.header("Bài 2: Streamlit Application")

st.subheader("Hiển thị DataFrame")

st.write(df)
st.table(df)
st.dataframe(df)

st.subheader("Biểu đồ cột điểm Math")
st.bar_chart(df.set_index('Name')['Math'])

st.header("Bài 3: Data Cleaning và Analysis")

students = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 5, 6, 7],
    'Name': ['An', 'Bình', 'Chi', np.nan, 'Em', 'Em', 'Phúc', 'Giang'],
    'Math': [8.5, 7.0, np.nan, 6.5, 8.0, 8.0, 7.5, 9.0],
    'Physics': [7.5, 8.0, 8.5, 7.0, 9.0, 9.0, 8.5, 8.0]
})

students_clean = students.dropna().drop_duplicates()

st.subheader("Dữ liệu sau khi làm sạch")
st.dataframe(students_clean)

st.subheader("Thống kê")

st.write("Math cao nhất:", students_clean['Math'].max())
st.write("Math thấp nhất:", students_clean['Math'].min())
st.write("Physics trung bình:", students_clean['Physics'].mean())
st.write("Số sinh viên Math >= 8.0:", (students_clean['Math'] >= 8.0).sum())

st.subheader("Lọc dữ liệu")

st.write("Sinh viên có Physics > 8.0")
st.dataframe(students_clean[students_clean['Physics'] > 8.0])

st.write("Sinh viên có điểm Math cao nhất")
st.dataframe(students_clean[students_clean['Math'] == students_clean['Math'].max()])

st.header("Bài 4: Advanced Data Operations")

students_clean['Math'] = students_clean['Math'].astype(float)
students_clean['Physics'] = students_clean['Physics'].astype(float)
students_clean['Average'] = (students_clean['Math'] + students_clean['Physics']) / 2

def grade(avg):
    if avg >= 9.0:
        return 'Xuất sắc'
    elif avg >= 8.0:
        return 'Giỏi'
    elif avg >= 7.0:
        return 'Khá'
    else:
        return 'Trung bình'

students_clean['Grade'] = students_clean['Average'].apply(grade)

st.subheader("Dữ liệu có cột Grade")
st.dataframe(students_clean)

desc = students_clean.describe()
desc = desc.rename(index={
    'count': 'Số lượng',
    'mean': 'Trung bình',
    'std': 'Độ lệch chuẩn',
    'min': 'Nhỏ nhất',
    '25%': '25%',
    '50%': 'Trung vị',
    '75%': '75%',
    'max': 'Lớn nhất'
})

st.subheader("Bảng thống kê mô tả")
st.dataframe(desc)
