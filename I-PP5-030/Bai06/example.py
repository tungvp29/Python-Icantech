import pandas as pd
import streamlit as st

filename = 'data5.6_2.csv'
df = pd.read_csv(f'Data/{filename}')
# print(df.dtypes)

st.write('Kiểu dữ liệu')
st.write(df.dtypes)
st.write('Bảng dữ liệu gốc:')
st.dataframe(df)
df = df.astype({'math score': 'float'})
# st.write(df.dtypes)

# st.write(df.duplicated())
st.write('Bảng dữ liệu bị trùng lặp:')
st.write(df[df.duplicated()])
st.write(f'Số lượng dữ liệu trùng lặp: {df.duplicated().sum()}')

st.write('Bảng dữ liệu sau khi loại bỏ các dòng trùng lặp:')
df = df.drop_duplicates()
st.dataframe(df)
st.write(f'Số dòng dữ liệu: {df.shape[0]}')