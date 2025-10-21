import streamlit as st
st.set_page_config(page_title="Vương Quốc Mô Hình", page_icon=":sparkle:", layout="wide")
with st.sidebar:
    st.title("Vương Quốc Mô Hình")
    st.header('Chào Mừng Bạn Đến Với Vương Quốc Mô Hình!')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxLMoVzEqkhEMNUn_xFBopQ1ziReY9Lp3jKg&s')
    st.write('Chào mừng bạn đến với Vương Quốc Mô Hình, thiên đường của những tín đồ yêu thích Anime, Manga và Văn hóa Nhật Bản. '
             'Chúng tôi tự hào là điểm đến hàng đầu, '
             'nơi hội tụ những mẫu mô hình 3D anime chất lượng cao, từ những nhân vật huyền thoại đến các siêu phẩm mới nhất. '
             'Đây không chỉ là một cửa hàng, '
             'mà còn là một phòng trưng bày nghệ thuật thu nhỏ dành cho những người trân trọng giá trị và độ tinh xảo của mô hình.')
    st.write('🏠 Địa chỉ: 123 Đường Trần Duy Hưng, Trung Tâm Quận 1, TP.HCM')
    st.write('📞 Số điện thoại: 0123456789')
st.title("Vương Quốc Mô Hình")
col1, col2, col3 = st.columns(3)
with col1:
    b1 = st.button("Mô Hình One Piece")
with col2:
    b2 = st.button("Mô Hình Naruto")
with col3:
    b3 = st.button("Mô Hình Demon Slayer")
if b1:
    st.header('Danh Sách Mô Hình One Piece')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('https://img.sugotoys.com.au/images/20250916234350/H5iUZBtpdk75qArt3yILqJetg0rl6TsnXescBvVlX3A.webp',
                  caption='Monkey D. Luffy (Gear 5) - 25.500.000 VND - Mã Số: OP001')
    with col5:
        st.image('https://i.ebayimg.com/images/g/loEAAOSwPSpnQlQk/s-l1600.webp',
                  caption='Roronoa Zoro - 21.200.000 VND - Mã Số: OP002')
    with col6:
        st.image('https://i.ebayimg.com/images/g/DIoAAOSw7DVoEwIp/s-l1600.webp',
                  caption='Kỷ Niệm 7 Năm One Piece - 90.000.000 VND - Mã Số: OP003')
if b2:
    st.header('Danh Sách Mô Hình Naruto')
    col7, col8, col9 = st.columns(3)
    with col7:
        st.image('https://i.ebayimg.com/images/g/cSsAAeSw8mlozm0a/s-l1600.webp',
                  caption='Itachi - 100.800.000 VND - Mã Số: NA001')
    with col8:
        st.image('https://i.ebayimg.com/images/g/UXMAAeSwfJpo13rq/s-l1600.webp',
                  caption='Sasuke Uchiha - 5.900.000 VND - Mã Số: NA002')
    with col9:
        st.image('https://img.sugotoys.com.au/images/20250927234114/wOT1oTqdQwpT3qk0jHmmZIK90BNyt_NhNdtZJrX7gSc-1024x683.webp',
                  caption='Kakashi Hatake - 22.100.000 VND - Mã Số: NA003')
if b3:
    st.header('Danh Sách Mô Hình Demon Slayer')
    col10, col11, col12 = st.columns(3)
    with col10:
        st.image('https://i.ebayimg.com/images/g/YDIAAeSwqNZonooE/s-l960.webp',
                  caption='Tanjiro Kamado - 12.300.000 VND - Mã Số: DS001')
    with col11:
        st.image('https://i.ebayimg.com/images/g/kfEAAOSwEhdlp094/s-l1600.webp',
                  caption='Shinobu Koucho - 20.000.000 VND - Mã Số: DS002')
    with col12:
        st.image('https://i.ebayimg.com/images/g/exkAAOSw8TNm7TKg/s-l1600.webp',
                  caption='Rengoku Kyoujurou - 26.523.165 VND - Mã Số: DS003') 
st.header('Đặt Hàng')
with st.form('don_dat_hang'):
    topics = ('One Piece', 'Naruto', 'Demon Slayer')
    option_topic = st.selectbox('Chọn Loại Mô Hình Bạn Muốn Đặt', topics)
    codes = ('OP001', 'OP002', 'OP003', 'NA001', 'NA002', 'NA003', 'DS001', 'DS002', 'DS003')
    option_code = st.selectbox('Chọn Mã Số Mô Hình Bạn Muốn Đặt', codes)
    nums = st.slider('Chọn Số Lượng Bạn Muốn Đặt', 1, 20, 1)
    name = st.text_input('Họ Và Tên Người Đặt Hàng:')
    phone = st.text_input('Số Điện Thoại Người Đặt Hàng:')
    address = st.text_input('Địa Chỉ Người Đặt Hàng:')
    
    bill = {'Loại Mô Hình: ': option_topic,
           'Mã Số Mô Hình: ': option_code,
             'Số Lượng: ': nums,
               'Họ Và Tên: ': name,
                 'Số Điện Thoại: ': phone,
                   'Địa Chỉ: ': address}
    submit = st.form_submit_button('Xác Nhận Đặt Hàng')
    if submit:
        st.header('Bạn Đã Chọn:')
        for x, y in bill.items():
            st.write(x, y)
print_bill = st.checkbox('In Hóa Đơn')
if print_bill:
    ans = ''
    for x in bill.items():
        ans = ans + str(x[0]) + ': ' + str(x[1]) + '\n'
    st.download_button('In Hóa Đơn', ans)