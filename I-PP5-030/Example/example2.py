import pandas as pd
import streamlit as st

data = pd.read_csv('data5.8.csv')
des = data.describe()
st.title('Phân tích dữ liệu với Streamlit')
st.write('Dữ liệu mô tả:')
# đổi tên các index
des.index = ['Số dòng dữ liệu', 'Trung bình', 'Độ lệch chuẩn', 'GTNN', 'GT trung vị 25%', 'GT trung vị 50%', 'GT trung vị 75%', 'GTLN']
print(des)
st.dataframe(des)
chart_data = pd.DataFrame(data)
st.vega_lite_chart(data, {
    'layer': [
        {
            'mark': {'type': 'point', 'filled': True, 'size': 100},
            'encoding': {
                'x': {'field': 'Số Giờ Học', 'type': 'quantitative'},
                'y': {'field': 'Điểm Số', 'type': 'quantitative'}
            }
        },
        {
            'mark': {'type': 'line', 'color': 'firebrick'},
            'transform': [
                {
                    'regression': 'Điểm Số',
                    'on': 'Số Giờ Học'
                }
            ],
            'encoding': {
                'x': {'field': 'Số Giờ Học', 'type': 'quantitative'},
                'y': {'field': 'Điểm Số', 'type': 'quantitative'}
            }
        }
    ]
})

st.write('Dựa trên biểu đồ, ta có thể thấy rằng **số giờ học** càng nhiều thì **điểm số** càng cao. Tuy nhiên, vẫn có một số điểm ngoại lai thể hiện điểm số không hoàn toàn bị ảnh hưởng bởi số giờ học.')