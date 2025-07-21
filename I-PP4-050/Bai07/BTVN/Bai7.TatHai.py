import streamlit as st
st.set_page_config(page_title="trắc nghiệm tính cách ", page_icon=":question:",layout="wide",initial_sidebar_state="expanded")
st.title("hãy chọn một con vật bạn yêu thích:")
col1,col2,col3,col4,col5=st.columns(5)
tinhcach={'con mèo':'lựa chọn này cho thấy bạn chưa sẵn sàng bắt đầu công việc, khao khát được đi nghỉ',
          'con chó':'bạn cảm nhận được sự hỗ trợ nhiệt tình của bạn bè và vì thế nên sẵn sàng giải quyết mọi vấn đề',
          'con sư tử':'có thể thấy bạn là người có vẻ ngoài nổi bật, bạn thu hút mọi người bằng vẻ hào nhoáng',
          'con ngựa':'có điều gì đó đang hạn chế sự tự do của bạn',
          'con thiên nga':'hiện tại bạn có khoảng thời gian ngọt ngào, hãy cố gắng tận hưởng và kéo dài nó nhé'
          }
with col1:
    b1=st.button('con mèo')
with col2:
    b2=st.button('con chó')
with col3:
    b3=st.button("con sư tử")
with col4:
    b4=st.button('con ngựa')
with col5:
    b5=st.button('con thiên nga')    
if b1:
    with st.expander("con mèo"):
        st.write(tinhcach["con mèo"])
if b2:
    with st.expander("con chó"):
        st.write(tinhcach["con chó"])
if b3:
    with st.expander("con sư tử"):
        st.write(tinhcach["con sư tử"])
if b4:
    with st.expander("con ngựa"):
        st.write(tinhcach["con ngựa"])
if b5:
    with st.expander("con thiên nga"):
        st.write(tinhcach["con thiên nga"])        
with st.sidebar:
    st.title("trắc nghiệm tính cách")
    if b1:
        st.write("bạn đã chọn con mèo!")
    if b2:
        st.write("bạn đã chọn con chó!")
    if b3:
        st.write("bạn đã chọn con sư tử!")
    if b4:
        st.write("bạn đã chọn con ngựa!")
    if b5:
        st.write("bạn đã chọn con thiên nga!")

    
