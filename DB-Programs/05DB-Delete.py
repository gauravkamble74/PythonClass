import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='garry74',database='python_batch01')
curs=con.cursor()

try:
    no=int(input("Enter account Number"))
    curs.execute("delete from accounts where accno=%d" %no)
    con.commit()
    if curs.rowcount>0:
        print("Account Deleted")
    else:
        print('Account does not exist')
except:
    print('Error deleting the account')

con.close()