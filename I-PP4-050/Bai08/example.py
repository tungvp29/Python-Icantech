import streamlit as st

url = 'https://png.pngtree.com/element_pic/16/10/24/285837b9c9381ee8c557ed155bb435ad.jpg'
url_audio = 'assets/audio/BeoDatMayTroi.mp3'

col1, col2 = st.columns(2)

with col1:
    st.image(url, caption='Happy Dog Outdoors', use_container_width=True)

with col2:
    st.audio(url_audio, autoplay=True)

st.video('https://www.youtube.com/watch?v=MO-w7Y4zRl0')

st.write("This is a happy dog image from the internet.")