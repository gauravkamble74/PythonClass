import mysql.connector as mycon

con=mycon.connect(host="localhost",user='root',password="garry74",database='python_batch01')
curs=con.cursor()

curs.execute("select customers.custnm,products.prodnm,products.company from customers inner join products on customers.prodid=products.prodid;")
data=curs.fetchall()

# print(data)
for i in data:
    print(i)
con.close()
