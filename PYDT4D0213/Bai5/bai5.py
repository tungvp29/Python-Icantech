import streamlit as st
from btvn_bai1 import Student           #btvn_bai1 là tên file chứa class Student

std = Student()
std.name = 'Vũ Phạm Tùng'
std.group = 'PYDT4D0213'
std.scores = {'Toán': 10, 'Lý': 9, 'Hóa': 8}

st.title("Giới thiệu bản thân")
st.write(f"Họ và tên :hook: : {std.name}")
st.write(f"Lớp :placard: : {std.group}")
st.write(f"Điểm cao nhất: {std.DiemCaoNhat()}")
st.write(f"Xếp hạng: {std.xephang()}")