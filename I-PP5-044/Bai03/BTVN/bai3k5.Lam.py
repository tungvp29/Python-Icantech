import streamlit as st
import pandas as pd
file_pyramid = pd.read_csv('pyramid.csv', encoding='utf-8')
dataframe = pd.DataFrame(file_pyramid)
spec = {
    "mark": {"type": "arc"},
    "encoding": {
        "theta": {
            "field": "value",
            "type": "quantitative",
            "scale": {"range": [2.35619449, 8.639379797]}
        },
        "color": {
            "field": "category",
            "type": "nominal",
            "scale": {
                "domain": ["A", "B", "C"],
                "range": ["#1f77b4", "#ff7f0e", "#2ca02c"]
            },
            "legend": {}
        }
    }
}

st.vega_lite_chart(dataframe, spec, use_container_width=True)

