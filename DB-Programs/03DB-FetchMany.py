import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='garry74',database='python_batch01')
curs=con.cursor()

curs.execute("select * from accounts;")

while True:
    data=curs.fetchmany(5)
    if not data:
        break
    for rec in data:
        print(rec)

    print('-'*40)
con.close()