import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='garry74',database='python_batch01')
curs=con.cursor()

ano=int(input('Enter account number '))

curs.execute("select accnm,balance from accounts where accno=%d"%ano)
rec = curs.fetchone()

try:
    print("Name : '%s' "%rec[0])
    print("Balance : '%.2f' "%rec[1])
except:
    print('')

con.close()