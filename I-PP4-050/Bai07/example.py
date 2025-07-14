import streamlit as st

st.set_page_config(
    page_title="Thông tin cá nhân 2", 
    page_icon=":100:", 
    layout="centered",
    initial_sidebar_state="auto")

st.sidebar.write("Sidebar")

with st.sidebar:
    st.title("Sidebar Title")
    st.write("Nội dung sidebar bên trái")
    st.write("Bạn có thể thêm các widget vào đây.")
    

st.title("Ứng dụng nhập thông tin cá nhân")
with st.expander("Hướng dẫn sử dụng"):
    st.write("Vui lòng điền đầy đủ thông tin dưới đây:" * 10)

with st.expander("Thông tin cá nhân"):
    pro = 0
    tienTrinhNhapDL = st.progress(pro)
    name = st.text_input(":memo: Nhập tên: ")
    age = st.text_input(":date: Nhập tuổi: ")
    address = st.text_input(":house: Nhập địa chỉ: ")
    phone = st.text_input(":telephone_receiver: Nhập số điện thoại: ")

cot1, cot2, cot3 = st.columns(3, border=True)
# with cot1:
#     st.write('Nội dung ở cột 1 '* 15)
with cot2:
    st.write('Nội dung ở cột 2 '* 15)
# with cot3:
#     st.write('Nội dung ở cột 3 '* 15)

cot4, cot5, cot6 = st.columns([2, 1, 3], border=True)