import streamlit as st
import pandas as pd

data = pd.read_scv('bai2.csv')
st.write(data)
st.table(data)
st.dataframe(data)

data = pd.read_csv('currency.csv')
st.write(data)
st.table(data)
st.dataframe(data)