import pandas as pd
import streamlit as st

data = pd.read_csv('data/movies.csv')
print(data)

# st.line_chart(data, x='Hours', y='Scores')

# st.area_chart(data, x='Hours', y='Scores')

# st.bar_chart(data, x='Hours', y='Scores')

st.vega_lite_chart(data, {
    'layer': [
        {
            'transform':[
               { 'sample': 50}
            ],
            'mark': {
                'type': 'point',
                'filled': True,
            },
            'encoding': {
                'x': {
                    'field': 'Rotten Tomatoes Rating', 
                    'type': 'quantitative'
                },
                'y': {
                    'field': 'IMDB Rating', 
                    'type': 'quantitative'
                }
            }
        },
        {
            'transform': [
                {
                    'loess': 'IMDB Rating',
                    'on': 'Rotten Tomatoes Rating',
                }
            ],
            'mark': {
                'type': 'line',
                'color': 'red',
            },
            'encoding': {
                'x': {
                    'field': 'Rotten Tomatoes Rating', 
                    'type': 'quantitative'
                },
                'y': {
                    'field': 'IMDB Rating', 
                    'type': 'quantitative'
                }
            }
        },
        {
            'transform': [
                {
                    'regression': 'IMDB Rating',
                    'on': 'Rotten Tomatoes Rating',
                }
            ],
            'mark': {
                'type': 'line',
                'color': 'green',
            },
            'encoding': {
                'x': {
                    'field': 'Rotten Tomatoes Rating', 
                    'type': 'quantitative'
                },
                'y': {
                    'field': 'IMDB Rating', 
                    'type': 'quantitative'
                }
            }
        }
    ]

})