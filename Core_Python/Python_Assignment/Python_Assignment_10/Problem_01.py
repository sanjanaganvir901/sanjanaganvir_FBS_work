n=int(input("Enter a number: "))
list1=[]

for i in range(n):
    num=int(input(f" Enter number{i+1}:"))
    list1+=[num]

sum=0
for i in range(n):
    sum=sum+list1[i]
print("Sum of all elements:",sum)
