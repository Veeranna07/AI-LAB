num=int(input("Enter a Number to check Prime or not : "))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is NOT a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is NOT a prime number")