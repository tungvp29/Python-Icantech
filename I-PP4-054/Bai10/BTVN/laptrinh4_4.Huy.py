import streamlit as st

st.set_page_config(page_title = 'Thuc don yeu thich', page_icon= ':rice:', layout= 'centered')

khai_vi = ['Banh mi', 'Banh bao', 'Banh tet', 'Banh chung']
mon_chinh = ['Com tam', 'Com ga', 'Com chien', 'Com suon']
do_uong = ['Tra sua', 'Nuoc ngot', 'Nuoc ep trai cay', 'Nuoc dua']
trang_mien = ['Banh kem','Banh gato', 'Banh sinh nhat', 'Banh bong lan']

st.title("Thuc don yeu thich")
with st.form(key='thuc don', clear_on_submit=True):
    lua_chon1 = st.multiselect('Chon mon khai vi:', khai_vi)
    lua_chon2 = st.selectbox('Chon mon chinh', mon_chinh)
    lua_chon3 = st.selectbox('Chon do uong:', do_uong)
    lua_chon4 = st.multiselect('Chon mon trang mieng', trang_mien)
    button = st.form_submit_button('Xac nhan')

with st.expander('Thuc don da chon:'):
    if button:
        st.write('**Mon khai vi da chon**')
        if len(lua_chon1) == 0:
            st.warning('Ban chua chon mon khai vi!')
        else:
            for mon in lua_chon1:
                st.write('🍡', mon)
        st.write('**Mon an chinh**')
        st.write(lua_chon2,'🍚')
        st.write('**Do uong**')
        st.write(lua_chon3,'🧋')
        st.write('**Mon khai vi da chon**')
        if len(lua_chon4) == 0:
            st.warning('Ban chua chon mon trang mieng!')
        else:
            for mon in lua_chon4:
                st.write('🍌', mon)




