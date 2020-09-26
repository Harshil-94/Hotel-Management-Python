def recpnew():
    from customerfeedback import custfeed
    class hotelfarecal:

        def __init__(self,amount=0,bill=0,rt='',e=" ",s=0,p=0,age=0,phn=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=101):
            print ("\n\n*****WELCOME TO NEST HOTEL*****\n")

            self.rt=rt

            self.r=r

            self.t=t

            self.p=p
            self.bill=bill
            self.s=s
            self.a=a
            self.name=name
            self.address=address
            self.cindate=cindate
            self.coutdate=coutdate
            self.rno=rno
            self.phn=phn
            self.age=age
            self.e=e
            self.amount=amount
        def inputdata(self):
            self.name=input("\nEnter your name:")
            self.address=input("\nEnter your address:")
            self.cindate=input("\nEnter your check in date:")
            self.coutdate=input("\nEnter your checkout date:")
            self.phn=int(input("\n Enter your phone no:"))
            self.age=int(input("\n Enter your age:"))
            self.e=input("\n Enter your email address:")
            self.bill=int(input("/n enter the bill no"))
            print("Your room no.:",self.rno,"\n")
            self.amount=0
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="hotel")
            mycursor=mydb.cursor()
            mycursor.execute("insert into customer values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(self.name,self.address,self.age,self.e,self.phn,self.cindate,self.coutdate,self.bill,self.amount))
            mydb.commit()
        
            

    def main():

        a=hotelfarecal()
        

        while (1):
            print("1.Enter Customer Data")

            print("2.EXIT")

            b=int(input("\nEnter your choice:"))
            if (b==1):
                a.inputdata()

            
            if (b==2):

                break



    main()


