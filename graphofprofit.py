def gfp():
    import matplotlib.pyplot as mp
    Profit=['2014','2015','2016','2017','2018']
    l=()
    l1=[]
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
    mycursor=mydb.cursor()
    mycursor.execute("select profit from profit")
    myrecord=mycursor.fetchall()
    for i in myrecord:
        l=l+i
    l1=list(l)
    mp.plot(Profit,l1,color='y',label='Overall Profit Of Hotel')
    mp.ylabel('year')
    mp.xlabel('Profit in ($)')
    mp.show()
    return()
