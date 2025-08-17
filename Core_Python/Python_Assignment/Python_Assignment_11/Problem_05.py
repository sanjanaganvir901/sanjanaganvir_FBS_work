n=int(input("Enter number of elements:"))
lst=[]

for i in range(n):
    lst.append(input(f"Enter element{i+1}: "))

for i in range(len(lst)-1):
    for j in range(len(lst)-i-1):
        if len(lst[j])>len(lst[j+1]):
            lst[j],lst[j+1]=lst[j+1],lst[j]

print("Sorted List by Length: ",lst)