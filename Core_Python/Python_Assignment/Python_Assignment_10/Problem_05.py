n=int(input("Enter how many elements you want in the list: "))
list1=[]

for i in range (n):
    number=int(input(f"Enter element {i+1}: "))
    list1.append(number)
print("Your list:",list1)

ele=int(input("Enter the number to check: "))

count=0
for i in range(len(list1)):
    if(ele==list1[i]):
        count+=1

if count>0:
    print("Yes the number is present")
    print(f"It appears {count} times ")
else:
    print("No the number is not present in the list")