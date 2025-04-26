import streamlit as st

# Cấu hình tiêu đề và icon
st.set_page_config(page_title='Trang web đặt đồ uống', page_icon=':tropical_drink:', layout='centered')

# Form nhập thông tin đặt hàng
with st.form(key='thucdon'):
    #đồ uống
    doUongLst = ['Trà sữa', 'Nước ngọt', 'Nước ép trái cây', 'Nước dừa']
    doUong = st.selectbox('Chọn đồ uống:', doUongLst)
    
    loaiDuongLst = ['Đường trắng', 'Đường nâu', 'Đường vàng']
    loaiDuong = st.selectbox('Chọn loại đường:', loaiDuongLst)

    toppingLst = ['Trân châu', 'Thạch trái cây', 'Thạch rau câu']
    topping = st.multiselect('Chọn topping:', toppingLst)

    #số lượng
    soluong = st.slider('Chọn số lượng:', 0, 10, 1)

    #hóa đơn lưu thành dictionary
    bill = {
        'Loại đồ uống': doUong,
        'Loại đường': loaiDuong,
        'Topping': topping,
        'Số lượng': soluong
    }

    submited = st.form_submit_button('Đặt hàng')

    print_bill = st.checkbox('In hóa đơn')

    #hiển thị thực đơn đã chọn
    if submited:
        st.success('Đặt hàng thành công!')
        st.write(f'Bạn đã chọn đồ uống: {bill["Loại đồ uống"]}')
        st.write(f'Loại đường: {bill["Loại đường"]}')
        if len(bill['Topping']) == 0:
            st.warning('Bạn chưa chọn topping')
        else:
            st.write('Topping đã chọn:')
            for item in bill['Topping']:
                st.write(':taco:', item)
        st.write(f'Số lượng: {bill["Số lượng"]}')

# In hóa đơn
if print_bill:
    bill_str = f'''Loại đồ uống: {bill["Loại đồ uống"]}
Loại đường: {bill["Loại đường"]}
Topping: {', '.join(bill["Topping"])} (nếu có)
Số lượng: {bill["Số lượng"]}
'''       
        
    st.download_button(
        label="Tải hóa đơn",
        data=bill_str,
        file_name="hoadon.txt",
        mime="text/plain"
    )