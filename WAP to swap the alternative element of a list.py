def swaplist(a):
    n=len(a)
    if n%2!=0:
        n=n-1
    for i in range(0,n,2):
        a[i],a[i+1]=a[i+1],a[i]
    return a
b=eval(input("Enter the list :"))
x=swaplist(b)
print(x)
        
    
