import pandas as pd

df=pd.read_csv("orders.csv")
print(df)
print('*'*30)
print("show status of null id DataFrame")
print(pd.isnull)

print("remove rows with null value")
df1=df.dropna()
print(df1)

print("remove column with null values")
df2=df.dropna(axis=1)
print(df2)

print("rename nulls")
df['userid'].fillna("No ID",inplace=True)
print(df)

print("replace values")
df3=df.replace("confirmed","PLACED")
print(df3)

print("rename column name")
df4=df.rename(columns={'paystatus':'Payment_Status'})
print(df4)