import streamlit as st

st.area_chart()
st.bar_chart()
st.line_chart()

st.vega_lite_chart(data, {
    'mark': {'type': 'arc', 'filled': True},
    'encoding': {
        'theta': {
            'field': 'value',
            'type': 'quantitative',
            'scale': {'range': [4.056, 10.439]}
        }
    }
})