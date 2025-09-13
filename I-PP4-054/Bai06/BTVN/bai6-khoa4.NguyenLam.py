import streamlit as st
st.title('Dien thong tin gioi thieu ban than')
my_bar = st.progress(0)

quiz = ['Ho va ten:', 'Ngay thang nam sinh', 'So thich:']
answers = []
len_quiz = len(quiz)
for i in range(len(quiz)):
    answer = st.text_input(quiz[i], '')
    if answer != '':
        answers.append(answer)

my_bar.progress(len(answers) / len_quiz)

if st.button('Confirm'):
    if len(answers) == len_quiz:
        # my_bar.progress(100)
        st.write('Ban da hoan thanh day du thong tin')
        st.balloons()
    else:  
        my_bar.progress(len(answers) / len_quiz)
        st.warning('Ban chua dien day du thong tin')
    for i in range(len(answers)):
        st.write(f'{quiz[i]} {answers[i]}')