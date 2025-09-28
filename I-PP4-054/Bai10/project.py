import streamlit as st

# Cấu hình tiêu đề và icon
st.set_page_config(page_title='Thực đơn yêu thích', page_icon=':taco:', layout='centered')

# Khai báo các danh sách món ăn
khaivi = ['Bánh mì', 'Bánh bao', 'Bánh tét', 'Bánh chưng']
main = ['Cơm tấm', 'Cơm chiên', 'Cơm gà', 'Cơm sườn']
douong = ['Trà sữa', 'Nước ngọt', 'Nước ép trái cây', 'Nước dừa']
trangmieng = ['Bánh kem', 'Bánh sinh nhật', 'Bánh gato', 'Bánh bông lan']
lichTrinh = ['Hà Giang', 'Hà nội', 'Đà Nẵng', 'Nha Trang', 'TP Hồ Chí Minh']

# Tạo tiêu đề cho ứng dụng
st.title('Chương trình thực đơn yêu thích')

# Form để chọn món ăn
with st.form(key='thucdon'):
    options1 = st.multiselect('Chọn món khai vị', khaivi)
    options2 = st.selectbox('Chọn món ăn', main)
    options3 = st.multiselect('Chọn món tráng miệng', trangmieng)
    options4 = st.selectbox('Chọn đồ uống', douong)
    st.multiselect()
    submited = st.form_submit_button('Đã điền xong')        #True/False

# Thực đơn đã chọn
with st.expander('Thực đơn đã chọn'):
    if submited:
        st.write('**Bạn đã chọn món khai vị:**')
        if len(options1) == 0:
            st.warning('Bạn chưa chọn món khai vị')
        else:
            for monkhaivi in options1:
                st.write(':dango:', monkhaivi)

        st.write('**Bạn đã chọn món chính:**')
        st.write(':rice:', options2)

        st.write('**Bạn đã chọn món tráng miệng:**')
        if len(options3) == 0:
            st.warning('Bạn chưa chọn món khai vị')
        else:
            for montrangmieng in options3:
                st.write(':watermelon:', montrangmieng)

        st.write('**Bạn đã chọn đồ uống:**')
        st.write(':tropical_drink:', options4)

#Form để chọn lịch trình di chuyển
with st.form(key='lichtrinh'):
    options4 = st.select_slider(
        label = 'Chọn lịch trình di chuyển',
        options=lichTrinh,
        value=['Hà Giang', 'Hà nội'])

    submited2 = st.form_submit_button('Đã điền xong')