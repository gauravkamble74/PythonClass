import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='garry74',database='python_batch01')
curs=con.cursor()

try:
    ano=int(input("enter account number "))
    anm=input("Enter account name ")
    aty=input("Enter account type ")
    bal=float(input("Enter Balance"))

    curs.execute("insert into accounts values (%d,'%s','%s',%.2f)"%(ano,anm,aty,bal))
    con.commit()
    print("Account opened successfully")
except:
    print("Error inserting data")
finally:
    con.close()