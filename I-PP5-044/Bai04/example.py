import streamlit as st
import pandas as pd

#Biểu diễn dưới dạng bảng
filtered_df = pd.read_csv('Data/diemthi2019.csv')
filtered_df = filtered_df.loc[0:200]
st.dataframe(filtered_df)

#Biểu diễn dưới dạng biểu đồ 1: Tổ hợp các môn Toán - Lý - Hóa hoặc Văn - Sử - Địa
st.vega_lite_chart(filtered_df, {
    'layer': [
        #Lớp biểu đồ đầu tiên
        {
            'mark': {
                'type': 'circle', 
                'color': 'blue', 
                'filled': True},
            'encoding': {
                'x': {'field': 'stt', 'type': 'quantitative'},
                'y': {'field': 'Toan', 'type': 'quantitative'}
            },
            'transform': [
                {
                    'filter': 'datum.stt <= 200'
                }
            ]
        },
        #Lớp biểu đồ thứ hai
        {
            'mark': {
                'type': 'circle', 
                'color': 'orange', 
                'filled': True},
            'encoding': {
                'x': {'field': 'stt', 'type': 'quantitative'},
                'y': {'field': 'Li', 'type': 'quantitative'}
            },
            'transform': [
                {
                    'filter': 'datum.stt <= 200'
                }
            ]
        },
        #Lớp biểu đồ thứ hai
        {
            'mark': {
                'type': 'circle', 
                'color': 'green', 
                'filled': True},
            'encoding': {
                'x': {'field': 'stt', 'type': 'quantitative'},
                'y': {'field': 'Hoa', 'type': 'quantitative'}
            },
            'transform': [
                {
                    'filter': 'datum.stt <= 200'
                }
            ]
        },
        
    ]
})

#Biểu diễn dưới dạng biểu đồ 2: Tổng điểm của các học sinh
#Dia,GDCD,Hoa,Li,Ngoai_ngu,Sinh,Su,Toan,Van
st.vega_lite_chart(filtered_df, {
    'mark': {
        'type': 'bar',
        'color': 'lightblue'
    },
    'transform': [
        {
            'calculate': 'datum.Toan + datum.Li + datum.Hoa + datum.Van + datum.Su + datum.Dia + datum.GDCD + datum.Sinh + datum.Ngoai_ngu',
            'as': 'TongDiem'
        },
        {
            'filter': 'datum.TongDiem <= 30'
        }
    ],
    'encoding': {
        'x': {'field': 'stt', 'type': 'ordinal'},
        'y': {'aggregate': 'sum', 'field': 'TongDiem', 'type': 'quantitative'}
    }
})
