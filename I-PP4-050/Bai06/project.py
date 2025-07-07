import streamlit as st
import time

st.title("Ứng dụng nhập thông tin cá nhân :100:")
pro = 0
myProgress = st.progress(pro)
name = st.text_input("Nhập tên: ")
age = st.text_input("Nhập tuổi: ")
address = st.text_input("Nhập địa chỉ: ")
phone = st.text_input("Nhập số điện thoại: ")

if name != "":
    pro += 25
if age != "":
    pro += 25
if address != "":
    pro += 25
if phone != "":
    pro += 25
myProgress.progress(pro)

button = st.button("Gửi thông tin", 1)
if button:
    if pro == 100:
        sendStatus = 0
        sendProgress = st.progress(sendStatus)         #0 -> 1: float; 0 -> 100: int
        for i in range(100):
            sendStatus += 1
            sendProgress.progress(sendStatus, f"Đang gửi thông tin...{sendStatus}%")
            time.sleep(0.05)

        st.write(f"Cám ơn {name}! Thông tin của bạn đã được gửi thành công.")
        st.write("Dưới đây là nội dung được gửi:")
        st.write("Họ và tên:", name)
        st.write("Địa chỉ:", address)
        st.write("Số điện thoại:", phone)
        st.write("Tuổi của bạn là:", age)
        st.balloons()
    else:
        st.error("Vui lòng điền đầy đủ thông tin trước khi gửi.")
        st.write("Bạn cần hoàn thành các trường sau:")
        if name == "":
            st.write("- Tên")
        if age == "":
            st.write("- Tuổi")
        if address == "":
            st.write("- Địa chỉ")
        if phone == "":
            st.write("- Số điện thoại")