def countchar():
    f=open("E:\\TEXT FILES\\WAP to count the number of characters.txt","r")
    st=f.read()
    l=len(st)
    print("The no of characters :",l)
    f.close()
countchar()
