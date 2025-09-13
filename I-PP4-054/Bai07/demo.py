import streamlit as st

st.set_page_config(page_title="Trắc nghiệm tính cách", page_icon=":question:", layout="centered")

st.title('Hãy chọn một con vật bạn yêu thích')

# TinhCach = {
#     'Con mèo': 'Lựa chọn này cho thấy bạn chưa sẵn sàng bắt đầu công việc, khao khát được đi nghỉ',
#     'Con chó': 'Bạn cảm nhận được sự hỗ trợ nhiệt tình của bạn bè và vì thế nên sẵn sàng giải quyết mọi vấn đề',
#     'Con sư tử': 'Có thể thấy bạn là người có vẻ ngoài nổi bật. Bạn thu hút mọi người bằng vẻ hào nhoáng',
#     'Con ngựa': 'Có điều gì đó đang hạn chế sự tự do của bạn',
#     'Con thiên nga': 'Hiện tại bạn có khoảng thời gian ngọt ngào, hãy cố gắng tận hưởng và kéo dài nó nhé'
# }

class Personality:
    def __init__(self, name, description, img):
        self.name = name
        self.description = description
        self.title = 'Con vật bạn chọn là ' + name
        self.image = img

conmeo = Personality(
    'Con mèo', 
    'Lựa chọn này cho thấy bạn chưa sẵn sàng bắt đầu công việc, khao khát được đi nghỉ',
    'https://github.com/tungvp29/Python-Icantech/blob/main/PYDT4D0213/Bai08/assets/Lion-species-hero-c-George-Logan.jpg'
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

tinhcach = [conmeo, concho, consutu, conngua, conthienga]
cols = st.columns(5)
des = ''
img = ''
tit = ''
for i in range(5):
    with cols[i]:
        if st.button(tinhcach[i].name):
            des = tinhcach[i].description
            img = tinhcach[i].image
            tit = tinhcach[i].title

with st.expander('Kết quả'):
    st.write(des)
    if img != '':
        st.image(img)

with st.sidebar:
    st.title('Trắc nghiệm tính cách')
    st.write(tit)