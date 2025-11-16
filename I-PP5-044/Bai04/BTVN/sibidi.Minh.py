import streamlit as st
import pandas as pd
df = pd.read_csv("diemthi2019.csv")

st.dataframe(df.loc[0:200])

st.vega_lite_chart(df.loc[0:200], {
    "layer": [
        {
            "mark": {
                "type": "circle",
                "color": "blue",
                "filled": True,
            },
            "encoding": {
                "x": {"field": "stt", "type": "quantitative"},
                "y": {"field": "Toan", "type": "quantitative"},
            },
        },
        {
            "mark": {
                "type": "circle",
                "color": "red",
            },
            "encoding": {
                "x": {"field": "stt", "type": "quantitative"},
                "y": {"field": "Li", "type": "quantitative"},
            },
        },
        {
            "mark": {
                "type": "circle",
                "color": "green",
            },
            "encoding": {
                "x": {"field": "stt", "type": "quantitative"},
                "y": {"field": "Hoa", "type": "quantitative"},
            },
        },
    ]
})
#Dia,GDCD,Hoa,Li,Ma_mon_ngoai_ngu,Ngoai_ngu,Sinh,Su,Toan,Van,
st.vega_lite_chart(df.loc[0:200], {
    "mark":  {
                "type": "bar",
                "color": "green",
            },
    "transform": [{
        "calculate": "datum.Toan + datum.Li + datum.Hoa + datum.Sinh + datum.Van + datum.Su + datum.Dia + datum.Ngoai_ngu + datum.GDCD",
        "as": "tong_diem"
    }],
    "encoding": {
        "x": {"field": "stt", "type": "quantitative"},
        "y": {"field": "tong_diem", "type": "quantitative", "aggregate": "sum"},
    },
})