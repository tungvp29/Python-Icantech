import pandas as pd
import numpy as np

data = {'Col1': [1, 2, np.nan, 4, 5],
        'Col2': ['A', np.nan, 'C', 'D', 'E'],
        'Col3': [True, False, False, np.nan, True]}
df = pd.DataFrame(data)
df.to_csv('PYDC5.6_1.csv', index=False)
print("File PYDC5.6_1.csv đã được tạo.")

import pandas as pd
import streamlit as st
import os

st.title("Thực hành làm sạch dữ liệu với Pandas và Streamlit")

# Xác định đường dẫn đến file CSV
file_path = 'PYDC5.6_1.csv'

if os.path.exists(file_path):
    # Đọc dữ liệu
    df = pd.read_csv(file_path)

    # --- Yêu cầu 1 & 2: Xác định số lượng dữ liệu thiếu ---
    # Đếm tổng số dữ liệu bị thiếu ban đầu
    missing_data_initial = df.isnull().sum().sum()
    
    st.markdown(f"**Số lượng dữ liệu bị thiếu ban đầu:** **{missing_data_initial}**")

    # --- Yêu cầu 1: Xử lý dữ liệu bị thiếu ---
    # Ví dụ xử lý: Xóa các hàng có dữ liệu bị thiếu (bạn có thể dùng fillna() thay thế tùy ý)
    df_cleaned = df.dropna()
    
    st.subheader("Bảng dữ liệu sau khi xử lý (dropna):")
    # --- Yêu cầu 2: In ra bảng dữ liệu sau khi xử lý ---
    st.dataframe(df_cleaned)

    # Hiển thị thông tin thêm về dữ liệu sau xử lý
    missing_data_after = df_cleaned.isnull().sum().sum()
    st.markdown(f"**Số lượng dữ liệu bị thiếu sau xử lý:** **{missing_data_after}**")

else:
    st.error(f"Không tìm thấy file dữ liệu: {file_path}. Vui lòng chạy code tạo file mẫu trước.")
