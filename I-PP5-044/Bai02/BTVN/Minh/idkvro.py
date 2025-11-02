import streamlit as st
import pandas as pd
st.set_page_config(page_title="Nhật Ký Sigma Gyat", page_icon="🥀", layout="wide")
df = pd.read_csv("sigmaboi.csv")
st.title("Write:")
st.write(df)
st.title("table:")
st.table(df)
st.title("DataFrame:")
st.dataframe(df)
skiidi = st.button("Click me! 🥀")
if skiidi:
    st.success("dop dop dop yes yes")
    st.balloons()