d={}
ch="Y"
while ch=="Y":
    productname=input("Enter the Product Name :")
    price=float(input("Enter the Price of the Product :"))
    d[productname]=price
    ch=input("DO you want to continue?(Y?N)")
ch="Y"
while ch=="Y":
    for i in range(i):
        search=input("Enter th Product Name to search :")
        print(d.get(search,"Sorry...Not present"))
        ch=input("Do u want to continue?(Y/N)")
        
