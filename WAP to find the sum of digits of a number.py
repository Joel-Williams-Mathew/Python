no=int(input("Enter a number :"))
sum=0
while no!=0:
    d=no%10
    sum=sum+d
    no=no//10
print("Sum of digits=",sum)
