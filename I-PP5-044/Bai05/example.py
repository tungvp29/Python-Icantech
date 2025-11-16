import streamlit as st
import pandas as pd
import random as rd

data = pd.read_csv('pydc5_5.csv')

st.subheader('Dữ liệu gốc')
st.dataframe(data)

data2 = data.copy()
st.subheader('Dữ liệu đã sao chép (thêm dòng mới)')
newdata = {'Tên': 'Tung', 'Toán': 6, 'Văn': 5}
data2 = data2._append(newdata, ignore_index=True, verify_integrity=True)
st.dataframe(data2)

# st.write(data2.shape)
data2.insert(loc=1, 
             column='Anh', 
             value=[float(rd.randint(1, 10)) for _ in range(data2.shape[0])])
st.subheader('Dữ liệu trước khi tính tổng')
st.dataframe(data2)
data2 = data2.mul([1,2,1,1], axis=1)
st.subheader('Dữ liệu sau khi nhân hệ số 2')
st.dataframe(data2)

st.subheader('Tính tổng:')
data2.insert(loc=4, 
             column='Tổng', 
             value= data2.sum(axis=1, numeric_only=True))    
st.dataframe(data2)

# for label, content in data2.items():
#     if (label == 'Tên'):
#         st.write(content)
# for index, content in data2.iterrows():
#     if (index == 1):
#         # st.write(index)
#         st.write(content)

st.subheader('Top 2 bạn có tổng điểm cao nhất')
st.dataframe(data2.nlargest(2, 'Tổng'))
st.subheader('Top 2 bạn có tổng điểm thấp nhất')
st.dataframe(data2.nsmallest(2, 'Tổng'))

