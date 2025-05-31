import pandas as pd 

pd.set_option('display.max_columns', None)
pd.options.display.max_rows = 248

data = pd.read_csv('country.csv')
print(data)
print(data.info())