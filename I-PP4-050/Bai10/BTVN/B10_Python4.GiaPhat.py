import streamlit as st
st.set_page_config(page_title="Thực đơn yêu thích", page_icon=":taco:", layout="centered")
monkhaivi=["Đậu phộng", "Súp cua", "Bắp chiên", "Bánh mì"]
monchinh=["Cơm chiên hải sản", "Mì trộn bò", "Bò bít tết", "Cháo lòng"]
montranmieng=["Chè sen", "Dưa hấu", "Kem vanilla", "Nho"]
douong=["Nước lọc", "Coca-cola", "Bia Tiger", "Trà sữa"]
lichtrinh=["Hà Nội", "Huế", "Đà Lạt", "Thành phố Hồ Chí Minh", "Tràng An"]
st.title("Kế hoạch bữa ăn")
with st.form(key="td"):
    chonmkv=st.multiselect("Món Khai Vị", monkhaivi)
    chonmc=st.selectbox("Món Chính", monchinh)
    chonmtm=st.multiselect("Món tráng miệng", montranmieng)
    chondu=st.selectbox("Đồ uống", douong)
    chonlt=st.select_slider("Lịch trình", lichtrinh, ["Hà Nội", "Huế"])
    fsb=st.form_submit_button("Gửi dữ liệu")
if fsb==True:
    with st.expander("Kế hoạch đã chọn"):
        st.subheader(f"Bạn đã chọn món khai vị:")
        if len(chonmkv)==0:
            st.warning("Bạn chưa chọn món khai vị")
        else:
            for monan in chonmkv:
                st.write(monan)
        st.subheader(f"Bạn đã chọn món chính:")
        st.write(f":rice: {chonmc}")
        st.subheader(f"Bạn đã chọn món tráng miệng:")
        if len(chonmtm)==0:
            st.warning("Bạn chưa chọn món tráng miệng")
        else:
            for monan in chonmtm:
                st.write(monan)
        st.subheader(f"Bạn đã chọn đồ uống:")
        st.write(chondu)
        st.subheader(f"Bạn đã chọn lịch trình: Từ {chonlt[0]} đến {chonlt[1]}")