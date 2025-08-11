import streamlit as st
st.set_page_config(page_title='thuc don yeu thich')
appetizer=['banh mi','hanh tay','salad']
main=['pizza','steak','salmon','sushi']
dessert=['cheesecake','yogurt','pancake']
with st.form('thuc don yeu thich'):
    monKhaiVi = st.multiselect('mon khai vi yeu thich cua ban?', appetizer)
    monChinh = st.multiselect('mon chinh ua thich cua ban?', main)
    monTrangMieng = st.multiselect('mon trang mieng yeu thich cua ban?', dessert)
    submitted=st.form_submit_button('submit')
    if submitted:
        st.subheader('cac lua chon cua ban la:')
        st.write('1.mon khai vi:')
        if len(monKhaiVi)==0:
            st.warning('ban chua chon mon khai vi')
        else:
            for i in range(len(monKhaiVi)):
                st.write(monKhaiVi[i])
        st.write('2.mon chinh:')
        if len(monChinh)==0:
            st.error('ban chua chon mon chinh')
        else:
            for i in range(len(monChinh)):
                st.write(monChinh[i])
        st.write('3.mon trang mieng:')
        if len(monTrangMieng)==0:
            st.write('ban chua chon mon trang mieng')
        else:
            for i in range(len(monTrangMieng)):
                st.write(monTrangMieng[i])
            
