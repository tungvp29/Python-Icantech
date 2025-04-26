import streamlit as st

mts = st.multiselect('Chọn món khai vị', ['Bánh mì', 'Bánh bao', 'Bánh tét', 'Bánh chưng'])
st.write('Món khai vị bạn đã chọn là:', mts)

slb = st.selectbox('Chọn món ăn', ['Bánh mì', 'Bánh bao', 'Bánh tét', 'Bánh chưng'])
st.write('Món ăn bạn đã chọn là:', slb)

cb = st.checkbox('Bạn có muốn ăn bánh mì không?')
# cb2 = st.checkbox('Bánh bao')
# cb3 = st.checkbox('Bánh tét')
if cb == True:
    st.write('Câu trả lời: Có')
    kq = 'Có'
else:
    st.write('Câu trả lời: Không')
    kq = 'Không'

downloadContent = f'Món ăn bạn đã chọn là: {slb}\nCâu trả lời: {kq}'
for monan in mts:
    downloadContent += f'\nMón khai vị bạn đã chọn là: {monan}'

st.download_button(
    label="Bấm để tải về thông tin bạn đã chọn",
    data=downloadContent,
    file_name="file.txt",
)

# lichTrinh = ['Hà Giang', 'Hà nội', 'Đà Nẵng', 'Nha Trang', 'TP Hồ Chí Minh']
# options4 = st.select_slider(
#         label = 'Chọn lịch trình di chuyển',
#         options=lichTrinh,
#         value=['Hà Giang', 'Hà nội'])


# soluong = st.slider('Chọn số lượng', -100, 200, 25)
# st.write('Số lượng bạn đã chọn là:', soluong)

#multiselect: chọn theo danh sách đã biết trước
#selectbox: 
#checkbox: 