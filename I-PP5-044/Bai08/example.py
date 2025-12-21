import streamlit as st
import pandas as pd

khach_hang = pd.read_csv('Data/data8.1.csv')
lich_su = pd.read_csv('Data/data8.2.csv')

st.subheader("Dữ liệu khách hàng")
st.dataframe(khach_hang)

st.subheader("Lịch sử giao dịch")
st.dataframe(lich_su)

#merge
merged_data = pd.merge(khach_hang, lich_su, on='ID Khách hàng')
st.subheader("Dữ liệu sau khi ghép nối")
st.dataframe(merged_data)

st.subheader('Khách hàng có khả năng rời bỏ:')
st.dataframe(merged_data.nsmallest(2, ['Thu nhập', 'Điểm tín dụng']))

#khách hàng có thu nhập cao và có mua hàng gần đây
st.subheader('Khách hàng có khả năng mua hàng trong tháng tới:')
data = merged_data.sort_values(by='Ngày', ascending=False).head(4).nlargest(3, 'Thu nhập')
st.dataframe(data)

st.subheader('Khách hàng có khả năng chi tiêu nhiều tiền hơn cho sản phẩm:')
st.dataframe(merged_data.nlargest(2, ['Thu nhập', 'Điểm tín dụng']))

st.subheader('Khách hàng có khả năng phản hồi một chiến dịch tiếp thị cụ thể:')
st.dataframe(merged_data.sort_values(by='Ngày', ascending=True).head(4).nlargest(2, 'Điểm tín dụng'))