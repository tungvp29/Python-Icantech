#pip install pandas
import pandas as pd

arr = [1, 'TungVP', 10, True]
data = pd.Series(arr, index=['STT', 'Hoten', 'Diem', 'Gioitinh'])
# print(data)

dict = { 'STT': [1, 2, 3],
        'ten': ['TungVP', 'Nguyen Van A', 'Nguyen Van B',],
        'diem': [10, 8, 9],
        'gioitinh': [True, False, True] }

df = pd.DataFrame(dict)
print(df.info())
# print(df)
# print('-------------------')
# dong1 = df.loc[0]
# print(dong1)
# print('-------------------')
# dong13 = df.loc[[0, 2]]
# print(dong13)

df2 = pd.DataFrame(dict, index=['Hs1', 'Hs2', 'Hs3'])
print(df2.loc['Hs1'])
pd.options.display.max_rows = 4
df3 = pd.read_csv('Cars.csv')
print(df3)
print(df3.info())