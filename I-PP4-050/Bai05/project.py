import streamlit as st

lst = [1, 2, 3, 4, 5]
st.title('Ứng dụng chat trên Streamlit :100:')
st.write("Xin chào! Đây là ứng dụng chat của tôi. :copyright:")

txt = st.text_input('Hãy nhập tên của bạn')

if txt:
    st.write(f'Chào {txt}, bạn có muốn xem danh sách số không?')

