import pickle
#Creating
def write():
    fil=open("E:\\TEXT FILES\\Binarystud.dat","ab")
    n=int(input("Enter the no. of students :"))
    for i in range(n):
        nm=input("Enter the name :")
        rlno=int(input("Enter the roll number :"))
        mrk=float(input("Enter the mark :"))
        lst=[rlno,nm,mrk]
        pickle.dump(lst,fil)
    fil.close()
    
#Display    
def read():
    f=open("E:\\TEXT FILES\\Binarystud.dat","rb")
    try:
        while True:
            ls=pickle.load(f)
            print("Name :",ls[1],"\t\t","Roll Number :",ls[0],"\t\t","Mark :",ls[2],"%")
    except EOFError:
        f.close()

#Searching
def search():
    f1=open("E:\\TEXT FILES\\Binarystud.dat","rb")
    s=int(input("Enter the roll number to search :"))
    try:
        while True:
            lst=pickle.load(f1)
            for i in lst:
                if lst[0]==s:
                    print("Name :",lst[1],"\t\t","Roll Number :",lst[0],"\t\t","Mark :",lst[2],"%")
                    break
            
    except EOFError:
        f1.close()

def menu():
    while True:
        print("1:Create,2:Display,3:Search,4:Exit")
        c=int(input("\t\t\t\t\tEnter ur choice :"))
        if c==1:
            write()
        elif c==2:
            read()
        elif c==3:
            search()
        else:
            break
menu()
