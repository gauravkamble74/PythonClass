import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='garry74',database='python_batch01')
curs=con.cursor()

curs.execute("select * from accounts order by accnm;")

rec=curs.fetchone()

while rec:
    print(rec)
    rec=curs.fetchone()
    print('_'*50)
con.close()