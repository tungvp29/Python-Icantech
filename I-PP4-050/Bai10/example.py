import streamlit as st

tinhTP = ['Hà Giang', 'Hà Nội', 'Đà Nẵng', 'Nha Trang', 'TP Hồ Chí Minh']

with st.form(key = 'thongtin'):
    name = st.text_input('Nhập tên của bạn:', key='name')
    email = st.text_input('Nhập email của bạn:', key='email')
    phone = st.text_input('Nhập số điện thoại của bạn:', key='phone')
    
    options = st.multiselect('Chọn tỉnh thành phố bạn muốn đến:',tinhTP)

    opt = st.selectbox('Chọn tỉnh thành phố bạn muốn đến:', tinhTP)
    st.select_slider(
        label='Chọn tỉnh thành phố bạn muốn đến:',
        options=tinhTP,
        value=('Hà Giang', 'Hà Nội')
    )

    submit_button = st.form_submit_button(label='Gửi thông tin')
    if submit_button:
        with st.spinner('Đang gửi thông tin...'):
            import time
            time.sleep(2)
        with st.expander('Thông tin đã gửi'):
            st.write(f'Tên: {name}')
            st.write(f'Email: {email}')
            st.write(f'Số điện thoại: {phone}')
            for tp in options:
                st.write(f'Tỉnh/Thành phố: {tp}')

        st.success('Thông tin đã được gửi thành công!')


