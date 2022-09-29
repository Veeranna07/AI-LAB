n=int(input("Enter a Number : "))
fact=1
if n==0:
    print("1")
elif n<0:
    print("Factorial does not exit...")
else:
    for i in range(1,n+1):
        fact*=i
    print("Factorial of",n,"=",fact)
