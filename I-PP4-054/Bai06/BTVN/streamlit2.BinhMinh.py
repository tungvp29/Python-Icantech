import streamlit as st

st.title('Điền thông tin giới thiệu bản thân em')
my_bar = st.progress(0)

quiz = ['Họ và tên:', 
        'Ngày tháng năm sinh:', 
        'Sở thích:',
        'Địa chỉ:',
        'Số điện thoại:',
        'Email:',
        'Nghề nghiệp:',
        'Giới thiệu ngắn về bản thân:']
answers = []
len_quiz = len(quiz)
for i in range(len_quiz):
    if i == 1:
        answer = st.date_input(quiz[i])
    else:
        answer = st.text_input(quiz[i], '')
    if answer != '':
        answers.append(answer)

my_bar.progress(len(answers) / len_quiz)

if st.button('Confirm'):
    if len(answers) == len_quiz:
        # my_bar.progress(100)
        st.success('Bạn đã hoàn thành đầy đủ thông tin!')
        for i in range(len(answers)):
            st.write(quiz[i], answers[i])
        st.balloons()
    else:
        my_bar.progress(len(answers) / len_quiz)
        st.error('Bạn chưa hoàn thành đầy đủ thông tin!')
