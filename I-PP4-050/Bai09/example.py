import streamlit as st

class Song:
    def __init__(self, name, link, type):
        self.name = name
        self.link = link
        self.type = type

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name'),
            link=data.get('link'),
            type=data.get('type')
        )
    
    @staticmethod
    def validate_type():
        valid_types = ['audio', 'video']
        return valid_types
    
    @property
    def is_audio(self):
        self.name = "Unknown Song"
        return self.type == 'audio'
    
    @is_audio.setter
    def is_audio(self, value):
        if value:
            self.type = 'audio'
        else:
            self.type = 'video'

    @is_audio.deleter
    def is_audio(self):
        del self.type
        self.type = 'video'  # Default type if deleted
        print("Audio type deleted, set to default 'video'.")
        

st.set_page_config(page_title="Song Example", page_icon=":musical_note:", layout="centered", initial_sidebar_state="auto")
st.title('Đây là title')
st.header('Đây là header')
st.write('Đây là nội dung của trang web trong câu lệnh write.')

st.text_input('Nhập tên bài hát:', key='song_name')
st.text_area('Nhập mô tả bài hát:', key='song_description')

bt1 = st.button('Xác nhận')
if bt1:
    st.write('Bạn đã xác nhận thông tin bài hát!')

if st.button('Hủy bỏ'):
    st.write('Bạn đã hủy bỏ thông tin bài hát.')

if st.button('Gửi thông tin'):
    st.balloons()
st.progress(50, text='Đang xử lý...')

col1, col2, col3 = st.columns(3)
st.columns([3, 1, 2])

st.sidebar.title('Sidebar Example')