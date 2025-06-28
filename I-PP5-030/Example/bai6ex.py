import pandas as pd
import streamlit as st

#Bảng dữ liệu 6_1
filename1 = 'data5.6_1.csv'
df = pd.read_csv(filename1)
st.title('Xử lý bảng dữ liệu 6_1')
missedData = df.isnull().sum()
#set column name for missedData
missedData.name = 'Số lượng dữ liệu bị thiếu'
st.write('Thống kê số lượng dữ liệu bị thiếu trong mỗi cột:')
st.dataframe(missedData)

df = df.dropna()
st.write('Bảng dữ liệu sau khi loại bỏ các dòng có dữ liệu bị thiếu:')
st.dataframe(df)

#Bảng dữ liệu 6_2
filename2 = 'data5.6_2.csv'
df2 = pd.read_csv(filename2)
st.title('Xử lý bảng dữ liệu 6_2')
st.write('Định dạng dữ liệu:')

df2 = df2.astype({'math score': 'float'})
st.write(df2.dtypes)
st.write(f'Số dữ liệu trùng lặp: {df2.duplicated().sum()}')
st.write(df2[df2.duplicated()])
st.write('Bảng dữ liệu sau khi loại bỏ các dòng trùng lặp:')
df2 = df2.drop_duplicates()
st.dataframe(df2)