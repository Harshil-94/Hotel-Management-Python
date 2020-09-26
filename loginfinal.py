from manager import manager
from recpmain import recpmain
from ap import ap
from db import db
from ds import ds
from hc import hc
from hs import hs
from ma import ma
from nh import nh
from vg import vg
from ya import ya
while(True):
    l1=["harshil","nimit","yuvraj","dipesh","adarsh","dev","himanshu","mohit","vivek"]
    l2=["123","123","123","1011","123","123","123","123","123",]
    print("1==>login as manager")
    print("2==>login as staff")
    print("3==>quit")
    ch=int(input("enter the choice"))
    flag=0
    if(ch==1):
        user=input("enter the user id")
        pasw=input("enter the password")
        if(user=="admin"):
            if(pasw=="admin123"):
                manager()
            else:
                flag=1
        else:
            flag=1
        if(flag==1):
            print("wrong admin userid or password")    
    elif(ch==2):
        user=input("enter the user id")
        pasw=input("enter the password")
        len1=len(l1)
        for i in range(0,len1):
            if(l1[i]==user):
                if(l2[i]==pasw):
                    if(user=="nimit"):
                        while(True):
                            print("1.for receptionist")
                            print("2.for your details")
                            print("3. exit")
                            ch2=int(input("enter your choice"))
                            if(ch2==1):
                                recpmain()
                                flag=2
                            elif(ch2==2):
                                nh()
                                flag=2
                            elif(ch2==3):
                                break
                    elif(user=="adarsh"):
                        ap()
                        flag=2
                    elif(user=="dev"):
                        db()
                        flag=2
                    elif(user=="dipesh"):
                        ds()
                        flag=2
                    elif(user=="harshil"):
                        hc()
                        flag=2
                    elif(user=="himanshu"):
                        hs()
                        flag=2
                    elif(user=="mohit"):
                        ma()
                        flag=2
                    elif(user=="vivek"):
                        vg()
                        flag=2
                    elif(user=="yuvraj"):
                        ya()
                        flag=2
                    else:
                        print("wrong input")
                        
    elif(ch==3):
            print("bye bye....thank you")
            break
    else:
            print("wrong choice")
         
