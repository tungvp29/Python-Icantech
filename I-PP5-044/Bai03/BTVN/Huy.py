import pandas as pd
import streamlit as st
data = pd.read_csv("pyramid.csv")
st.vega_lite_chart(data,
    {
        "mark": {"type" : "arc"},
        "encoding": {
            "theta": {
                "field": "value", "type": "quantitative",
                "scale": {"range": [2.35619449, 8.639379797]},
            },
            "color": {
                "field": "category","type": "nomial",
                "scale": {
                    "domain": ["Bầu trời", "Mặt tối", "mặt sáng"],
                    "range": ["#416D9D", "#674028", "#DEAC58"]
                },
                "legend": {
                    "orient": "right","title": "Chú thích màu sắc",
                }},
            "order": {"field": "order"}
        }
    })  