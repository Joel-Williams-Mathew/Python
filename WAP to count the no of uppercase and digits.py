def uppdigit():
    f=open("E:\\TEXT FILES\\WAP to count the no of uppercase and digits.txt","r")
    st=f.read()
    up=0
    d=0
    for i in st:
        if i.isupper():
            up+=1
        elif i.isdigit():
            d+=1
        else:
            pass
    print("The no of uppercase :",up)
    print("The no of digits :",d)
    f.close()
uppdigit()
