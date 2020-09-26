while(True):
    extus={'harshil':'123','yuvraj':'123','nimit':'123','dipesh':'1011'}
    l1=list(dict.keys(extus))
    l2=list(dict.values(extus))
    print("1==>login")
    print("2==>quit")
    ch=int(input("enter the choice"))
    if(ch==1):
        user=input("enter the user id")
        pasw=input("enter the password")
        if(user=="admin"):
            if(pasw=="admin123"):
                print("path of admin")

        for i in l1:
            if(i==user):
                ind=l1.index(i)
                if(l2[ind]==pasw):
                    print("path of customer")
    elif(ch==2):
        print("bye bye....thank you")
        break
    else:
        print("wrong choice")
         
