import pandas as pd

myDict = {
    'films':['znmd','yjhd','ddlj','kbbg','soty','tere naam'],
    'relyr':[2012,2011,2001,2002,2018,1996],
    'actor':['hritik','ranbir','kajol','ab','varun','salman'],
    'director':['javed','karan','yrf','sony','yrf','tseries']
}

print(myDict)

df = pd.DataFrame.from_dict(myDict)
print(df)
df.to_json('films.json')
print("Data written to JSON Successfully")

