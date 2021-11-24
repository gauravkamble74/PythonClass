import pandas as pd
import numpy as np

df=pd.read_csv('accounts.csv')
cols=np.array(["Srno","Accno","Accnm","Acctype","Balance"])
df.columns=cols
print(df)

print('__'*50)

print('Filter by condtion')
df1 = df[df["Acctype"]== "saving"]
print(df1)

print('__'*50)

print('Filter by multiple condtions')
df2 = df[(df["Acctype"]=="current") & (df["Balance"]>75000)]
print(df2)