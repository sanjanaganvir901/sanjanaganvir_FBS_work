n=int(input("enter the number of elements: "))

list1=[]
for i in range(n):
    num=int(input(f"Enter number{i+1}:"))
    list1.append(num)
print("Original list: ",list1)
reversed_list=[]
for i in range(len (list1)-1,-1,-1):
    reversed_list.append(list1[i])
print("Reverse list: ",reversed_list)