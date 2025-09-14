import streamlit as st

st.set_page_config(
    page_title="Song Example", 
    page_icon=":musical_note:", 
    layout="wide", 
    initial_sidebar_state="auto")
st.title('Đây là title')
st.header('Đây là header')
st.subheader('Đây là subheader')
st.write("Nội dung này được viết bằng câu lệnh write và nó có thể bao gồm cả hình ảnh, audio, video bên dưới.")

baihat = st.text_input('Nhập tên bài hát:')

st.write('Tên bài hát bạn vừa nhập là: ', baihat)
if st.button('Xác nhận'):
    st.write('Bạn đã xác nhận thông tin bài hát!')

#0 => 100 | 0.0 => 1.0
st.progress(70, text='Đang xử lý...')
# st.balloons()
with st.expander('Thông tin chi tiết'):
    st.write("Đây là nội dung chi tiết của sản phẩm")

st.columns(2)
st.columns([3, 1, 2])
with st.sidebar:
    st.write("Đây là sidebar")  

st.image('https://static.toiimg.com/photo/msid-67586673/67586673.jpg?resizemode=4&width=400', caption='Con mèo', use_container_width=False)