n=int(input("Enter number of elements: "))
list1=[]

for i in range(n):
    list1.append(int(input(f"Enter element{i+1}: ")))

for i in range(len(list1)-1):
    for j in range(len(list1)-i-1):
        if list1[j]<list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]

print("Second Lrgest Number:",list1[1])