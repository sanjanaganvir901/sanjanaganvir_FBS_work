n=int(input("Enter number of elements: "))
list1=[]

for i in range(n):
    num=int(input(f" Enter number{i+1}:"))
    list1+=[num]

x=int(input("Enter element to remove: "))

k=0
for i in range(len(list1)):
    if list1[i]!=x:
        list1[k]=list1[i]
        k+=1

list1=list1[:k]
print("List after removing all occurence of",x,":",list1)
