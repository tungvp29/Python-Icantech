import streamlit as st
import pandas as pd

data = pd.read_csv('Data/data5.6_1.csv')
data2 = pd.read_csv('Data/data5.6_2.csv')
st.subheader('Bảng dữ liệu data5.6_1.csv')
st.dataframe(data)

st.write(data.dtypes)

st.subheader('Thông tin về các giá trị thiếu trong data5.6_1.csv')
st.write(data.isnull().sum())
st.write(f'Tổng số dòng trước khi loại bỏ các giá trị None:{data.shape[0]}')

dataNA = data.dropna(subset=['race/ethnicity','gender'])
st.write(f'Tổng số dòng sau khi loại bỏ các giá trị None: {dataNA.shape[0]}') # dòng, cột
st.dataframe(dataNA)

st.dataframe(dataNA['math score'].mode())


st.subheader('Bảng dữ liệu data5.6_2.csv')
st.dataframe(data2)

st.write(data2.dtypes)
# data2 = data2.astype('float')
data2 = data2.astype({
    'reading score':'float',
    'writing score':'float'
    })
st.write(data2.dtypes)
st.write(data2.describe())

st.subheader('Các dòng bị trùng lặp trong data5.6_2.csv')
# st.dataframe(data2.duplicated())
st.dataframe(data2[data2.duplicated()])
st.write(f'Tổng số dòng bị trùng lặp: {data2.duplicated().sum()}')

st.subheader('Bảng dữ liệu data5.6_2.csv sau khi loại bỏ các dòng bị trùng lặp')
data2_no_duplicates = data2.drop_duplicates()
st.dataframe(data2_no_duplicates)
st.write(f'Tổng số dòng sau khi loại bỏ trùng lặp: {data2_no_duplicates.shape[0]}')