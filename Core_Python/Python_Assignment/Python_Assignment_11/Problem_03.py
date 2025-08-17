n=int(input("Enter number of sublists: "))
lst=[]
for i in range(n):
    sub=[]
    sub.append(int(input(f"Enter first element of sublist{i+1}:")))
    sub.append(int(input(f"Enter second element of sublist{i+1}:")))
    lst.append(sub)

for i in range(len(lst)-1):
    for j in range(len(lst)-i-1):
        if lst[j][1]>lst[j+1][1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]

print("Sorted List: ",lst)
