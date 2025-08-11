import streamlit as st

contents = ''

with st.form('contact_form'):
    options = ('Email', 'Phone', 'Address', 'Social Media')

    opt = st.selectbox('Chọn phương thức liên lạc', options)

    age = st.slider('Chọn độ tuổi của bạn', 0, 110, 18)

    checked1 = st.checkbox('Tôi đồng ý với các điều khoản và điều kiện')
    # checked2 = st.checkbox('Tôi không đồng ý với các điều khoản và điều kiện')
    # checked3 = st.checkbox('Tôi đang suy nghĩ các điều khoản và điều kiện')
    submitted = st.form_submit_button('Gửi')
    if checked1 and submitted:
        st.write('Cảm ơn bạn đã đồng ý với các điều khoản và điều kiện.')
        st.write(f'Phương thức liên lạc đã chọn: {opt}')
        st.write(f'Độ tuổi của bạn là: {age}')
        contents = f'Phương thức liên lạc: {opt}\nĐộ tuổi: {age}\nĐồng ý với các điều khoản và điều kiện: {checked1}'
    else:
        if not submitted:
            st.warning('Vui lòng gửi thông tin sau khi đồng ý với các điều khoản và điều kiện.')

dl = st.download_button(label='Tải xuống', data=contents, disabled=not checked1,)