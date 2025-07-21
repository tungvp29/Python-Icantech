import streamlit as st

st.set_page_config(page_title="Ca sĩ yêu thích", page_icon=":microphone:", layout="centered")

class Singer:
    def __init__(self, ten, ngaysinh, noisinh, gioithieu, anhDaiDien):
        self.ten = ten
        self.ngaysinh = ngaysinh
        self.noisinh = noisinh
        self.gioithieu = gioithieu
        self.anhDaiDien = anhDaiDien

class Song:
    def __init__(self, ten, link, loai):
        self.ten = ten
        self.link = link
        self.loai = loai

caSi = Singer(
    ten = 'Nguyễn Huỳnh Sơn',
    ngaysinh = '10 tháng 9, 1992',
    noisinh = 'Hà Nội',
    gioithieu = 'Thường được biết đến với nghệ danh Soobin hay với tên cũ Soobin Hoàng Sơn (viết cách điệu là SOOBIN), là một nam ca sĩ kiêm nhạc sĩ sáng tác ca khúc người Việt Nam. Được đánh giá là một trong những nghệ sĩ âm nhạc Việt Nam xuất sắc nhất trong thế hệ của mình, anh dành phần lớn sự nghiệp gắn bó với tư cách là thành viên của SpaceSpeakers. Xuyên suốt sự nghiệp của mình, anh đã giành được nhiều giải thưởng cao quý, trong đó có năm đề cử và ba giải Cống hiến.',
    anhDaiDien = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/SOOBIN_HO%C3%80NG_S%C6%A0N_2.png/250px-SOOBIN_HO%C3%80NG_S%C6%A0N_2.png'
)

baiHat1 = Song('Em của ngày hôm qua', 'https://github.com/tungvp29/Python-Icantech/blob/main/PYDT4D0213/Bai08/assets/audio/EmCuaNgayHomQua.mp3', 'audio')
baiHat2 = Song('Bèo dạt mây trôi', 'https://github.com/tungvp29/Python-Icantech/blob/main/PYDT4D0213/Bai08/assets/audio/BeoDatMayTroi.mp3', 'audio')
lstAudio = [baiHat1, baiHat2]

baiHat3 = Song('Giá như', 'https://www.youtube.com/watch?v=UOL-e1LTDag', 'video')
baiHat4 = Song('The playah', 'https://www.youtube.com/watch?v=d44UTUSTYKU', 'video')
lstVideo = [baiHat3, baiHat4]


with st.sidebar:
    st.image(caSi.anhDaiDien,caption=caSi.ten)
    st.write(f'Họ và tên: {caSi.ten}')
    st.write(f'Ngày sinh: {caSi.ngaysinh}')
    st.write(f'Nơi sinh: {caSi.noisinh}')
    st.write(caSi.gioithieu)

st.header('Bài hát yêu thích')
for audioFile in lstAudio:
    st.write(audioFile.ten)
    st.audio(audioFile.link)

st.header('Video yêu thích')
for videoFile in lstVideo:
    st.write(videoFile.ten)
    st.video(videoFile.link)
