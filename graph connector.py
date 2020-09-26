import _init_
c="y"
while(c=="y"):
    print("1.graph of expense")
    print("2.graph of income")
    print("3.graph of overall profit")
    print("4.ext")
    ch=int(input("enter your choice"))
    if(ch==1):
        goe()
    elif(ch==2):
        goi()
    elif(ch==3):
        gfp()
    else:
        break
