import streamlit as st
import time 

pro = 0
name = st.text_input("Nhập tên: ")
age = st.text_input("Nhập tuổi: ")
address = st.text_input("Nhập địa chỉ: ")
phone = st.text_input("Nhập số điện thoại: ")

# if len(name) > 0:
#     pro = 25
# if len(age) > 0:
#     pro = 50
# if len(address) > 0:
#     pro = 75
# if len(phone) > 0:
#     pro = 100

if st.button("Nhấn vào đây để xem thông tin name", 'name'):
    st.write(f"Họ và tên :hook: : {name}")
if st.button("Nhấn vào đây để xem thông tin age", 'age'):
    st.write('Chưa có thông tin tuổi')
if st.button("Nhấn vào đây để xem thông tin address", 'address'):
    pass
if st.button("Nhấn vào đây để xem thông tin phone", 'phone'):
    pass

myProgress = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.05)
    myProgress.progress(percent_complete+ 1)

if st.button('click'):
    st.write('Submit thành công')
    st.balloons()