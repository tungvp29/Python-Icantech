import streamlit as st

st.set_page_config(page_title="Thuc don yeu thich", page_icon="🍴")

st.title("Thuc don yeu thich")
st.write("Chao mung ban den voi trang thuc don yeu thich cua chung toi.Hay kham pha nhung mon an ngon nhat(Chon mon di bro).")

appetizer = ['Banh mi nuong phomai', 'Sup hanh tay Phap', 'Salad Caesar', 'Goi cuon', 'Banh mi bo toi']
main = ['Pizza', 'Pad Thai', 'Steak', 'Moussaka', 'Paella']
dessert = ['Cheesecake', 'Tiramisu', 'Creme brulee', 'Panna cotta', 'Trifle']
drinks = ['Tra sua', 'Nuoc ep', 'Ca phe', 'Sinh to', 'Nuoc loc']
snacks = ['Khoai tay chien', 'Banh quy', 'Banh ngot', 'Xuc xich', 'Nem chua']

with st.form('Thuc don yeu thich'):
    options1 = st.multiselect('Mon khai vi ua thich cua ban?', appetizer)
    options2 = st.multiselect('Mon chinh ua thich cua ban?', main)
    options3 = st.multiselect('Mon trang mieng ua thich cua ban?', dessert)
    options4 = st.multiselect('Do uong ua thich cua ban?', drinks)
    options5 = st.multiselect('Do an nhe ua thich cua ban?', snacks)
    submitted = st.form_submit_button('Submit')

if submitted:
    st.write('Cac lua chon cua ban la:')
    st.write('**1. Mon khai vi:**')
    if len(options1) == 0:
        st.write('Ban chua chon mon khai vi')
    else:
        for i in range(len(options1)):
            st.write(options1[i])

    st.write('**2. Mon chinh:**')
    if len(options2) == 0:
        st.write('Ban chua chon mon chinh')
    else:
        for i in range(len(options2)):
            st.write(options2[i])

    st.write('**3. Mon trang mieng:**')
    if len(options3) == 0:
        st.write('Ban chua chon mon trang mieng')
    else:
        for i in range(len(options3)):
            st.write(options3[i])

    st.write('**4. Do uong:**')
    if len(options4) == 0:
        st.write('Ban chua chon do uong')
    else:
        for i in range(len(options4)):
            st.write(options4[i])

    st.write('**5. Do an nhe:**')
    if len(options5) == 0:
        st.write('Ban chua chon do an nhe')
    else:
        for i in range(len(options5)):
            st.write(options5[i])