def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

n=int(input("Enter a number: "))
for i in range(1,n+1):
    print("factorial of numbers",i,":",fact(i))