import streamlit as st
st.set_page_config(page_title="Nước uống yêu thích", page_icon="🍹")

st.title("Đồ uống yêu thích")

with st.form('Đồ uống yêu thích'):
    douong = ['Trà sữa', 'Nước ép', 'Cà phê', 'Sinh tố', 'Nước lọc', 'Nước có ga', 'Nước khoáng']
    douongdachon = st.selectbox('Đồ uống yêu thích của bạn?', douong)

    loaiduong = ['Đường trắng', 'Đường nâu', 'Không đường', 'Đường ăn kiêng']
    loaiduongdachon = st.selectbox('Bạn muốn loại đường nào?', loaiduong)

    topping = ['Trân châu đen', 'Trân châu trắng', 'Thạch', 'Không topping', 'Hạt chia', 'Kem']
    toppingdachon = st.multiselect('Bạn muốn topping nào?', topping)

    loaida = ['Đá nhiều', 'Đá ít', 'Không đá', 'Đá xay']
    loaidadachon = st.radio('Bạn muốn loại đá nào?', loaida)

    kichthuoc = ['Nhỏ', 'Vừa', 'Lớn', 'Siêu lớn']
    kichthuocdachon = st.radio('Bạn muốn kích thước nào?', kichthuoc)

    soluong = st.slider('Số lượng mà bạn muốn', 1, 10, 5)

    inhoadon = st.checkbox('Bạn có muốn in hóa đơn không?')

    submit = st.form_submit_button('Giao hàng')

    hoadon = {
        'Đồ uống': douongdachon,
        'Loại đường': loaiduongdachon,
        'Topping': toppingdachon,
        'Loại đá': loaidadachon,
        'Kích thước': kichthuocdachon,
        'Số lượng': soluong,
        'In hóa đơn': inhoadon
    }

    if submit:
        st.success('Bạn đã đặt hàng thành công!')
        st.write(f'Đồ uống mà bạn chọn: {hoadon["Đồ uống"]}')
        st.write(f'Topping mà bạn chọn: {", ".join(hoadon["Topping"])}')
        st.write(f'Loại đường mà bạn chọn: {hoadon["Loại đường"]}')
        st.write(f'Loại đá mà bạn chọn: {hoadon["Loại đá"]}')
        st.write(f'Kích thước mà bạn chọn: {hoadon["Kích thước"]}')
        st.write(f'Số lượng mà bạn chọn: {hoadon["Số lượng"]}')

if hoadon['In hóa đơn']:
    hoadon_text = f"""
    Hóa đơn của bạn:
    - Đồ uống: {hoadon['Đồ uống']}
    - Loại đường: {hoadon['Loại đường']}
    - Topping: {', '.join(hoadon['Topping'])}
    - Loại đá: {hoadon['Loại đá']}
    - Kích thước: {hoadon['Kích thước']}
    - Số lượng: {hoadon['Số lượng']}
    """
    st.download_button('Tải hóa đơn', hoadon_text, file_name='hoadon.txt')