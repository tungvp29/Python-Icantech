import streamlit as st
p = 0
st.progress(p)
ten = st.text_input("Nhập tên của bạn:")
tuoi = st.text_input("Nhập tuổi của bạn:")
dia_chi= st.text_input("Nhập địa chỉ của bạn:")
so_thich = st.text_input("Nhập sở thích của bạn:")
button = st.button("Gửi thông tin")
if ten != "":
    p += 25
if tuoi != "":
    p += 25
if dia_chi != "":
    p += 25
if so_thich != "":
    p += 25
if p != 100:
    st.progress(p)
if button and p == 100:
    st.balloons()
    st.write("Thông tin đã được gửi")
else:
    st.write("Thông tin chưa đủ")