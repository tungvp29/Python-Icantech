import streamlit as st

loginInfomationString = ''
with st.form(key='login', clear_on_submit=True):
    username = st.text_input('Username:')
    password = st.text_input('Password:', type='password')
    remember_me = st.checkbox('Ghi nhớ tài khoản')
    if st.form_submit_button('Login'):
        loginInfomationString = f'Username: {username}, Password: {password}, Remember me: {remember_me}'

st.download_button('Download login information', loginInfomationString, file_name='login.txt')

with st.form(key='form1', clear_on_submit=True):
    st.subheader('Trả lời câu hỏi sau:')
    st.write('**1. Bạn thích học lập trình không?**')
    st.radio('Chọn một:', ['Có', 'Không'])
    st.write('**2. Bạn thích học ngôn ngữ lập trình nào?**')
    check1 = st.checkbox('Python')
    check2 = st.checkbox('JavaScript')
    check3 = st.checkbox('Java')
    check4 = st.checkbox('C++')
    check5 = st.checkbox('Ruby')

    options = st.multiselect('**3. Bạn thích học ở đâu?**', ['Tại nhà', 'Tại trường', 'Tại trung tâm', 'Trực tuyến'])

    hours = st.slider('**4. Bạn học lập trình bao nhiêu tiếng mỗi tuần?**', 0, 40, 10)
    st.form_submit_button('Gửi câu trả lời')



st.write('Bạn học lập trình', hours, 'tiếng mỗi tuần.')
