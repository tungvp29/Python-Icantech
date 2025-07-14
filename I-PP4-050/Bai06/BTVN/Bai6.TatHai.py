import streamlit as st
p=0
ten=st.text_input("nhap ten ban")
tuoi=st.text_input("ban bao nhieu tuoi?:")
so_thich=st.text_input("so thich cua ban la gi?:")
dia_chi=st.text_input("nhap dia chi nha ban:")
if ten !="":
    p += 25
if tuoi !="":
    p +=25
if so_thich != "":
    p +=25
if dia_chi !="":
    p +=25    
st.progress(p)
button=st.button("gui thong tin")
if button:
    if p==100:
        st.balloons()
        st.write("thong tin da duoc gui")
    else:
        st.write("chua nhap du thong tin")