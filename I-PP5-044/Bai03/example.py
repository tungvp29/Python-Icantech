import pandas as pd
import streamlit as st

data = pd.read_csv('Data/movies.csv')
st.subheader("Bảng dữ liệu Score.csv:")
st.dataframe(data)


# st.line_chart(data, x='Horsepower', y='Cylinders')
# st.line_chart(data, x='Hours', y='Scores')
# st.area_chart(data, x='Hours', y='Scores')

#barchart
# st.bar_chart(data, x='Hours', y='Scores')
#stacked barchart
# st.bar_chart(data)

st.vega_lite_chart(data, {
    'mark': {'type': 'point', 'filled': True},
    'encoding': {
        'x': {'field': 'Rotten Tomatoes Rating', 'type': 'quantitative'},
        'y': {'field': 'IMDB Rating', 'type': 'quantitative'}
    }
})

st.vega_lite_chart(data, {
    'layer': [
        #Lớp bản đồ đầu tiên
        {
            'mark': {'type': 'point', 'filled': True},
            'encoding': {
                'x': {'field': 'Rotten Tomatoes Rating', 'type': 'quantitative'},
                'y': {'field': 'IMDB Rating', 'type': 'quantitative'}
            }
        },
        #Lớp bản đồ thứ hai
        {
            'mark': {'type': 'line', 'color': 'firebrick'},
            'transform': [{
                'loess': 'IMDB Rating',
                'on': 'Rotten Tomatoes Rating'
            }],
            'encoding': {
                'x': {'field': 'Rotten Tomatoes Rating', 'type': 'quantitative'},
                'y': {'field': 'IMDB Rating', 'type': 'quantitative'},
            }
        },
        #Lớp bản đồ thứ ba
        {
            'mark': {'type': 'bar', 'color': 'red', 'opacity': 0.3},
            'encoding': {
                'y': {'field': 'IMDB Votes', 'type': 'quantitative'},
            }
        },
    ]
})

