def countwords():
    f=open("E:\\TEXT FILES\\WAP to count the no of words.txt","r")
    st=f.read()
    l=st.split()
    h=len(l)
    print("The no of words :",h)
    f.close()
countwords()
