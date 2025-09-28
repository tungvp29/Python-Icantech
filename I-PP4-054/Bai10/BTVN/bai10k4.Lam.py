import streamlit as st
appetizer = ['Banh mi tra bong','Banh mi nuong muoi ot','Salad','Sup bi ngo']
main = ['Spaghetti','Com chien','Pizza','Hamburger','Com ga singapore']
dessert = ['kem so co la','Banh tiramisu','Sua chua','kem sau rieng','Che']
with st.form('Thuc don yeu thich'):
    options1 = st.multiselect('Mon khai vi', appetizer)
    options2 = st.multiselect('Mon chinh', main)
    options3 = st.multiselect('Mon trang mieng', dessert)
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write('Mon khai vi ban chon la:')
        st.write('Mon chinh ban chon la:')
        if len(options1) == 0:
            st.write('Ban chua chon mon nao')
        else:
            for i in range(len(options1)):
                st.write(options1[i])
        st.write('Mon chinh ban chon la:')
        if len(options2) == 0:
            st.write('Ban chua chon mon nao')
        else:
            for i in range(len(options2)):
                st.write(options2[i])        

        st.write('Mon trang mieng ban chon la:')
        if len(options3) == 0:
            st.write('Ban chua chon mon nao')
        else:
            for i in range(len(options3)):
                st.write(options3[i])      