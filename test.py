import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
mycursor=mydb.cursor()
mycursor.execute("select * from customer")
myrecord=mycursor.fetchall()
print("----name----address----age----emailid----phoneno----checkin date-----checkout date")
for (name,address,age,emailid,phno,cindate,coutdate) in myrecord:
    print("=====================================")
    print("customer name :",name)
    print("customer address :",address)
    print("customer age :",age)
    print("customer emailid :",emailid)
    print("customer phno :",phno)
    print("customer check in date :",cindate)
    print("customer check out date :",coutdate)
                
