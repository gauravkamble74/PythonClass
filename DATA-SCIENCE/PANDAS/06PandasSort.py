import pandas as pd
import numpy as np

df = pd.read_csv('accounts.csv')

# print(df)
cols=np.array(["Srno","Accno","Accnm","Acctype","Balance"])
df.columns=cols
# print(df)

print('_'*50)
df1=df.sort_values("Balance")
# print(df1)

print('_'*50)
print("Group By")
df2=df.groupby("Acctype")
# print(df2)
# for rec in df2:
#     print(rec)

# print(df2.first())
# print(df2.last())

print(df.groupby("Acctype").groups)