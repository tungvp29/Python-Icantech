import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Data Visualization Example",
    layout="wide"
)
data = pd.read_csv('Data/data5.8.csv')
st.subheader('Bang du lieu goc')
st.dataframe(data)
st.write('So luong du lieu None: ', data.isnull().sum().sum())
st.write('So luong du lieu bi lap: ', data.duplicated().sum())
st.subheader("bang thong ke du lieu")
des = data.describe()
des.index = [
    'Tong so dong', 'GT trung binh',
    'Do lech chuan', 'GTNN',
    'Gia tri trung vi 25%', 'Gia tri trung vi 50%', 'Gia tri trung vi 75%', 
    'GTLN'
]
st.write(des)
st.subheader('Bieu do Scatter Plot voi duong xu huong')
st.vega_lite_chart(data, {
    'layer': [
        {
            'mark': {'type': 'point', 'filled': True},
            'encoding': {
                'x': {'field': 'Số Giờ Học', 'type': 'quantitative'},
                'y': {'field': 'Điểm Số', 'type': 'quantitative'},
            }
        }
    ]
})