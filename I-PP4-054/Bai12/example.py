import streamlit as st

st.text_input("Nhập tên của bạn:")
st.text_area("Nhập mô tả về bạn:")

st.columns(3)
st.columns([0.5, 1, 2], border=True)

st.button(label="Click me!")