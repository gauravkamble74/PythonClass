import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='garry74',database='python_batch01')
curs=con.cursor()

curs.execute("select * from accounts;")
data=curs.fetchall()

# print(data)
for rec in data:
    print(rec)

con.close()