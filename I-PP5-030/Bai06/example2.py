import pandas as pd
import streamlit as st

filename = 'data5.6_1.csv'
df = pd.read_csv(f'Data/{filename}')

st.dataframe(df)

st.write(df.isnull().sum())

df = df.dropna()
st.dataframe(df)