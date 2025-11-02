import streamlit as st
import pandas as pd

df = pd.read_csv('Data/score.csv') #=> trả về DataFrame

arr1 = {
    'STT': 2, 
    'Họ và tên': 'Nguyễn Nguyên Lâm', 
    'Ngày sinh': '03/04/2005', 
    'Lớp': '9A1'
}

st.subheader("Write:")
st.write(df)

st.subheader("Table:")
st.table(df)

st.subheader("DataFrame:")
st.dataframe(df) 