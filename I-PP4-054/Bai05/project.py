#Tạo chương trình:
#có 4 ô nhập liệu, lấy thông tin tên, ngày sinh, môn học, sở thích từ phía người dùng
#kiểm tra người dùng đã nhập đủ 4 thông chưa
#nếu đủ rồi thì in lại thông tin lên màn hình, chưa đủ thì thông báo người dùng cần nhập bổ sung

import streamlit as st

st.title("Chương trình giới thiệu bản thân")
name = st.text_input("Nhập tên của bạn:")
dob = st.date_input("Nhập ngày sinh của bạn:")
monhoc = st.text_input("Nhập môn học yêu thích của bạn:")
sothich = st.text_input("Nhập sở thích của bạn:")

if len(name) > 0 and dob and len(monhoc) > 0 and len(sothich) > 0:
    st.subheader("Thông tin của bạn:")
    st.write(f"Tên: {name}")
    st.write(f"Ngày sinh: {dob}")
    st.write(f"Môn học yêu thích: {monhoc}")
    st.write(f"Sở thích: {sothich}")
else:
    st.warning("Vui lòng nhập đầy đủ thông tin vào tất cả các ô.")