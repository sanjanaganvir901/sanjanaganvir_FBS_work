n=int(input("Enter the list: "))
list1=[]

for i in range (n):
    num=int(input(f"Enter number{i+1}: "))
    list1+=[num]
maximum=list1[0]
minimum=list1[0]

for i in range(1,n):
    if list1[i]>maximum:
        maximum=list1[i]
    if list1[i]<minimum:
        minimum=list1[i]

print("Maximum element: ",maximum)
print("Minimum element: ",minimum)

