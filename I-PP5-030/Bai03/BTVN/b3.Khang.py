import streamlit as st
import pandas as pd

data = pd.read_csv('bieudo.csv')
st.line_chart(data, x='thời gian', y='sản lượng')
st.bar_chart(data, x='thời gian', y='sản lượng')
st.area_chart(data, x='thời gian', y='sản lượng')

data1 = pd.read_csv('a.csv')
st.vega_lite_chart(data1,
    {
        'mark': 'arc',
        'encoding': {
            'theta': {'field': 'value', 'type': 'quantitative'},
            'range': ['#416D9D', '#674028', '#DEAC58']
        },
        'legend': {
            'orient': 'right', 'title': 'Chú thích sắc màu'
        }
    }
)
