import streamlit as st
import pandas as pd
#chinh duogn dan toi file csv
data = pd.read_csv('../Data/data5.6_1.csv')

st.subheader("Bảng dữ liệu ban đầu")
st.dataframe(data)

st.subheader("Thông tin về các giá trị bị thiếu trong data5.6_1.csv")
st.write("Số lượng giá trị bị thiếu theo từng cột:")
st.dataframe(data.isnull().sum())
st.write(f"Tổng số dòng trước khi loại bỏ các giá trị None: {data.shape[0]}")

data_cleaned = data.dropna(subset=['race/ethnicity', 'gender'])
st.write(f"Tổng số dòng sau khi loại bỏ các giá trị None: {data_cleaned.shape[0]}")
st.subheader("Bảng dữ liệu sau khi loại bỏ các giá trị None")
st.dataframe(data_cleaned)

st.subheader("Kiểm tra các dòng bị trùng lặp")
duplicates = data_cleaned.duplicated()
st.write(f"Tổng số dòng bị trùng lặp: {duplicates.sum()}")

data_no_duplicates = data_cleaned.drop_duplicates()
st.write(f"Tổng số dòng sau khi loại bỏ các dòng trùng lặp: {data_no_duplicates.shape[0]}")
st.subheader("Bảng dữ liệu sau khi loại bỏ các dòng trùng lặp")
st.dataframe(data_no_duplicates)

#chinh duong   toi file csv
data2 = pd.read_csv('../Data/data5.6_2.csv')

st.subheader("Bảng dữ liệu ban đầu (data5.6.2.csv)")
st.dataframe(data2)

st.subheader("Kiểu dữ liệu của các cột")
st.write(data2.dtypes)

st.subheader("Thông tin về các giá trị bị thiếu")
st.write("Số lượng giá trị bị thiếu theo từng cột:")
st.dataframe(data2.isnull().sum())
st.write(f"Tổng số dòng trước khi xử lý: {data2.shape[0]}")

data2_cleaned = data2.dropna()
st.write(f"Tổng số dòng sau khi loại bỏ các giá trị bị thiếu: {data2_cleaned.shape[0]}")
st.subheader("Bảng dữ liệu sau khi loại bỏ các giá trị bị thiếu")
st.dataframe(data2_cleaned)

st.subheader("Kiểm tra các dòng bị trùng lặp")
duplicates = data2_cleaned.duplicated()
st.write(f"Tổng số dòng bị trùng lặp: {duplicates.sum()}")
