import streamlit as st
import time

name = st.text_input("Nhập tên của bạn: ")
button = st.button("Click me", 1)
if button:
    st.write("Xin chào!", name)

st.button("Click me", 'nut2')

pro = 0
myProgress = st.progress(pro)         #0 -> 1: float; 0 -> 100: int
for i in range(100):
    pro += 1
    myProgress.progress(pro)
    time.sleep(0.05)

button2 = st.button("Bóng bay này!", 'nut3')
if button2:
    st.balloons()
