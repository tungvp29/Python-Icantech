import streamlit as st
import pandas as pd

khach_hang = pd.read_csv('../Data/data8.1.csv')
lich_su = pd.read_csv('../Data/data8.2.csv')

#Ctrl + C => clipboard
pd.read

st.subheader('Dữ liệu khách hàng')
st.data_editor(khach_hang)

st.subheader('Lịch sử giao dịch')
st.dataframe(lich_su)

merge_data = pd.merge(khach_hang, lich_su, on='ID Khách hàng')
st.subheader('Dữ liệu sau khi ghép nối')
st.dataframe(merge_data)

st.subheader('Khách hang có khả năng rời bỏ:')
st.dataframe(merge_data.nsmallest(2, ['Thu nhập', 'Điểm tín dụng']))

st.subheader('Khách hang có khả năng mua hàng trong tháng tới')
data = merge_data.sort_values(by='Ngày', ascending=False).head(4).nlargest(2, 'Thu nhập')
st.dataframe(data)

st.subheader('Khách hàng có khả năng chi tiêu nhiều hơn cho sản phẩm:')
st.dataframe(merge_data.nlargest(2, ['Thu nhập', 'Điểm tín dụng']))

st.dataframe(merge_data.describe())