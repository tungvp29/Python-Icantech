import pandas as pd
import streamlit as st

data = pd.read_csv('Data/data8.1.csv')
st.dataframe(data)
data2 = pd.read_csv('Data/data8.2.csv')
st.dataframe(data2)