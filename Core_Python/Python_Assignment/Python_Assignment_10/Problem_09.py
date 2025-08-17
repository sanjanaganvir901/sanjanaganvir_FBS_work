n=int(input("Enter a number of elements: "))
list1=[]


for i in range(n):
    num=int(input(f" Enter number{i+1}:"))
    list1.append(num)

even_list=[]
odd_list=[]

for num in list1:
    if num%2==0:
        even_list.append(num)

    else:
        odd_list.append(num)

print("Original list: ",list1)
print("Even list:",even_list)
print("Odd list: ",odd_list)