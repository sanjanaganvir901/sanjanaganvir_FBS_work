def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
num=int(input("Enter a number:"))
if num<=0:
    print("Enter another number")
else:
    result=fact(num)
print("Fctorial of given number is:",result)