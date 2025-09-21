import streamlit as st

with st.form(key='form1', clear_on_submit=True):
    st.title('Form Example')
    st.text_input('Nhập tên bài hát:')
    st.text_input('Nhập tên tác giả:')
    selected_options = st.multiselect(
        'Thể loại bài hát:', 
        ['Pop', 'Rock', 'Jazz', 'Classical', 'Hip Hop'],
        default=['Pop'],
        max_selections=2)

    with st.expander('Mô tả bài hát'):
        st.text_area('Nội dung mô tả bài hát:')
    submitted = st.form_submit_button('Xác nhận')

with st.form(key='form2', clear_on_submit=True):
    st.text_input('Ngày phát hành:')
    st.form_submit_button('Xác nhận')