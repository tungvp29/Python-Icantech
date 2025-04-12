import streamlit as st  

st.columns(3)
st.columns([1, 2, 1])

with st.expander('Thực đơn yêu thích'):
    st.write('Chương trình thực đơn yêu thích')
    st.write('Bạn có thể chọn nhiều món ăn khác nhau')   
    
lichTrinh = ['Hà Giang', 'Hà nội', 'Đà Nẵng', 'Nha Trang', 'TP Hồ Chí Minh']

app = ['bánh mì', 'bánh bao', 'bánh tét', 'bánh chưng']
main = ['cơm tấm', 'cơm chiên', 'cơm gà', 'cơm sườn']
dessert = ['bánh kem', 'bánh sinh nhật', 'bánh gato', 'bánh bông lan']

with st.form('Thực đơn yêu thích'):
    options1 = st.multiselect('Chọn món khai vị', app)
    options2 = st.selectbox('Chọn món ăn', main)
    options3 = st.multiselect('Chọn món tráng miệng', dessert)

    submited = st.form_submit_button('Đã điền xong')
    

        
with st.expander('Thông tin chi tiết'):
    if submited:
        if len(options1) == 0:
            st.warning('Bạn chưa chọn món khai vị')
        else:
            st.write('**1. Món khai vị:**')
            for khaivi in options1:
                st.write(' :fish_cake: ', khaivi)
        st.write('**2. Món chính:**', options2)
        if len(options3) == 0:
            st.warning('Bạn chưa chọn món tráng miệng')
        else:
            st.write('**3. Món tráng miệng:**')
            for trangmieng in options3:
                st.write(' - ', trangmieng)