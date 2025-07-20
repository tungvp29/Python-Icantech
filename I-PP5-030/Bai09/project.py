import streamlit as st
import pandas as pd

data = pd.read_csv('Data/data.csv')
#làm sạch dữ liệu
data = data.dropna()  # loại bỏ các hàng có giá trị NaN
data = data.drop_duplicates()  # loại bỏ các hàng trùng lặp

st.write('Bảng dữ liệu sau khi làm sạch:')
st.dataframe(data)
des = data.describe()
des.index = [
    'Tổng số dòng', 'GT Trung bình', 
    'Độ lệch chuẩn', 'GTNN', 
    'Giá trị trung vị 25%', 'Giá trị trung vị 50%', 'Giá trị trung vị 75%', 'GTLN']
st.write(des)

dsNha100 = data[data['Giá bán/m2'] >= 100]
st.write('Dữ liệu nhà có giá bán/m2 >= 100:')
st.dataframe(dsNha100)

max_GB = data['Giá bán/m2'].max()
min_GB = data['Giá bán/m2'].min()
infoMax = data[data['Giá bán/m2'] == max_GB]
infoMin = data[data['Giá bán/m2'] == min_GB]

st.write('Dữ liệu nhà có giá bán/m2 lớn nhất:')
st.dataframe(infoMax)
tenQUan = infoMax['Quận/Huyện'].unique()[0]
st.write(f'Quận {tenQUan} có nhà có giá bán/m2 lớn nhất là {round(max_GB, 2)}')

st.write('Dữ liệu nhà có giá bán/m2 nhỏ nhất:')
st.dataframe(infoMin)
tenQUan = infoMin['Quận/Huyện'].unique()[0]
st.write(f'Quận {tenQUan} có nhà có giá bán/m2 nhỏ nhất là {round(min_GB, 2)}')

max_GiaTong = data['Giá bán (tổng)'].max()
min_GiaTong = data['Giá bán (tổng)'].min()
infoMax = data[data['Giá bán (tổng)'] == max_GiaTong]
infoMin = data[data['Giá bán (tổng)'] == min_GiaTong]
st.write('Loại hình nhà ở có giá bán (tổng) lớn nhất:', infoMax['Loại hình nhà ở'].unique()[0])
st.dataframe(infoMax)
st.write('Loại hình nhà ở có giá bán (tổng) nhỏ nhất:', infoMin['Loại hình nhà ở'].unique()[0])
st.dataframe(infoMin)