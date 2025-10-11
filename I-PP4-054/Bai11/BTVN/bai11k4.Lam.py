import streamlit as st
with st.form('Order do uong'):
    do_uong = ['Tra sua', 'Ca phe', 'Nuoc ep trai cay', 'Sinh to']
    size = ['Nho', 'Vua', 'Lon']
    topping = ['Tran chau den', 'Tran chau trang', 'Pudding', 'Thach', 'Khong']
    drink = st.selectbox('Chon do uong', do_uong)
    drink_size = st.radio('Chon size', size)
    drink_topping = st.multiselect('Chon topping', topping)
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write(f'Ban da chon {drink} - size {drink_size}')
        if len(drink_topping) == 0:
            st.write('Ban khong chon topping nao')
        else:
            st.write('Topping ban chon la:')
            for i in range(len(drink_topping)):
                st.write(drink_topping[i])