import pandas as pd

data = [1, 2, 2, 3, 5, 7, 11, 11, 13, 17, 19, 19, 23, 29, 310]

data_mean = pd.Series(data).mean()
data_median = pd.Series(data).median()
data_mode = pd.Series(data).mode()

print(f'Giá trị trung bình: {data_mean}')
print(f'Giá trị trung vị: {data_median}')
print(f'Giá trị xuất hiện nhiều nhất: {data_mode}')