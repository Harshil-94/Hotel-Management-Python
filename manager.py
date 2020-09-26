def manager():
    from graphconnector import gc
    import time
    c="y"
    while(c=="y"):    
        print("1.employee details")
        print("2.customer details")
        print("3.hotel P&L")
        print("4.customer feedback")
        print("5.exit")
        ch=int(input("enter your choice"))
        if(ch==1):
            while(c=="y"):
                print("1.receptionist")
                print("2.cleaning staff")
                print("3.laundry staff")
                print("4.game staff")
                print("5.manager info")
                print("6.resturant staff")
                print("7.exit")
                ch1=int(input("enter your choice"))
                if(ch1==1):
                    import mysql.connector
                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
                    mycursor=mydb.cursor()
                    mycursor.execute("select * from staff where designation='receptionist'")
                    myrecord=mycursor.fetchall()
                    for (name,age,workhour,salary,designation) in myrecord:
                        print("=====================================")
                        print("staff name :",name)
                        print("staff age :",age)
                        print("staff workhour :",workhour)
                        print("staff salary :",salary)
                        print("staff designation :",designation)
                        time.sleep(1)


                    
                elif(ch1==2):
                    import mysql.connector
                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
                    mycursor=mydb.cursor()
                    mycursor.execute("select * from staff where designation='cleaner'")
                    myrecord=mycursor.fetchall()
                    for (name,age,workhour,salary,designation) in myrecord:
                        print("=====================================")
                        print("staff name :",name)
                        print("staff age :",age)
                        print("staff workhour :",workhour)
                        print("staff salary :",salary)
                        print("staff designation :",designation)
                        time.sleep(1)
                elif(ch1==3):
                    import mysql.connector
                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
                    mycursor=mydb.cursor()
                    mycursor.execute("select * from staff where designation='laundry'")
                    myrecord=mycursor.fetchall()
                    for (name,age,workhour,salary,designation) in myrecord:
                        print("=====================================")
                        print("staff name :",name)
                        print("staff age :",age)
                        print("staff workhour :",workhour)
                        print("staff salary :",salary)
                        print("staff designation :",designation)
                        time.sleep(1)
                elif(ch1==4):
                    import mysql.connector
                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
                    mycursor=mydb.cursor()
                    mycursor.execute("select * from staff where designation='gaming room staff'")
                    myrecord=mycursor.fetchall()
                    for (name,age,workhour,salary,designation) in myrecord:
                        print("=====================================")
                        print("staff name :",name)
                        print("staff age :",age)
                        print("staff workhour :",workhour)
                        print("staff salary :",salary)
                        print("staff designation :",designation)
                        time.sleep(1)
                elif(ch1==5):
                    import mysql.connector
                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
                    mycursor=mydb.cursor()
                    mycursor.execute("select * from staff where designation='manager'")
                    myrecord=mycursor.fetchall()
                    for (name,age,workhour,salary,designation) in myrecord:
                        print("=====================================")
                        print("staff name :",name)
                        print("staff age :",age)
                        print("staff workhour :",workhour)
                        print("staff salary :",salary)
                        print("staff designation :",designation)
                        time.sleep(1)
                elif(ch1==6):
                    import mysql.connector
                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
                    mycursor=mydb.cursor()
                    mycursor.execute("select * from staff where designation='resturant'")
                    myrecord=mycursor.fetchall()
                    for (name,age,workhour,salary,designation) in myrecord:
                        print("=====================================")
                        print("staff name :",name)
                        print("staff age :",age)
                        print("staff workhour :",workhour)
                        print("staff salary :",salary)
                        print("staff designation :",designation)
                        time.sleep(1)
                elif(ch1==7):
                    break
                else:
                    print("wrong choice")
                    
                    
        elif(ch==2):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
            mycursor=mydb.cursor()
            mycursor.execute("select * from customer")
            myrecord=mycursor.fetchall()
            for (name,address,age,emailid,phno,cindate,coutdate,billno,amount) in myrecord:
                print("=====================================")
                print("customer name :",name)
                print("customer address :",address)
                print("customer age :",age)
                print("customer emailid :",emailid)
                print("customer phno :",phno)
                print("customer check in date :",cindate)
                print("customer check out date :",coutdate)
                print("customer bill number:",billno)
                print("amount:",amount)
                time.sleep(1)

        elif(ch==3):
            gc()
                    
                
        elif(ch==4):
                import mysql.connector
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
                mycursor=mydb.cursor()
                mycursor.execute("select * from feedback")
                myrecord=mycursor.fetchall()
                for (name,email,comment) in myrecord:
                    print("=====================================")
                    print("customer name :",name)
                    print("customer email:",email)
                    print("customer comment :",comment)
                    time.sleep(1)

        elif(ch==5):
            break
