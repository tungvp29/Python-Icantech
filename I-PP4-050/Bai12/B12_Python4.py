import streamlit as st

class info:
     def __init__(self, name, image1, image2, image3, caption1, caption2, caption3):
          name=self.n
          image1=self.i1
          


st.set_page_config("Vương quốc mô hình", ":star:")
with st.sidebar:
    st.header("Vương quốc mô hình")
    st.subheader("Chào mừng bạn đến Vương quốc mô hình!")
    st.image("https://tse2.mm.bing.net/th/id/OIP.IQfSe6CT8VVEjYINOs8qwwHaHa?rs=1&pid=ImgDetMain&o=7&rm=3")
    st.write("Chúng tôi chuyên bán các mô hình nhân vật hoạt hình chất lượng. Luôn cập nhật và đa dạng sản phẩm. Cam kết sự hài lòng của khách hàng với dịch vụ chuyên nghiệp. Hãy đến và khám phá thế giới mô hình tại Vương quốc mô hình!")
    st.write("🏠 Địa chỉ cửa hàng: Hà Nội, Việt Nam")
    st.write("☎️ Điện thoại liên hệ: 0123456789")
st.header("Vương quốc mô hình")
col1, col2, col3 = st.columns([1,1,1])
with col1:
    button1=st.button("Pokemon")
with col2:
    button2=st.button("Demon Slayer")
with col3:
    button3=st.button("Conan")
if button1:
        st.header("Danh sách mô hình Pokemon")
        col4, col5, col6 = st.columns([1,1,1])
        with col4:
            st.image("https://tse2.mm.bing.net/th/id/OIP.p-lqFkalsKQC-jiSDhI87gHaFX?rs=1&pid=ImgDetMain&o=7&rm=3", "Ash Trainer - Mã số: 001")
        with col5:
             st.image("https://tse2.mm.bing.net/th/id/OIP.6PaTaYBJw8RvLSIJlcxTMQHaFi?rs=1&pid=ImgDetMain&o=7&rm=3", "Pikachu Pokemon - Mã số: 002")
        with col6:
             st.image("https://tse3.mm.bing.net/th/id/OIP.XjSK3Guo1iyA-539C1fPwQAAAA?rs=1&pid=ImgDetMain&o=7&rm=3", "Raichu Pokemon - Mã số: 003")
if button2:
        st.header("Danh sách mô hình Demon Slayer")
        col4, col5, col6 = st.columns([1,1,1])
        with col4:
            st.image("https://tse1.mm.bing.net/th/id/OIP.0EBrXVXzarak2jp3_St4MAHaKG?rs=1&pid=ImgDetMain&o=7&rm=3", "Shinobu Kochou - Mã số: 001")
        with col5:
             st.image("https://tse3.mm.bing.net/th/id/OIP.ybRhrDbk49m1WUhJia5G4QHaIJ?rs=1&pid=ImgDetMain&o=7&rm=3", "Tanjiro Kamado - Mã số: 002")
        with col6:
             st.image("https://tse2.mm.bing.net/th/id/OIP.4EdW9gBSEDumzEqBtE571AHaHa?rs=1&pid=ImgDetMain&o=7&rm=3", "Muzan Kibutsuji - Mã số: 003")
if button3:
        st.header("Danh sách mô hình Conan")
        col4, col5, col6 = st.columns([1,1,1])
        with col4:
            st.image("https://tse2.mm.bing.net/th/id/OIP.Xrym5rW1eX9c1dyXcLPy4AHaHa?rs=1&pid=ImgDetMain&o=7&rm=3", "Kudo Shinichi - Mã số: 001")
        with col5:
             st.image("https://tse1.mm.bing.net/th/id/OIP.XehjKVsjj7lPZiuHgehn9wHaHa?rs=1&pid=ImgDetMain&o=7&rm=3", "Edogawa Conan - Mã số: 002")
        with col6:
             st.image("https://tse1.mm.bing.net/th/id/OIP.f8iFsxv2P6ko26BoPbxhcwHaJ4?rs=1&pid=ImgDetMain&o=7&rm=3", "Ran Mouri - Mã số: 003")
st.header("Đặt hàng")
with st.form(key="md"):
    lstcd=("Pokemon", "Demon Slayer", "Conan")
    lstmsmh=("001","002","003")
    chu_de=st.selectbox(label="Chọn đồ uống", options=lstcd)
    ma_so=st.selectbox(label="Chọn đường", options=lstmsmh)
    so_luong=st.slider("Chọn số lượng mô hình:",min_value=0, max_value=10, value=1, step=1)
    ho_ten=st.text_input("Họ và tên:")
    sdt=st.text_input("Số điện thoại liên lạc:")
    dia_chi=st.text_input("Địa chỉ giao hàng:")
    bill={"Chủ đề mô hình: " : chu_de, "Mã số mô hình: " : ma_so, "Số lượng mô hình: " : so_luong, "Họ và tên:" : ho_ten, "Số điện thoại liên lạc:" : sdt, "Địa chỉ giao hàng:" : dia_chi}
    gui=st.form_submit_button("Xác Nhận")
    if gui:
        st.balloons()
        st.header("Bạn đã mua mô hình!")
        for x,y in bill.items():
            st.write(x,y)
in_hoa_don = st.checkbox("In hoá đơn")
if in_hoa_don:
    hoa_don=""
    for x in bill:
        hoa_don += str(x) + "" + str(bill[x]) + "\n"
    st.download_button("In hoá đơn", hoa_don)
