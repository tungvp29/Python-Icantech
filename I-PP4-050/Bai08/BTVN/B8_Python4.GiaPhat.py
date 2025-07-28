import streamlit as st

st.set_page_config(page_title="Favorite singer", page_icon=":microphone:", layout="centered")

class Singer:
    def __init__(self, name, DOB, POB, intro, profpic):
        self.name = name
        self.DOB = DOB
        self.POB = POB
        self.intro = intro
        self.profpic = profpic
        self.song = []
    def add_song(self, song):
        pass

class Song:
    def __init__(self, name, link, type):
        self.name = name
        self.link = link
        self.type = type

#object / instance
singer1 = Singer(
    name = 'Alan Walker',
    DOB = '24 August 1997',
    POB = 'Northampton, England',
    intro = 'Alan Olav Walker (born 24 August 1997) is a Norwegian DJ and record producer. His songs "Faded", "Sing Me to Sleep", "Alone", "All Falls Down", "Ignite" and "Darkside" have each been multi-platinum-certified and reached number 1 on the VG-lista chart in Norway. Walker values his anonymity and is known to wear a hoodie and mask to remain inconspicuous.',
    profpic = 'https://upload.wikimedia.org/wikipedia/commons/7/71/Alan_Walker_visits_Spangdahlem.jpg'
)

song1 = Song('Alone', 'assets/audio/Alone.mp3', 'audio')
song2 = Song('On my way', 'assets/audio/OnMyWay.mp3', 'audio')
lstAudio = [song1, song2]

song3 = Song('Faded', 'https://youtu.be/60ItHLz5WEA?si=oKOuUgszz8zTIUCj', 'video')
song4 = Song('Darkside', 'https://youtu.be/M-P4QBt-FWw?si=ke7s6hHL5j6wk9zj', 'video')
lstVideo = [song3, song4]


with st.sidebar:
    st.image(singer1.profpic,caption=singer1.name)
    st.write(f'Name: {singer1.name}')
    st.write(f'Date of birth: {singer1.DOB}')
    st.write(f'Place of birth: {singer1.POB}')
    st.write(singer1.intro)

st.header('Favorite songs')
for audioFile in lstAudio:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write(audioFile.name)
    with col2:
        st.audio(audioFile.link)

st.header('Favorite videos')
for videoFile in lstVideo:
    st.write(videoFile.name)
    st.video(videoFile.link)