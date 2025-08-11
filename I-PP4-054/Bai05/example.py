import streamlit as st

st.title("Tiêu đề chương trình")
st.header("Chương trình quản lý cây trồng")
st.subheader("Chức năng chính")
st.write("Hello, Streamlit!")

tree = st.text_input("Nhập tên cây:")
st.text_area("Mô tả cây:")

st.write('Bạn đã nhập tên cây là:', tree)
#print("This is a simple Streamlit app to demonstrate the code structure.")
# input("Nhấn Enter để tiếp tục...")