import streamlit as st

st.image(image = ['assets/image/Lion-species-hero-c-George-Logan.jpg',
                  'assets/image/zebra-high-quality-png.png'],
         caption=['Lion species hero c George Logan',
                  'Zebra high quality PNG'],
         use_container_width=True
         )

st.write("This is a happy dog image from the internet.")

st.image(image = 'https://www.rawpixel.com/image/6169402/png-element-nature',
         caption='Lion species hero c George Logan',
         use_container_width=True
         )

st.audio('assets/audio/ConGiDepHon.mp3', autoplay=True)

st.video('https://www.youtube.com/watch?v=IXgmTBG7Il8')