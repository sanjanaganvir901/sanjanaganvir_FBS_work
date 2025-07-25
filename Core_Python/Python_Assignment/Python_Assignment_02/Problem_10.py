# A program to reverse three-digit number.

num = int(input("Enter a three-digit number :"))
# num = 123
a = num % 10 # = 3
num = num // 10 # = 12
b = num % 10 # = 2
c = num // 10 # = 1
print("Reverse of three-digit number :",a,b,c)