import streamlit as st
st.set_page_config(page_title='đặt đồ uống ',page_icon=':tropical_drink:')
with st.form(key='thực đơn'):
    do_uong_list=('matcha latte','cafe sữa','cafe đen','capuchino','bạc xỉu','trà đá')
    do_uong=st.selectbox('chọn đồ uống:',do_uong_list)
    duong_list=('đường đen','đường trắng','đường vàng','đường mía')
    duong=st.selectbox('chọn loại đường:',duong_list)
    topping=st.checkbox('kèm trân châu')
    so_luong=st.slider('chọn số lượng:',min_value=1,max_value=10,value=1)
    value=st.checkbox('in bill')
    bill={
        'loại đồ uống':do_uong,
        'loại đường':duong,
        'kèm trân châu':topping,
        'số lượng':so_luong,
    }
    submit=st.form_submit_button('đặt hàng')
    if submit:
        st.success('đã đặt hàng thành công')
        st.write('bạn đã đặt đồ uống',bill['loại đồ uống'])
        st.write('bạn đã chọn loại đường',bill['loại đường'])
        if bill['kèm trân châu']:
            st.write('có kèm trân châu')
        else:
            st.write('không trân châu')
print_bill=st.checkbox('in hóa đơn')
if print_bill:
    ans=''
    for x in bill:
        ans += str(x) + '' + str(bill[x]) + '\n'
    st.download_button('in hóa đơn',ans)
    


