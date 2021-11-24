import pandas as pd
import numpy as np

arr = np.array(
    [
        [12,23,34,45,56,67,78],
        [22,34,65,55,89,54,33],
        [45,56,67,78,78,78,99]
    ]
)

# print(arr)
df = pd.DataFrame(arr)
# print(df)

arr1 = np.array(
    [
        ['hibernate','education','global','english',1450,200],
        ['sweet bengal','tourism','spacetimecinema','bengali',540,120],
        ['git-github','education','global','english',540,221],
        ['data science','education','sharayu','english',380,47],
        ['sql-db','education','soham','english',1270,550],
        ['test cricket','sports','spacetimecinema','english',45809,5748],
        ['install visual studio','education','sohamglobal','english',4732,543],
        ['premier league','sports','soformidable','english',7438,763],
        ['spark','education','sharayuglobal','english',8743,795],
        ['rawangla sikkim','tourism','spacetimecinema','hindi',8694,764],
        ['configure tomcat','education','soal','english',5932,384],
        ['intro to javabeans','education','global','hindi',9484,667],
        ['ramoji hyderabad','tourism','spacetimecinema','telugu',7944,154]
    ]
)

col = np.array(["Title","Category","Channel","Language","Views","Likes"])

df1 = pd.DataFrame(arr1,columns=col)
print(df1)