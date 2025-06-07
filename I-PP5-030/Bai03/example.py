import pandas as pd
import streamlit as st

# data = [{'Rank': 1,'Score': 28},
#         {'Rank': 2,'Score': 55},
#         {'Rank': 3,'Score': 43},
#         {'Rank': 4,'Score': 19},
#         {'Rank': 5,'Score': 87}]

data = pd.read_csv('score.csv')
chart_data = pd.DataFrame(data)
print(chart_data)
st.vega_lite_chart(chart_data, {
    'layer': [
        {
            'transform': [
                {'sample': 10}
            ],
            'mark': {'type': 'point', 
                     'filled': True, 
                     'size': 500,},
            'encoding': {
                'x': {'field': 'Hours', 'type': 'nominal'},
                'y': {'field': 'Scores', 'type': 'quantitative'}
            }
        },
        {
            'mark': {
                'type': 'line',
                'color': 'firebrick',
                'point': True
            },
            'transform': [
                {
                    'loess': 'Hours',
                    'on': 'Scores'
                }
            ],
            'encoding': {
                'x': {'field': 'Hours', 'type': 'quantitative'},
                'y': {'field': 'Scores', 'type': 'quantitative'}
            }
        },
        {
            'mark': {
                'type': 'line',
                'color': 'steelblue',
            },
            'transform': [
                {
                    'regression': 'Hours',
                    'on': 'Scores'
                }
            ],
            'encoding': {
                'x': {'field': 'Hours', 'type': 'quantitative'},
                'y': {'field': 'Scores', 'type': 'quantitative'}
            }
        }
    ]
})