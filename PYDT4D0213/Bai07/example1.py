import streamlit as st
import time

st.set_page_config(page_title="Bài 07", page_icon=":smile:", layout="wide")

#Nội dung
with st.expander('Thông tin cá nhân'):
    name = st.text_input("Nhập tên: ")
    age = st.text_input("Nhập tuổi: ")

with st.expander('Thông tin liên hệ'):
    address = st.text_input("Nhập địa chỉ: ")
    phone = st.text_input("Nhập số điện thoại: ")

#Chia cột trên giao diện
col1, col2, col3 = st.columns([3, 3, 3])
with col1:
    st.header('A cat')
    st.write('Con mèo')
    st.image('https://static.toiimg.com/photo/msid-67586673/67586673.jpg?resizemode=4&width=400')

with col2:
    st.header('A owl')
    st.write('Con cú')
    st.image('https://static.toiimg.com/photo/msid-67586673/67586673.jpg?resizemode=4&width=400')

with col3:
    st.header('A dog')
    st.write('Con chó')
    st.image('https://static.toiimg.com/photo/msid-67586673/67586673.jpg?resizemode=4&width=400')

#Sidebar
with st.sidebar.title('Sidebar'):
    st.sidebar.write('Con mèo')
    st.sidebar.write('Con cú')
    st.sidebar.write('Con chó')
    st.image('https://th.bing.com/th/id/OIP.vGOfkcKApkhwUhqfTxV_nQHaEI?rs=1&pid=ImgDetMain')
    


pro = 0
if len(name) > 0:
    pro += 25
if len(age) > 0:
    pro += 25
if len(address) > 0:
    pro += 25
if len(phone) > 0:
    pro += 25

myProgress = st.progress(pro)

if st.button('click'):
    st.write('Submit thành công')
    st.balloons()