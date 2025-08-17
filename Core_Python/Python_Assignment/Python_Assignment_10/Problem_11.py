size=int(input("Enter a number of elements:"))
list1=[]

for i in range(size):
    num=int(input(f"Enter number{i+1}:"))
    list1.append(num)
m=int(input("Enter value of m:"))
n=int(input("Enter value of n:"))
print(f"Number is divisible by {m} and {n}: ")
for num in list1:
    if num%m==0 and num%n==0:
        print(num)