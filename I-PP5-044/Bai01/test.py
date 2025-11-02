import pandas as pd
import streamlit as st

#Ví dụ với Series
arr = [1, 'Vũ Phạm Tùng', '01/02/2003', '10A3']
arr1 = {
    'STT': 2, 
    'Họ và tên': 'Nguyễn Nguyên Lâm', 
    'Ngày sinh': '03/04/2005', 
    'Lớp': '9A1'
}

myseries = pd.Series(arr, index=['STT', 'Họ và tên', 'Ngày sinh', 'Lớp'])

myseries1 = pd.Series(arr1)

# print(myseries)
# print("-----")
# print(myseries1)
# print("-----")

#Ví dụ với DataFrame
data = {
    'STT': [1, 2, 3, 4],
    'Họ và tên': ['Vũ Phạm Tùng', 'Nguyễn Nguyên Lâm', 'Trần Văn A', 'Lê Thị B'],
    'Ngày sinh': ['01/02/2003', '03/04/2005', '05/06/2004', '07/08/2002'],
    'Lớp': ['10A3', '9A1', '10A2', '11B1']
}

df = pd.DataFrame(data)
print(df)
print("-----")
# print(df.loc[0])  # Lấy dòng thứ 2 (index 1)
# print(df.loc[[1,3]])  # Lấy dòng thứ 2 (index 1)
# pd.options.display.max_rows = 7
df2 = pd.read_csv('data.csv')
# print("-----")
# print(df2)
# print("-----")
print(df2.info())