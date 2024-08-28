def replace():
    f=open("E:\\TEXT FILES\\WAP to replace i by e.txt","r")
    st=f.read()
    l=st.replace("i","e")
    print(l)
    f.close()
replace()
