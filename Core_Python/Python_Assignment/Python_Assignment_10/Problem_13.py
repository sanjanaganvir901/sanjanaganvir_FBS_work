n=int(input("Enter number of elements: "))
list1=[]

for i in range(n):
    num=int(input(f"Enter number{i+1}:"))
    list1+=[num]

k=0
for i in range(len(list1)):
    if list1[i]%2!=0:
            list1[k]=list1[i]
            k+=1       
list1=list1[:k]

print("List after removing even list1: ",list1)