import pandas as pd
import numpy as np


df = pd.read_csv('accounts.csv')
# print(df)

print('first 10 elements')
dfhead = df.head(10)
# print(dfhead)

print('Statistical Information about the file')
df1 = df.describe()
# print(df1)
print(np.round(df1.head(10),2))

