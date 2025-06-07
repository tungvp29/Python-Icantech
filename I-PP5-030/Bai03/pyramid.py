import pandas as pd
import streamlit as st

data = pd.read_csv('pyramid.csv')
chart_data = pd.DataFrame(data)
print(chart_data)
st.vega_lite_chart(chart_data, {    
    'mark': {'type': 'arc'},
    'encoding': {
        'theta': {
            'field': 'value',
            'type': 'quantitative',
            'scale': {'range': [2.356, 8.639]},
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
                'title': 'Chú thích màu sắc',
            }
        },
        'order': {
            'field': 'order',
        }
    }
})