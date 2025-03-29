import streamlit as st  

st.columns(3)
st.columns([1, 2, 1])

with st.expander('Thông tin chi tiết'):
    st.write('Nội dung chi tiết 1...')
    st.write('Nội dung chi tiết 2...')

# exp = st.expander('Thông tin chi tiết').write('Nội dung chi tiết...').write('Nội dung chi tiết 2...')

st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/SOOBIN_HO%C3%80NG_S%C6%A0N_2.png/250px-SOOBIN_HO%C3%80NG_S%C6%A0N_2.png', use_column_width=True)