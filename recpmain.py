from recpnew import recpnew
from recpexist import recpexist
def recpmain():
    while(True):
        print("1.new customer")
        print("2.existing customer")
        print("3.exit")
        ch3=int(input("enter your choice"))
        if(ch3==1):
            recpnew()
        elif(ch3==2):
            recpexist()
        elif(ch3==3):
            break
        else:
            print("wrong choice")
        
        
    
