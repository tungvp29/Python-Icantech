import streamlit as st

URL='https://thenollywoodreporter.com/wp-content/uploads/2025/07/Justin-Bieber-.webp'
col1,col2=st.columns(2)

with st.sidebar:
    st.image(URL, caption='Justin Bieber')
    st.write('tuổi:31')
    st.write('nghề nghiệp: ca sĩ, nhạc sĩ')
    st.write('Justin Drew Bieber (/biːbər/ BEE-bər; sinh ngày 1 tháng 3 năm 1994)[1][2] là một nam ca sĩ kiêm sáng tác nhạc người Canada. Bieber nổi tiếng nhờ khả năng kết hợp đa dạng nhiều dòng nhạc và là nghệ sĩ đóng vai trò quan trọng trong nền âm nhạc đại chúng hiện nay.[3] Anh được giám đốc điều hành thu âm người Mỹ Scooter Braun phát hiện và ký hợp đồng với RBMG Records vào năm 2008, sau đó gây chú ý với việc phát hành EP 7 ca khúc đầu tay My World (2009) và sớm trở thành một thần tượng tuổi teen.')

st.header('Audio ca khúc')
st.write('Stay')
st.audio('stay.mp3')

st.header('video ca khúc')
st.write('stay')
st.video('https://www.youtube.com/watch?v=kTJczUoc26U')

st.header('audio ca khúc')
st.write('ghost')
st.audio('ghost.mp3')

st.header('video ca khúc')
st.write('ghost')
st.video('https://www.youtube.com/watch?v=Fp8msa5uYsc')

st.header('audio ca khúc')
st.write('holy')
st.audio('holy.mp3')

st.header('video ca khúc')
st.write('holy')
st.video('https://www.youtube.com/watch?v=pvPsJFRGleA')

