import streamlit as st


st.write('Chương trình thực đơn yêu thích')

with st.form(key = 'cauhoi1'):
    st.write('Nội dung trong form')

    submited = st.form_submit_button('Gửi')
    if submited:
        st.write('Đã gửi thành công')

# lichTrinh = ['Hà Giang', 'Hà nội', 'Đà Nẵng', 'Nha Trang', 'TP Hồ Chí Minh']
# st.select_slider(
#     'Chọn địa điểm du lịch',
#     options = lichTrinh, 
#     value=['Hà Giang', 'Hà nội']
# )
with st.form(key = 'cauhoi2'):
    list_options = [
        'Sử dụng with st.expander và đặt tiêu đề, nội dung bên trong',
        'Sử dụng ‘with st.expander’ với tham số là tiêu đề và nội dung',
        'Sử dụng ‘st.expander’ với tham số là tiêu đề, và đặt nội dung bên trong',
        'Sử dụng ‘st.expander’ và đặt tiêu đề, nội dung bên trong'
    ]
    
    options = st.multiselect(
        'Câu 2: Để tạo ra một expander với tiêu đề là "Chi tiết sản phẩm", ta phải viết đoạn mã nào?', 
        list_options
    )
    # for option in options:
    st.write('Bạn đã chọn:', options)

    option = st.selectbox('Chọn đáp án đúng', list_options)
    st.write('Bạn đã chọn:', option)


    submited = st.form_submit_button('Gửi')
    if submited:
        st.write('Đã gửi thành công')

st.write('Nội dung bên ngoài form')