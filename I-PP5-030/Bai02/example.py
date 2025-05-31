import streamlit as st
import pandas as pd

data1 = pd.read_csv('score.csv')
# print(data)
data = [['a', 'b', 'c', 'd'],
        ['e', 'f', 'g', 'h'],
        ['i', 'j', 'k', 'l'],
        ['m', 'n', 'o', 'p']]

st.title('Điểm học sinh:')
st.write(data)
st.table(data)
st.dataframe(data)