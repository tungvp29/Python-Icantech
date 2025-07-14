import streamlit as st

st.set_page_config(page_title="Trắc nghiệm tính cách", page_icon=":question:", layout="centered")

st.title('Hãy chọn một con vật bạn yêu thích')
col1, col2, col3, col4, col5 = st.columns(5)

TinhCach = {
    'Con mèo': 'Lựa chọn này cho thấy bạn chưa sẵn sàng bắt đầu công việc, khao khát được đi nghỉ',
    'Con chó': 'Bạn cảm nhận được sự hỗ trợ nhiệt tình của bạn bè và vì thế nên sẵn sàng giải quyết mọi vấn đề',
    'Con sư tử': 'Có thể thấy bạn là người có vẻ ngoài nổi bật. Bạn thu hút mọi người bằng vẻ hào nhoáng',
    'Con ngựa': 'Có điều gì đó đang hạn chế sự tự do của bạn',
    'Con thiên nga': 'Hiện tại bạn có khoảng thời gian ngọt ngào, hãy cố gắng tận hưởng và kéo dài nó nhé'
}

class Personality:
    def __init__(self, name, description, img):
        self.name = name
        self.description = description
        self.title = 'Con vật bạn chọn là ' + name
        self.image = img

conmeo = Personality(
    'Con mèo', 
    'Lựa chọn này cho thấy bạn chưa sẵn sàng bắt đầu công việc, khao khát được đi nghỉ',
    'https://static.toiimg.com/photo/msid-67586673/67586673.jpg?resizemode=4&width=400'
    )

concho = Personality(
    'Con chó', 
    'Bạn cảm nhận được sự hỗ trợ nhiệt tình của bạn bè và vì thế nên sẵn sàng giải quyết mọi vấn đề',
    'https://hips.hearstapps.com/hmg-prod/images/happy-dog-outdoors-royalty-free-image-1652927740.jpg?crop=0.447xw:1.00xh;0.187xw,0&resize=980')

consutu = Personality(
    'Con sư tử', 
    'Có thể thấy bạn là người có vẻ ngoài nổi bật. Bạn thu hút mọi người bằng vẻ hào nhoáng',
    'https://www.akronzoo.org/sites/default/files/styles/square_large/public/assets/animals/Lion-Donovan.png?h=00546c34&itok=-9dhFwI5')

conngua = Personality(
    'Con ngựa', 
    'Có điều gì đó đang hạn chế sự tự do của bạn',
    'https://www.horseridingnow.com.au/wp-content/uploads/2024/07/shutterstock_153831563-scaled.jpg'
    )

conthienga = Personality(
    'Con thiên nga', 
    'Hiện tại bạn có khoảng thời gian ngọt ngào, hãy cố gắng tận hưởng và kéodài nó nhé',
    'https://www.acfc.com.vn/acfc_wp/wp-content/uploads/2024/07/image-9-1024x620.webp'
    )
    

with col1:
    button1 = st.button(conmeo.name)
with col2:
    button2 = st.button(concho.name)
with col3:
    button3 = st.button(consutu.name)
with col4:
    button4 = st.button(conngua.name)
with col5:
    button5 = st.button(conthienga.name)

if button1:
    with st.expander(conmeo.name):
        st.write(conmeo.description)
        st.image(conmeo.image)
if button2:
    with st.expander(concho.name):
        st.write(concho.description)
        st.image(concho.image)
if button3:
    with st.expander(consutu.name):
        st.write(consutu.description)
        st.image(consutu.image)
if button4:
    with st.expander(conngua.name):
        st.write(conngua.description)
        st.image(conngua.image)
if button5:
    with st.expander(conthienga.name):
        st.write(conthienga.description)
        st.image(conthienga.image)

with st.sidebar:
    st.title('Trắc nghiệm tính cách')
    if button1:
        st.write(conmeo.title)
    if button2:
        st.write(concho.title)
    if button3:
        st.write(consutu.title)
    if button4:
        st.write(conngua.title)
    if button5:
        st.write(conthienga.title)