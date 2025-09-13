import streamlit as st

st.set_page_config(page_title='Ứng dụng Chat', page_icon=':speech_balloon:', layout='centered')
st.title('Ứng dụng chat trên Streamlit :100:')
st.header('Hãy nhập tên của bạn và xem danh sách số dưới đây :1234:')
st.subheader('Danh sách số:')
st.write('1, 2, 3, 4, 5')

st.text_input('Hãy nhập tên của bạn')
st.text_area('Hãy nhập tin nhắn của bạn')

if st.button('Gửi tin nhắn'):
    st.success('Tin nhắn đã được gửi!')
button1 = st.button('Xem danh sách số')
if button1:
    st.write('Danh sách số: 1, 2, 3, 4, 5')

value = 0
prog = st.progress(value, "Đang tải dữ liệu...")
if button1:
    value += 10
    prog.progress(value, "Đang tải dữ liệu...")

with st.expander('Thông tin cá nhân', expanded=True):
    st.write('Tên: John Doe')
    st.write('Tuổi: 30')
    st.write('Email: john.doe@example.com')

col1, col2, col3 = st.columns([2, 3, 1], border=True)
with col1:
    st.write('Thông tin thêm 1')
with col2:
    st.write('Thông tin thêm 2')
with col3:
    st.write('Thông tin thêm 3')

st.sidebar.title('Thanh bên')

with st.form('form1'):
    st.text_input('Hãy nhập tên của bạn')
    st.text_area('Hãy nhập tin nhắn của bạn')
    st.form_submit_button('Gửi tin nhắn')
