import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Visualization Example",
    layout="wide"
)

data = pd.read_csv('Data/data5.8.csv')

st.subheader('Bảng dữ liệu gốc')
st.dataframe(data)

st.write('Số dòng dữ liệu None:', data.isnull().sum().sum())
st.write('Số dòng dữ liệu bị lặp:', data.duplicated().sum())

st.subheader('Bảng thống kê dữ liệu')
des = data.describe()
des.index = [
    'Tổng số dòng', 'GT Trung bình', 
    'Độ lệch chuẩn', 'GTNN', 
    'Giá trị trung vị 25%', 'Giá trị trung vị 50%', 'Giá trị trung vị 75%', 
    'GTLN'
]
st.write(des)

st.subheader('Biểu đồ với đường xu hướng')
st.write('Biểu đồ điểm với đường xu hướng (LOESS) thể hiện tương quan giữa số giờ học và điểm số.')
st.vega_lite_chart(data, {
    'layer': [
        {
            'mark': {'type': 'point', 'filled': True},
            'encoding': {
                'x': {'field': 'Số Giờ Học', 'type': 'quantitative'},
                'y': {'field': 'Điểm Số', 'type': 'quantitative'},
            }
        },
        {
            'mark': {'type': 'line', 'color': 'red'},
            'transform': [
                {'loess': 'Điểm Số', 'on': 'Số Giờ Học'},
            ],
            'encoding': {
                'x': {'field': 'Số Giờ Học', 'type': 'quantitative'},
                'y': {'field': 'Điểm Số', 'type': 'quantitative'},
            }
        },
    ]
})

st.write('Biểu đồ điểm với đường xu hướng (LOESS) thể hiện tương quan giữa số giờ học và năm sinh.')
st.vega_lite_chart(data, {
    'layer': [
        {
            'mark': {'type': 'point', 'filled': True},
            'encoding': {
                'x': {'field': 'Số Giờ Học', 'type': 'quantitative'},
                'y': {'field': 'Năm Sinh', 'type': 'quantitative', "scale": {"domain": [2007, 2015]}},
            }
        },
        {
            'mark': {'type': 'line', 'color': 'red'},
            'transform': [
                {'regression': 'Năm Sinh', 'on': 'Số Giờ Học'},
            ],
            'encoding': {
                'x': {'field': 'Số Giờ Học', 'type': 'quantitative'},
                'y': {'field': 'Năm Sinh', 'type': 'quantitative', "scale": {"domain": [2007, 2015]}},
            }
        },
    ]
})