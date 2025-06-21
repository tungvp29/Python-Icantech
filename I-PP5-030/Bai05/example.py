import pandas as pd
import streamlit as st

data = pd.read_csv('pydc5_5.csv')
st.write('Dữ liệu gốc')
st.dataframe(data)

st.write('Dữ liệu đã sao chép')
data_copy = data.copy()
new_row = {'Tên': 'Hoàng', 'Toán': 6, 'Văn': 5}
data_copy = data_copy._append(new_row, ignore_index=True, verify_integrity=True)
# st.dataframe(data_copy)

data_copy.insert(loc=3, column='Anh', value=[1,2,3])
data_copy.insert(loc=4, column='Tổng', value= data_copy.sum(axis=1, numeric_only=True))
st.dataframe(data_copy)

st.write(data_copy.shape[1])

st.write(data_copy.min(numeric_only=True))

# for label, content in data_copy.items():
#     st.write(label)
#     st.write(content)

# for index, content in data_copy.iterrows():
#     st.write(f'Dòng: {index}')
#     st.write(content)

# df2 = pd.DataFrame([{'col1': 10, 'col2': 20, 'col3': 30},
#                     {'col1': 40, 'col2': 50, 'col3': 60}])
# df2 = df2.mul(5)  # Thêm 5 vào mỗi phần tử
# st.dataframe(df2)

# st.write(df2.sum(axis=1))


