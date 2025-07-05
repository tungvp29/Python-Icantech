import pandas as pd
import streamlit as st

data = pd.read_csv('Data/data5.8.csv')
st.dataframe(data)
st.write('Bảng thống kê dữ liệu:')
des = data.describe()
# print(des.index)
des.index = [
    'Tổng số dòng', 'GT Trung bình', 
    'Độ lệch chuẩn', 'GTNN', 
    'Giá trị trung vị 25%', 'Giá trị trung vị 50%', 'Giá trị trung vị 75%', 'GTLN']
# des.columns = ['Cột số giờ học', 'Cột điểm số', 'Cột năm sinh']
st.write(des)