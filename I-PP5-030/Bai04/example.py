import streamlit as st
import pandas as pd

data = pd.read_csv('Data/diemthi2019.csv')
print(data)

df = st.dataframe(data)

# st.bar_chart(data, x='Dia', y='sbd')

st.vega_lite_chart(data, {
    'layer': [
        {
            'mark': {
                'type': 'bar',
                'tooltip': True,
                'color': '#1f77b4'
            },
            'encoding': {
                'x': {
                    'field': 'Dia',
                    'bin': True,
                    'type': 'quantitative',
                    'axis': {
                        'title': 'Điểm môn Địa lý'
                    }
                },
                'y': {
                    'aggregate': 'count',
                    'axis': {
                        'title': 'Số học sinh'
                    }
                }
            }
        }, 
        {
            'mark': {
                'type': 'line',
                'tooltip': True,
                'color': '#FF5733'
            },
            'encoding': {
                'x': {
                    'field': 'Su',
                    'bin': True,
                    'type': 'quantitative',
                    'axis': {
                        'title': 'Điểm môn Lịch sử'
                    }
                },
                'y': {
                    'aggregate': 'count',
                    'axis': {
                        'title': 'Số học sinh'
                    }
                }
            }
        },
        {
            'mark': {
                'type': 'line',
                'tooltip': True,
                'color': '#28A745'
            },
            'encoding': {
                'x': {
                    'field': 'Van',
                    'bin': True,
                    'type': 'quantitative',
                    'axis': {
                        'title': 'Điểm môn Lịch sử'
                    }
                },
                'y': {
                    'aggregate': 'count',
                    'axis': {
                        'title': 'Số học sinh'
                    }
                }
            }
        }
    ]
    
})