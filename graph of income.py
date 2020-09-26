def goi():
    #graph for the profit of the hotel
    import matplotlib.pyplot as  mp
    Incomes=['2014','2015','2016','2017','2018']
    l=()
    l1=[]
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
    mycursor=mydb.cursor()
    mycursor.execute("select income from pnl")
    myrecord=mycursor.fetchall()
    for i in myrecord:
        l=l+i
    l1=list(l)
    mp.barh(Incomes,l1,align='center',color='g',label='P&L Expenses')
    mp.ylabel('year')
    mp.xlabel('Income in ($)')
    mp.show()
    return()
    
