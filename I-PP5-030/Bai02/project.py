import streamlit as st
import pandas as pd

data1 = pd.read_csv('nhatky.csv')

st.title('Nhật ký:')
st.dataframe(data1)

df1 = data1.loc[[0, 1, 2]]
st.write(df1)

df2 = data1.loc[[0, 1, 2], ['Nội dung', 'Cảm xúc']]
st.write(df2)

