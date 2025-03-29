import streamlit as st

st.set_page_config(page_title='Thế giới động vật', page_icon=':tiger:', layout='centered')
col1, col2, col3, col4, col5 = st.columns(5)
col6, col7 = st.columns([2, 1])

class Animal:
    def __init__(self, name, img, caption , video, audio):
        self.name = name
        self.image = img
        self.video = video
        self.audio = audio
        self.caption = caption

conmeo = Animal(
    name = 'Con mèo',
    img = 'https://static.toiimg.com/photo/msid-67586673/67586673.jpg?resizemode=4&width=400',
    caption= 'Ảnh con mèo',
    video = 'https://www.youtube.com/watch?v=l6FN5RG14Lg',
    audio = 'cat-meow.wav'
)

with col1:
    button1 = st.button(conmeo.name)
with col2:
    button2 = st.button('Con chó')
with col3:
    button3 = st.button('Con sư tử')
with col4:
    button4 = st.button('Con ngựa')
with col5:
    button5 = st.button('Con thiên nga')

if button1:
    with col6:
        st.title(conmeo.name)
        st.write('Tiếng mèo kêu')
        st.audio(conmeo.audio)

        st.write('Video mèo')
        st.video(conmeo.video, format='video/mp4')
    with col7:
        st.title('')
        st.image(conmeo.image, caption=conmeo.caption)

if button2:
    with col6:
        st.title('Con chó')
        st.write('Tiếng chó sủa')
        st.audio('cat-meow.wav')

        st.write('Video chó')
        st.video('https://www.youtube.com/watch?v=l6FN5RG14Lg', format='video/mp4')
    with col7:
        st.title('')
        st.image('https://static.toiimg.com/photo/msid-67586673/67586673.jpg?resizemode=4&width=400', caption='Con chó')