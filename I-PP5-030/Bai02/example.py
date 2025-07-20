import streamlit as st
import pandas as pd

data1 = pd.read_csv('score.csv')   #dataframe
# print(data)
data = [['a', 'b', 'c', 'd'],
        ['e', 'f', 'g', 'h'],
        ['i', 'j', 'k', 'l'],
        ['m', 'n', 'o', 'p']]

st.title('Điểm học sinh:')

st.write('Câu lệnh write() hiển thị dữ liệu dưới dạng văn bản')
st.write(data1)

st.write('Câu lệnh table() hiển thị dữ liệu dưới dạng bảng')
st.table(data1)

st.write('Câu lệnh dataframe() hiển thị dữ liệu dưới dạng bảng có thể tương tác')
st.dataframe(data1)