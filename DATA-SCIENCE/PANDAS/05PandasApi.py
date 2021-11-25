import pandas as pd

url="https://v6.exchangerate-api.com/v6/8a70906313adcc4468cf2d4b/latest/USD"

df=pd.read_json(url)
print(df)

df.to_csv("rates.csv")
print("Data written to csv successfuly")