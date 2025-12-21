import streamlit as st
import pandas as pd
st.set_page_config(page_title="Biểu đồ Số Giờ Học và Điểm Số", page_icon="📊", layout="wide")
data = pd.read_csv('Data/data5.8.csv')
st.subheader("Dữ liệu Số Giờ Học và Điểm Số")
des = data.describe()
des.index = ['Tổng số dòng', 'Trung bình', 'Độ lệch chuẩn', 'Giá trị nhỏ nhất', '25%', '50%', '75%', 'Giá trị lớn nhất']
st.write(des)
bieudo = pd.DataFrame(data)
st.subheader("Biểu đồ giữa số giờ học và điểm số")
st.vega_lite_chart(data, {
    "layer": [
        {
            "mark": {"type": "point", "filled": True},
            "encoding": {
                "x": {"field": "Số Giờ Học", "type": "quantitative"},
                "y": {"field": "Điểm Số", "type": "quantitative"}
            }
        },
        {
            "": {"type": "line", "color": "red"},
            "transform": [{"loessmark": "Điểm Số", "on": "Số Giờ Học"}],
            "encoding": {
                "x": {"field": "Số Giờ Học", "type": "quantitative"},
                "y": {"field": "Điểm Số", "type": "quantitative"}
            }
        }]})