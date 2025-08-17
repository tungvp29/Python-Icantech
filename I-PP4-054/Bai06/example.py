import streamlit as st
import time

bt1 = st.button(label = "Xem thông tin cá nhân", key="button1")
if bt1:
    st.write("Thông tin cá nhân:")
    st.write("Họ và tên: Nguyễn Văn A")
    st.write("Ngày sinh: 01/01/2000")
    st.write("Địa chỉ: Hà Nội, Việt Nam")
    st.write("Sở thích: Đọc sách, Du lịch, Chơi thể thao")

if st.button(label = "Xem thông tin cá nhân", key="button2"):
    st.write("Thông tin cá nhân:")
    st.write("Họ và tên: Trần Thị B")
    st.write("Ngày sinh: 02/02/2001")
    st.write("Địa chỉ: TP. Hồ Chí Minh, Việt Nam")
    st.write("Sở thích: Nấu ăn, Vẽ tranh, Du lịch")

if st.button('Tải dữ liệu'):
    my_bar = st.progress(0, "Đang tải dữ liệu...")
    for i in range(100):
        time.sleep(0.05)
        my_bar.progress(i + 1)

    st.write(f"Đã tải dữ liệu thành công!")
    st.balloons()

thongtin1 = st.text_input("Nhập thông tin cá nhân 1:")
thongtin2 = st.text_input("Nhập thông tin cá nhân 2:")
thongtin3 = st.text_input("Nhập thông tin cá nhân 3:")
thongtin4 = st.text_input("Nhập thông tin cá nhân 4:")
thongtin5 = st.text_input("Nhập thông tin cá nhân 5:")
percent = 0
if len(thongtin1) > 0:
    percent += 20
if len(thongtin2) > 0:
    percent += 20
if len(thongtin3) > 0:
    percent += 20
if len(thongtin4) > 0:
    percent += 20
if len(thongtin5) > 0:
    percent += 20

tienTrinh = st.progress(percent, "Tiến trình nhập thông tin cá nhân")
if percent == 100:
    st.balloons()
    st.success("Bạn đã nhập đầy đủ thông tin cá nhân!")