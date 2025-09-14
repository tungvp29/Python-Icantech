import streamlit as st

st.set_page_config(page_title='Thế giới động vật', page_icon=':tiger:', layout='centered')

class Animal:
    def __init__(self, name = '', img = '', caption = '', video = '', audio = '', description = ''):
        self.name = name
        self.image = img
        self.video = video
        self.audio = audio
        self.caption = caption
        self.description = description

lstAnimal = []

lstAnimal.append(Animal(
    name = 'Con mèo',
    img = 'https://static.toiimg.com/photo/msid-67586673/67586673.jpg?resizemode=4&width=400',
    caption= 'Ảnh con mèo',
    video = 'https://www.youtube.com/watch?v=l6FN5RG14Lg',
    audio = 'cat-meow.wav',
    description = '''Mèo (chính xác hơn là mèo nhà để phân biệt với các loài trong họ Mèo khác) là động vật có vú, nhỏ nhắn và chuyên ăn thịt, sống chung với loài người, được nuôi để săn vật gây hại hoặc làm thú nuôi cùng với chó. Mèo đã sống gần gũi với loài người ít nhất 9.500 năm,[4] và hiện nay chúng là con vật cưng phổ biến nhất trên thế giới.[5]
Có rất nhiều các giống mèo khác nhau, một số không có lông hoặc không có đuôi, và chúng có nhiều màu lông khác nhau. Mèo là những con vật có kỹ năng của thú săn mồi và được biết đến với khả năng săn bắt hàng nghìn loại sinh vật để làm thức ăn, ví dụ như chuột. Chúng đồng thời là những sinh vật thông minh, và có thể được dạy hay tự học cách sử dụng các công cụ đơn giản như mở tay nắm cửa hay giật nước trong nhà vệ sinh.
Mèo giao tiếp bằng cách kêu meo meo, gừ-gừ, rít, gầm gừ và ngôn ngữ cơ thể. Mèo trong các bầy đàn sử dụng cả âm thanh lẫn ngôn ngữ cơ thể để giao tiếp với nhau.'''
))
lstAnimal.append(Animal(
    name = 'Con chó',
    img = 'https://static.toiimg.com/photo/msid-67586673/67586673.jpg?resizemode=4&width=400',
    caption= 'Ảnh con chó',
    video = 'https://www.youtube.com/watch?v=l6FN5RG14Lg',
    audio = 'cat-meow.wav',
    description = '''Chó (danh pháp khoa học: Canis lupus familiaris) là một loài động vật có vú thuộc họ Chó (Canidae). Chó là loài vật đầu tiên được thuần hóa từ loài sói xám (Canis lupus) vào khoảng 15.000 năm trước.[2] Chó được nuôi làm thú cưng, chó săn, chó bảo vệ, chó dẫn đường, chó cứu hộ, và nhiều công việc khác. Chó cũng được sử dụng trong các hoạt động thể thao như đua chó và chó kéo xe. Chó có khả năng học hỏi và tuân theo các mệnh lệnh của con người, và chúng có thể hiểu được từ 165 đến 250 từ và cử chỉ, tùy theo giống chó (giống chó biên tập''')
)
lstAnimal.append(Animal(
    name = 'Con thỏ',
    img = 'https://static.toiimg.com/photo/msid-67586673/67586673.jpg?resizemode=4&width=400',
    caption= 'Ảnh con thỏ',
    video = 'https://www.youtube.com/watch?v=l6FN5RG14Lg',
    audio = 'cat-meow.wav',
    description = '''Thỏ là loài động vật có vú thuộc họ Thỏ (Leporidae) trong bộ Gặm nhấm (Lagomorpha). Chúng có kích thước nhỏ, tai dài, chân sau mạnh mẽ và đuôi ngắn. Thỏ thường sống trong các hang động hoặc tổ dưới đất và có khả năng sinh sản nhanh chóng. Chúng ăn cỏ, lá cây và các loại thực vật khác. Thỏ được nuôi làm thú cưng và cũng được sử dụng trong nghiên cứu khoa học.'''
))
lstAnimal.append(Animal(
    name = 'Con chim',
    img = 'https://static.toiimg.com/photo/msid-67586673/67586673.jpg?resizemode=4&width=400',
    caption= 'Ảnh con chim',
    video = 'https://www.youtube.com/watch?v=l6FN5RG14Lg',
    audio = 'cat-meow.wav',
    description = '''Chim là loài động vật có vú thuộc lớp Aves trong ngành Chân khớp (Arthropoda). Chúng có cánh, lông vũ và mỏ, và thường có khả năng bay. Chim sống ở khắp nơi trên thế giới, từ rừng nhiệt đới đến sa mạc và vùng cực. Chúng ăn nhiều loại thức ăn khác nhau, bao gồm hạt, côn trùng và cá. Chim đóng vai trò quan trọng trong hệ sinh thái bằng cách giúp thụ phấn cho cây cối và kiểm soát số lượng côn trùng.'''
))
lstAnimal.append(Animal(
    name = 'Con cá',
    img = 'https://static.toiimg.com/photo/msid-67586673/67586673.jpg?resizemode=4&width=400',
    caption= 'Ảnh con cá',
    video = 'https://www.youtube.com/watch?v=l6FN5RG14Lg',
    audio = 'cat-meow.wav',
    description = '''Cá là loài động vật có vú thuộc lớp Pisces trong ngành Chân khớp (Arthropoda). Chúng sống trong nước và có vây để bơi. Cá có nhiều loại khác nhau, từ cá nhỏ như cá vàng đến cá lớn như cá mập. Chúng ăn nhiều loại thức ăn khác nhau, bao gồm tảo, côn trùng và các loài cá khác. Cá đóng vai trò quan trọng trong hệ sinh thái bằng cách giúp duy trì cân bằng sinh học trong các hệ thống nước ngọt và nước mặn.'''
))

def ShowAnimalInfo(animal):
    with col6:
        st.title(animal.name)
        st.write(animal.description)
        st.write(f'Tiếng {animal.name} kêu')
        st.audio(animal.audio)
        st.write(f'Video {animal.name}')
        st.video(animal.video, format='video/mp4')
    with col7:
        st.image(animal.image, caption=animal.caption)

lstCols = st.columns(len(lstAnimal))
col6, col7 = st.columns([2, 1])
    
for i in range(len(lstAnimal)):
    with lstCols[i % len(lstCols)]:
        if st.button(lstAnimal[i].name, key=lstAnimal[i].name):
            ShowAnimalInfo(lstAnimal[i])