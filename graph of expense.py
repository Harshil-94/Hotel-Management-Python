def goe():
    import matplotlib.pyplot as mp
    Expenses=['2014','2015','2016','2017','2018']
    l=()
    l1=[]
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
    mycursor=mydb.cursor()
    mycursor.execute("select expense from pnl")
    myrecord=mycursor.fetchall()
    for i in myrecord:
        l=l+i
    l1=list(l)
    mp.barh(Expenses,l1,align='center',color='r',label='P&L Expenses')
    mp.ylabel('year')
    mp.xlabel('expense in ($)')
    mp.show()
    return()

