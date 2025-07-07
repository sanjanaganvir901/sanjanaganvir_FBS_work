num=int(input("Enter the number: "))

copy=num

a=num%10
num=num//10
b=num%10
c=num//10
reverse=a*100+b*10+c
print("reverse number:",reverse)

if(copy==reverse):
    print("It is a palindrome number")

else:
    print("It is not a palindrome number")