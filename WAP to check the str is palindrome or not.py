def palind(a):
    if a==a[::-1]:
        print("It is a PALINDROME")
    else:
        print("It is NOT a plaindrome")
    return a
x=input("Enter the string :")
y=palind(x)

