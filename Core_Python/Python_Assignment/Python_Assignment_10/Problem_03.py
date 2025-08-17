n=int(input("enter the number of elements: "))

list1=[]
for i in range(n):
    num=int(input(f"Enter number{i+1}:"))
    list1.append(num)

max_num=list1[0]
sec_max=list1[0]

for i in range(1,len(list1)):
    if(list1[i]>max_num):
        sec_max=max_num
        max_num=list1[i]
    elif(list1[i]>sec_max and list1[i]!=max_num):
        sec_max=list1[i]

print("List :",list1)
print("Second largest element:",sec_max)
               