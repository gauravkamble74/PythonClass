import pandas as pd

df1=pd.read_csv("Customers.csv")
df2=pd.read_csv("orders.csv")

# print(df1)
print('_'*50)
# print(df2)

print('Inner Join')
dfinner=df1.merge(df2,on="userid",how="inner")
# print(dfinner)

print('_'*50)
print('Left outer Join')
dfleft=df1.merge(df2,on="userid",how="left")
# print(dfleft)

print('_'*50)
print('Right outer join')
dfright=df1.merge(df2,on="userid",how="right")
print(dfright)