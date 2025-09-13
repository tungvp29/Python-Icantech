import streamlit as st

st.set_page_config(
    page_title="Kiểm tra tính cách", 
    page_icon=":couple:",
    layout="centered",
    initial_sidebar_state="auto")

# st.sidebar.title("Thông tin cá nhân")
with st.sidebar:
    st.title("Thông tin cá nhân")
    st.write("Họ và tên:")
    st.text_input("Nhập họ và tên")

with st.expander("Nội dung", expanded=False, icon="🚨"):
    st.write("đây là nội dung bên trong expander")
    st.write("đây là nội dung bên trong expander")
    st.write("đây là nội dung bên trong expander")
    st.write("đây là nội dung bên trong expander")
    st.write("đây là nội dung bên trong expander")
    st.write("đây là nội dung bên trong expander")
    st.write("đây là nội dung bên trong expander")

col1, col2, col3, col4 = st.columns(4)
with col3:
    st.write("Nội dung chính của trang web")

c1, c2, c3 = st.columns([3, 1, 2], border=True)
with c1:
    st.write("Nội dung chính của trang web")
with c2:
    st.write("Nội dung chính của trang web")
with c3:
    st.write("Nội dung chính của trang web")
