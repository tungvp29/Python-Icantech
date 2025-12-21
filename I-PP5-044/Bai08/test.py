import streamlit as st
import pandas as pd

customer_data = pd.read_csv('Data/data8.1.csv')

st.title("Customer Data")
st.write(customer_data)

order_data = pd.read_csv('Data/data8.2.csv')
st.title("Order Data")
st.write(order_data)

merged_data = pd.merge(customer_data, order_data, on='ID khách hàng')
st.title("Merged Data")
st.write(merged_data)

st.dataframe(merged_data.nsmallest(2, ['Thu nhập', 'Điểm tín dụng']))

st.dataframe(merged_data.nlargest(2, ['Thu nhập', 'Điểm tín dụng']))

st.dataframe(merged_data.nlargest(2, ['Thu nhập']).sort_values(by=['Ngày'], ascending=False))

st.dataframe(merged_data.sort_values(by='Ngày').head(4).nlargest(3, ['Điểm tín dụng']))
