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
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.title = 'Con vật bạn chọn là ' + name

conmeo = Personality('Con mèo', 'Lựa chọn này cho thấy bạn chưa sẵn sàng bắt đầu công việc, khao khát được đi nghỉ')
concho = Personality('Con chó', 'Bạn cảm nhận được sự hỗ trợ nhiệt tình của bạn bè và vì thế nên sẵn sàng giải quyết mọi vấn đề')
consutu = Personality('Con sư tử', 'Có thể thấy bạn là người có vẻ ngoài nổi bật. Bạn thu hút mọi người bằng vẻ hào nhoáng')
conngua = Personality('Con ngựa', 'Có điều gì đó đang hạn chế sự tự do của bạn')
conthienga = Personality('Con thiên nga', 'Hiện tại bạn có khoảng thời gian ngọt ngào, hãy cố gắng tận hưởng và kéodài nó nhé')

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
if button2:
    with st.expander(concho.name):
        st.write(concho.description)
if button3:
    with st.expander(consutu.name):
        st.write(consutu.description)
if button4:
    with st.expander(conngua.name):
        st.write(conngua.description)
if button5:
    with st.expander(conthienga.name):
        st.write(conthienga.description)

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