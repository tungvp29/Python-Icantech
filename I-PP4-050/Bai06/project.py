import streamlit as st
import time

st.title("Ứng dụng nhập thông tin cá nhân")
pro = 0
tienTrinhNhapDL = st.progress(pro)
name = st.text_input(":memo: Nhập tên: ")
age = st.text_input(":date: Nhập tuổi: ")
address = st.text_input(":house: Nhập địa chỉ: ")
phone = st.text_input(":telephone_receiver: Nhập số điện thoại: ")

if name != "":
    pro += 25
if age != "":
    pro += 25
if address != "":
    pro += 25
if phone != "":
    pro += 25
tienTrinhNhapDL.progress(pro)

button = st.button(":email: Gửi thông tin", 1)
if button:
    if pro == 100:
        sendStatus = 0
        tienTrinhGuiDL = st.progress(sendStatus)         #0 -> 1: float; 0 -> 100: int
        for i in range(100):
            sendStatus += 1
            tienTrinhGuiDL.progress(sendStatus, f"Đang gửi thông tin...{sendStatus}%")
            time.sleep(0.05)

        st.write(f"Cám ơn {name}! Thông tin của bạn đã được gửi thành công.")
        st.write("Dưới đây là nội dung được gửi:")
        st.write(":memo: Họ và tên:", name)
        st.write(":house: Địa chỉ:", address)
        st.write(":telephone_receiver: Số điện thoại:", phone)
        st.write(":date: Tuổi của bạn là:", age)
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