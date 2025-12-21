import streamlit as st
import pandas as pd

data = pd.read_csv('data.csv')

st.subheader('Kiểm tra bộ dữ liệu')
st.write('Kiểu dữ liệu của các cột:')
st.write(data.dtypes)

st.write('Số lượng giá trị null trong mỗi cột:')
st.dataframe(data.isnull().sum())

st.write(f'Số dữ liệu bị lặp: {data.duplicated(
    subset=['Quận/Huyện', 'Diện tích (m2)', 'Giá bán (tổng)', 'Loại hình nhà ở', 'Giá bán/m2']).sum()}')

st.subheader('Dữ liệu đã kiểm tra:')
st.dataframe(data)

st.subheader('Các căn nhà có giá trị hơn 100 triệu đồng/m2:')
filter_100 = data[data['Giá bán/m2'] > 100]
st.dataframe(filter_100)
st.write(f'Tổng số căn nhà có giá trị hơn 100 triệu đồng/m2: {filter_100.shape[0]} căn')

st.write(f'{data.nlargest(1, 'Giá bán/m2').loc[:, ['Quận/Huyện']].values[0][0]} là quận/huyện có căn nhà đắt nhất với giá {round(data["Giá bán/m2"].max(), 2)} triệu đồng/m2')
st.write(f'{data.nsmallest(1, 'Giá bán/m2').loc[:, ['Quận/Huyện']].values[0][0]} là quận/huyện có căn nhà rẻ nhất với giá {round(data["Giá bán/m2"].min(), 2)} triệu đồng/m2')

st.write(f'{data.nlargest(1, 'Giá bán/m2').loc[:, ['Loại hình nhà ở']].values[0][0]} là loại hình nhà ở có căn nhà đắt nhất với giá {round(data["Giá bán/m2"].max(), 2)} triệu đồng/m2')
st.write(f'{data.nsmallest(1, 'Giá bán/m2').loc[:, ['Loại hình nhà ở']].values[0][0]} là loại hình nhà ở có căn nhà rẻ nhất với giá {round(data["Giá bán/m2"].min(), 2)} triệu đồng/m2')

st.write('Ngôi nhà có giá bán (tổng) cao nhất:')
st.dataframe(data.nlargest(1, 'Giá bán (tổng)'))