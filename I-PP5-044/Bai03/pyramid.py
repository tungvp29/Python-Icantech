import pandas as pd
import streamlit as st

data = pd.read_csv('Data/pyramid.csv')

st.vega_lite_chart(data, {
    'mark': {
        'type': 'arc'
    },
    'encoding': {
        'theta': {
            'field': 'value',           #cột value
            'type': 'quantitative',     #dạng số
            'scale': {
                'range': [4.056, 10.439]
            }
        },
        'color': {
            'field': 'category',
            'type': 'nominal',
            'scale': {
                'domain': ['Bầu trời', 'Mặt tối', 'Mặt sáng'],
                'range': ['#416d9d', '#674028', '#deac58']
            },
            'legend': {
                'orient': 'right',
                'title': 'Chú thích màu sắc'
            } 
        },
    }
})